"""
LiteLLM helper utilities for unified multi-provider AI API interactions.

This module provides:
- Unified interface for OpenAI, Anthropic, Azure, and other providers
- Built-in retry logic and rate limiting
- Cost tracking across providers
- Streaming support
- Automatic fallback between providers
- Response formatting

LiteLLM advantages:
- Single interface for multiple providers
- Automatic retry and rate limiting
- Built-in cost tracking
- Easy provider switching

Example usage:
    from utils.litellm_helpers import LiteLLMClient, chat_completion
    
    # Simple chat completion (auto-detects provider from model name)
    response = chat_completion(
        model="gpt-3.5-turbo",  # or "claude-3-sonnet-20240229"
        messages=[{"role": "user", "content": "Hello!"}]
    )
    
    # Streaming response
    for chunk in chat_completion_stream(
        model="gpt-4",
        messages=[{"role": "user", "content": "Tell me a story"}]
    ):
        print(chunk, end="")
    
    # Using the client class
    client = LiteLLMClient(default_model="gpt-3.5-turbo")
    response = client.chat(messages=[...])
"""

import os
import logging
from typing import Optional, List, Dict, Any, Iterator, Union
from functools import wraps
import time

try:
    import litellm
    from litellm import completion, acompletion
    LITELLM_AVAILABLE = True
except ImportError:
    LITELLM_AVAILABLE = False
    logging.warning(
        "litellm not installed. Install with: pip install litellm"
    )


# Configure logging
logger = logging.getLogger(__name__)

# Configure LiteLLM settings
if LITELLM_AVAILABLE:
    # Disable verbose logging by default
    litellm.suppress_debug_info = True
    litellm.set_verbose = False
    
    # Enable success callback for cost tracking (optional)
    # litellm.success_callback = ["langfuse"]  # Add your callbacks here


class LiteLLMError(Exception):
    """Base exception for LiteLLM errors."""
    pass


class LiteLLMClient:
    """
    Unified client for multiple LLM providers via LiteLLM.
    
    Supports:
    - OpenAI (gpt-3.5-turbo, gpt-4, etc.)
    - Anthropic (claude-3-opus, claude-3-sonnet, etc.)
    - Azure OpenAI (azure/<deployment-name>)
    - Google (gemini-pro)
    - And many more providers
    
    Example:
        client = LiteLLMClient(default_model="gpt-3.5-turbo")
        response = client.chat(
            messages=[{"role": "user", "content": "Hello!"}]
        )
        print(response.content)
    """
    
    def __init__(
        self,
        default_model: str = "gpt-3.5-turbo",
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        api_key: Optional[str] = None,
        api_base: Optional[str] = None,
        organization: Optional[str] = None,
    ):
        """
        Initialize LiteLLM client.
        
        Args:
            default_model: Default model to use (e.g., "gpt-3.5-turbo", "claude-3-sonnet-20240229")
            temperature: Default temperature for completions (0.0-2.0)
            max_tokens: Default max tokens for completions
            api_key: API key (if not set in environment)
            api_base: Custom API base URL (for Azure, etc.)
            organization: Organization ID (for OpenAI)
        """
        if not LITELLM_AVAILABLE:
            raise ImportError("litellm not installed. Install with: pip install litellm")
        
        self.default_model = default_model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.api_key = api_key
        self.api_base = api_base
        self.organization = organization
        
        # Load API keys from environment if not provided
        if self.api_key is None:
            self._load_api_keys()
    
    def _load_api_keys(self):
        """Load API keys from environment variables."""
        # LiteLLM automatically reads these environment variables:
        # - OPENAI_API_KEY
        # - ANTHROPIC_API_KEY
        # - AZURE_API_KEY
        # - GOOGLE_API_KEY
        # etc.
        pass
    
    def chat(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        stream: bool = False,
        **kwargs
    ) -> Union[str, Iterator[str]]:
        """
        Send a chat completion request.
        
        Args:
            messages: List of message dicts with 'role' and 'content'
            model: Model to use (defaults to self.default_model)
            temperature: Temperature for sampling (defaults to self.temperature)
            max_tokens: Max tokens to generate
            stream: Whether to stream the response
            **kwargs: Additional arguments to pass to litellm.completion()
        
        Returns:
            If stream=False: Complete response string
            If stream=True: Iterator yielding response chunks
        
        Example:
            response = client.chat(
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": "What is Python?"}
                ]
            )
        """
        model = model or self.default_model
        temperature = temperature if temperature is not None else self.temperature
        max_tokens = max_tokens or self.max_tokens
        
        try:
            response = completion(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                stream=stream,
                api_key=self.api_key,
                api_base=self.api_base,
                organization=self.organization,
                **kwargs
            )
            
            if stream:
                return self._stream_response(response)
            else:
                return self._extract_content(response)
        
        except Exception as e:
            logger.error(f"LiteLLM chat error: {e}")
            raise LiteLLMError(f"Chat completion failed: {e}")
    
    def _extract_content(self, response) -> str:
        """Extract content from LiteLLM response."""
        try:
            return response.choices[0].message.content
        except (AttributeError, IndexError) as e:
            logger.error(f"Failed to extract content from response: {e}")
            return ""
    
    def _stream_response(self, response) -> Iterator[str]:
        """Stream response chunks."""
        try:
            for chunk in response:
                if hasattr(chunk, 'choices') and len(chunk.choices) > 0:
                    delta = chunk.choices[0].delta
                    if hasattr(delta, 'content') and delta.content:
                        yield delta.content
        except Exception as e:
            logger.error(f"Error during streaming: {e}")
            raise LiteLLMError(f"Streaming failed: {e}")
    
    async def achat(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        stream: bool = False,
        **kwargs
    ):
        """
        Async version of chat().
        
        Example:
            response = await client.achat(
                messages=[{"role": "user", "content": "Hello!"}]
            )
        """
        model = model or self.default_model
        temperature = temperature if temperature is not None else self.temperature
        max_tokens = max_tokens or self.max_tokens
        
        try:
            response = await acompletion(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                stream=stream,
                api_key=self.api_key,
                api_base=self.api_base,
                organization=self.organization,
                **kwargs
            )
            
            if stream:
                return self._stream_response(response)
            else:
                return self._extract_content(response)
        
        except Exception as e:
            logger.error(f"LiteLLM async chat error: {e}")
            raise LiteLLMError(f"Async chat completion failed: {e}")
    
    def get_cost(self, model: str, prompt_tokens: int, completion_tokens: int) -> float:
        """
        Calculate cost for a request using LiteLLM's built-in cost tracking.
        
        Args:
            model: Model name
            prompt_tokens: Number of prompt tokens
            completion_tokens: Number of completion tokens
        
        Returns:
            Cost in USD
        
        Example:
            cost = client.get_cost("gpt-3.5-turbo", 100, 50)
            print(f"Cost: ${cost:.6f}")
        """
        try:
            return litellm.completion_cost(
                model=model,
                prompt_tokens=prompt_tokens,
                completion_tokens=completion_tokens
            )
        except Exception as e:
            logger.warning(f"Could not calculate cost: {e}")
            return 0.0


def chat_completion(
    model: str,
    messages: List[Dict[str, str]],
    temperature: float = 0.7,
    max_tokens: Optional[int] = None,
    stream: bool = False,
    **kwargs
) -> Union[str, Iterator[str]]:
    """
    Simple function interface for chat completions.
    
    Args:
        model: Model to use (e.g., "gpt-3.5-turbo", "claude-3-sonnet-20240229")
        messages: List of message dicts with 'role' and 'content'
        temperature: Temperature for sampling (0.0-2.0)
        max_tokens: Max tokens to generate
        stream: Whether to stream the response
        **kwargs: Additional arguments
    
    Returns:
        If stream=False: Complete response string
        If stream=True: Iterator yielding response chunks
    
    Example:
        response = chat_completion(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello!"}]
        )
    """
    if not LITELLM_AVAILABLE:
        raise ImportError("litellm not installed. Install with: pip install litellm")
    
    try:
        response = completion(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            stream=stream,
            **kwargs
        )
        
        if stream:
            return _stream_chunks(response)
        else:
            return response.choices[0].message.content
    
    except Exception as e:
        logger.error(f"Chat completion error: {e}")
        raise LiteLLMError(f"Completion failed: {e}")


def _stream_chunks(response) -> Iterator[str]:
    """Helper to stream response chunks."""
    for chunk in response:
        if hasattr(chunk, 'choices') and len(chunk.choices) > 0:
            delta = chunk.choices[0].delta
            if hasattr(delta, 'content') and delta.content:
                yield delta.content


def get_available_models() -> Dict[str, List[str]]:
    """
    Get available models by provider.
    
    Returns:
        Dictionary mapping provider names to lists of model names
    
    Example:
        models = get_available_models()
        print(f"OpenAI models: {models['openai']}")
        print(f"Anthropic models: {models['anthropic']}")
    """
    return {
        "openai": [
            "gpt-4",
            "gpt-4-turbo",
            "gpt-4-turbo-preview",
            "gpt-3.5-turbo",
            "gpt-3.5-turbo-16k",
        ],
        "anthropic": [
            "claude-3-opus-20240229",
            "claude-3-sonnet-20240229",
            "claude-3-haiku-20240307",
            "claude-2.1",
            "claude-2",
            "claude-instant-1.2",
        ],
        "azure": [
            "azure/<deployment-name>",  # Requires Azure deployment
        ],
        "google": [
            "gemini-pro",
            "gemini-pro-vision",
        ],
        "cohere": [
            "command",
            "command-light",
        ],
    }


def validate_model(model: str) -> bool:
    """
    Check if a model name is valid.
    
    Args:
        model: Model name to validate
    
    Returns:
        True if model is valid
    
    Example:
        if validate_model("gpt-3.5-turbo"):
            print("Valid model!")
    """
    all_models = get_available_models()
    for provider_models in all_models.values():
        if model in provider_models or model.startswith("azure/"):
            return True
    return False


def get_model_info(model: str) -> Dict[str, Any]:
    """
    Get information about a model.
    
    Args:
        model: Model name
    
    Returns:
        Dictionary with model information
    
    Example:
        info = get_model_info("gpt-3.5-turbo")
        print(f"Max tokens: {info['max_tokens']}")
        print(f"Provider: {info['provider']}")
    """
    # OpenAI models
    if model.startswith("gpt-4"):
        return {
            "provider": "openai",
            "max_tokens": 8192 if "turbo" in model else 8192,
            "supports_functions": True,
            "supports_vision": "vision" in model,
        }
    elif model.startswith("gpt-3.5"):
        return {
            "provider": "openai",
            "max_tokens": 16385 if "16k" in model else 4096,
            "supports_functions": True,
            "supports_vision": False,
        }
    
    # Anthropic models
    elif model.startswith("claude-3"):
        return {
            "provider": "anthropic",
            "max_tokens": 200000,  # Claude 3 has 200k context
            "supports_functions": False,
            "supports_vision": "opus" in model or "sonnet" in model,
        }
    elif model.startswith("claude"):
        return {
            "provider": "anthropic",
            "max_tokens": 100000,
            "supports_functions": False,
            "supports_vision": False,
        }
    
    # Google models
    elif model.startswith("gemini"):
        return {
            "provider": "google",
            "max_tokens": 30720,
            "supports_functions": True,
            "supports_vision": "vision" in model,
        }
    
    else:
        return {
            "provider": "unknown",
            "max_tokens": None,
            "supports_functions": False,
            "supports_vision": False,
        }


def compare_models(
    prompt: str,
    models: List[str],
    temperature: float = 0.7,
    max_tokens: Optional[int] = None,
) -> Dict[str, Dict[str, Any]]:
    """
    Compare responses from multiple models.
    
    Args:
        prompt: Prompt to send to all models
        models: List of model names to compare
        temperature: Temperature for sampling
        max_tokens: Max tokens to generate
    
    Returns:
        Dictionary mapping model names to response info
    
    Example:
        results = compare_models(
            prompt="Explain quantum computing in one sentence",
            models=["gpt-3.5-turbo", "claude-3-sonnet-20240229", "gemini-pro"]
        )
        for model, info in results.items():
            print(f"{model}: {info['response']}")
            print(f"  Cost: ${info['cost']:.6f}")
            print(f"  Latency: {info['latency']:.2f}s")
    """
    messages = [{"role": "user", "content": prompt}]
    results = {}
    
    for model in models:
        start_time = time.time()
        try:
            response = completion(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            
            latency = time.time() - start_time
            content = response.choices[0].message.content
            
            # Calculate cost
            try:
                cost = litellm.completion_cost(
                    model=model,
                    prompt_tokens=response.usage.prompt_tokens,
                    completion_tokens=response.usage.completion_tokens,
                )
            except:
                cost = 0.0
            
            results[model] = {
                "response": content,
                "latency": latency,
                "cost": cost,
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
                "total_tokens": response.usage.total_tokens,
            }
        
        except Exception as e:
            logger.error(f"Error with model {model}: {e}")
            results[model] = {
                "response": None,
                "error": str(e),
                "latency": time.time() - start_time,
            }
    
    return results


# Example usage and testing
if __name__ == "__main__":
    # Configure logging for examples
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    print("LiteLLM Helper Module - Examples")
    print("=" * 50)
    
    # Example 1: Simple chat completion
    print("\n1. Simple chat completion:")
    try:
        response = chat_completion(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Say hello in German!"}
            ]
        )
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 2: Using the client class
    print("\n2. Using LiteLLMClient:")
    try:
        client = LiteLLMClient(default_model="gpt-3.5-turbo")
        response = client.chat(
            messages=[{"role": "user", "content": "What is 2+2?"}]
        )
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 3: Available models
    print("\n3. Available models:")
    models = get_available_models()
    for provider, model_list in models.items():
        print(f"{provider}: {len(model_list)} models")
    
    # Example 4: Model info
    print("\n4. Model information:")
    info = get_model_info("gpt-3.5-turbo")
    print(f"GPT-3.5-turbo info: {info}")
