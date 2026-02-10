"""
LiteLLM Demo - Unified API for Multiple LLM Providers

This example demonstrates how to use litellm to interact with different
LLM providers (OpenAI, Anthropic, etc.) using a single unified interface.

Prerequisites:
    pip install litellm openai anthropic
    
    Set environment variables:
    - OPENAI_API_KEY
    - ANTHROPIC_API_KEY (optional)

Features demonstrated:
1. Simple chat completions with different providers
2. Streaming responses
3. Cost comparison between models
4. Automatic fallback between providers
5. Model comparison
"""

import os
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from utils.litellm_helpers import (
    LiteLLMClient,
    chat_completion,
    get_available_models,
    get_model_info,
    compare_models,
)
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def example_1_simple_chat():
    """Example 1: Simple chat completion with different providers."""
    print("\n" + "="*60)
    print("Example 1: Simple Chat Completion")
    print("="*60)
    
    # Test with OpenAI
    print("\n1a. Using OpenAI (gpt-3.5-turbo):")
    try:
        response = chat_completion(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Explain quantum computing in one sentence."}
            ],
            temperature=0.7
        )
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test with Anthropic (if API key is available)
    print("\n1b. Using Anthropic (claude-3-haiku):")
    if os.getenv("ANTHROPIC_API_KEY"):
        try:
            response = chat_completion(
                model="claude-3-haiku-20240307",
                messages=[
                    {"role": "user", "content": "Explain quantum computing in one sentence."}
                ],
                temperature=0.7
            )
            print(f"Response: {response}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Skipped: ANTHROPIC_API_KEY not set")


def example_2_streaming():
    """Example 2: Streaming responses."""
    print("\n" + "="*60)
    print("Example 2: Streaming Response")
    print("="*60)
    
    print("\nStreaming from gpt-3.5-turbo:")
    try:
        stream = chat_completion(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Write a haiku about coding."}
            ],
            stream=True
        )
        
        print("Response: ", end="", flush=True)
        for chunk in stream:
            print(chunk, end="", flush=True)
        print()  # New line after streaming
        
    except Exception as e:
        print(f"Error: {e}")


def example_3_client_class():
    """Example 3: Using the LiteLLMClient class."""
    print("\n" + "="*60)
    print("Example 3: Using LiteLLMClient Class")
    print("="*60)
    
    # Initialize client with default model
    client = LiteLLMClient(
        default_model="gpt-3.5-turbo",
        temperature=0.7,
        max_tokens=100
    )
    
    print("\n3a. Simple chat:")
    try:
        response = client.chat(
            messages=[
                {"role": "system", "content": "You are a Python expert."},
                {"role": "user", "content": "What is a list comprehension?"}
            ]
        )
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n3b. Override model per request:")
    try:
        response = client.chat(
            messages=[
                {"role": "user", "content": "Say hello in French!"}
            ],
            model="gpt-4",  # Override default model
            temperature=0.9
        )
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error: {e}")


def example_4_model_info():
    """Example 4: Getting model information."""
    print("\n" + "="*60)
    print("Example 4: Model Information")
    print("="*60)
    
    # List available models by provider
    print("\n4a. Available models by provider:")
    models = get_available_models()
    for provider, model_list in models.items():
        print(f"\n{provider.upper()}:")
        for model in model_list[:3]:  # Show first 3 models
            print(f"  - {model}")
    
    # Get specific model info
    print("\n4b. Detailed model information:")
    for model_name in ["gpt-3.5-turbo", "gpt-4", "claude-3-sonnet-20240229"]:
        info = get_model_info(model_name)
        print(f"\n{model_name}:")
        print(f"  Provider: {info['provider']}")
        print(f"  Max tokens: {info['max_tokens']}")
        print(f"  Supports functions: {info['supports_functions']}")
        print(f"  Supports vision: {info['supports_vision']}")


def example_5_cost_tracking():
    """Example 5: Cost tracking and comparison."""
    print("\n" + "="*60)
    print("Example 5: Cost Tracking")
    print("="*60)
    
    client = LiteLLMClient()
    
    # Make a request and track cost
    print("\nMaking request and calculating cost:")
    try:
        from litellm import completion
        
        response = completion(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Explain machine learning in 50 words."}
            ]
        )
        
        # Get token usage
        prompt_tokens = response.usage.prompt_tokens
        completion_tokens = response.usage.completion_tokens
        total_tokens = response.usage.total_tokens
        
        # Calculate cost
        cost = client.get_cost(
            model="gpt-3.5-turbo",
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens
        )
        
        print(f"Response: {response.choices[0].message.content}")
        print(f"\nToken usage:")
        print(f"  Prompt tokens: {prompt_tokens}")
        print(f"  Completion tokens: {completion_tokens}")
        print(f"  Total tokens: {total_tokens}")
        print(f"  Cost: ${cost:.6f}")
        
    except Exception as e:
        print(f"Error: {e}")


def example_6_model_comparison():
    """Example 6: Compare responses from multiple models."""
    print("\n" + "="*60)
    print("Example 6: Model Comparison")
    print("="*60)
    
    prompt = "Explain the concept of recursion in programming in one sentence."
    
    # Only compare models where we have API keys
    models_to_compare = ["gpt-3.5-turbo"]
    
    if os.getenv("ANTHROPIC_API_KEY"):
        models_to_compare.append("claude-3-haiku-20240307")
    
    print(f"\nComparing models: {', '.join(models_to_compare)}")
    print(f"Prompt: {prompt}")
    print()
    
    try:
        results = compare_models(
            prompt=prompt,
            models=models_to_compare,
            temperature=0.7,
            max_tokens=100
        )
        
        for model, info in results.items():
            print(f"\n{model}:")
            if "error" in info:
                print(f"  Error: {info['error']}")
            else:
                print(f"  Response: {info['response']}")
                print(f"  Latency: {info['latency']:.2f}s")
                print(f"  Tokens: {info['total_tokens']} ({info['prompt_tokens']} + {info['completion_tokens']})")
                print(f"  Cost: ${info['cost']:.6f}")
    
    except Exception as e:
        print(f"Error: {e}")


def example_7_fallback():
    """Example 7: Automatic fallback between models."""
    print("\n" + "="*60)
    print("Example 7: Fallback Between Models")
    print("="*60)
    
    # Try multiple models in order of preference
    models = ["gpt-4", "gpt-3.5-turbo"]
    messages = [{"role": "user", "content": "Hello, how are you?"}]
    
    print("\nTrying models in order:", ", ".join(models))
    
    for model in models:
        print(f"\nAttempting {model}...")
        try:
            response = chat_completion(
                model=model,
                messages=messages
            )
            print(f"✓ Success with {model}")
            print(f"Response: {response}")
            break  # Success, no need to try other models
        
        except Exception as e:
            print(f"✗ Failed with {model}: {e}")
            print("Trying next model...")
    else:
        print("\n✗ All models failed!")


def example_8_multi_turn_conversation():
    """Example 8: Multi-turn conversation."""
    print("\n" + "="*60)
    print("Example 8: Multi-turn Conversation")
    print("="*60)
    
    client = LiteLLMClient(default_model="gpt-3.5-turbo")
    
    # Conversation history
    messages = [
        {"role": "system", "content": "You are a helpful math tutor."}
    ]
    
    # Simulate a conversation
    conversation = [
        "What is 2 + 2?",
        "What is the square of that number?",
        "Now multiply that by 3"
    ]
    
    print("\nConversation:")
    for user_message in conversation:
        # Add user message
        messages.append({"role": "user", "content": user_message})
        print(f"\nUser: {user_message}")
        
        try:
            # Get assistant response
            response = client.chat(messages=messages)
            print(f"Assistant: {response}")
            
            # Add assistant response to history
            messages.append({"role": "assistant", "content": response})
        
        except Exception as e:
            print(f"Error: {e}")
            break


def main():
    """Run all examples."""
    print("\n" + "="*60)
    print("LiteLLM Demo - Unified Multi-Provider Interface")
    print("="*60)
    
    # Check for API keys
    if not os.getenv("OPENAI_API_KEY"):
        print("\n⚠️  Warning: OPENAI_API_KEY not set in environment")
        print("Please set your API key to run these examples:")
        print("  export OPENAI_API_KEY='your-key-here'")
        return
    
    print("\n✓ OpenAI API key found")
    
    if os.getenv("ANTHROPIC_API_KEY"):
        print("✓ Anthropic API key found")
    else:
        print("ℹ Anthropic API key not found (optional)")
    
    # Run examples
    try:
        example_1_simple_chat()
        example_2_streaming()
        example_3_client_class()
        example_4_model_info()
        example_5_cost_tracking()
        example_6_model_comparison()
        example_7_fallback()
        example_8_multi_turn_conversation()
        
    except KeyboardInterrupt:
        print("\n\nExamples interrupted by user")
    
    except Exception as e:
        print(f"\n\nUnexpected error: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n" + "="*60)
    print("Demo Complete!")
    print("="*60)


if __name__ == "__main__":
    main()
