"""
Module 04 - Exercise 01: Model Selection
==========================================

Task: Research and compare open source models on Hugging Face Hub.

Learning Objectives:
- Navigate Hugging Face Hub programmatically
- Compare model specifications
- Evaluate licensing and use cases
- Make informed model selection decisions

Instructions:
-------------
1. Complete the ModelSelector class
2. Implement comparison logic
3. Create a recommendation system
4. Test with different use cases

Success Criteria:
-----------------
- Find at least 3 models for a given task
- Compare size, license, downloads, and performance
- Return a justified recommendation
- Handle errors gracefully
"""

import os
from typing import List, Dict, Optional
from dotenv import load_dotenv
from huggingface_hub import HfApi, model_info, list_models
from dataclasses import dataclass

load_dotenv()


@dataclass
class ModelInfo:
    """Container for model information."""
    name: str
    downloads: int
    likes: int
    license: Optional[str]
    size_category: str  # small, medium, large
    task: str


class ModelSelector:
    """Research and compare Hugging Face models."""
    
    def __init__(self, token: Optional[str] = None):
        """
        Initialize the model selector.
        
        Args:
            token: Hugging Face API token (optional)
        """
        self.token = token or os.getenv("HUGGINGFACE_TOKEN")
        self.api = HfApi(token=self.token)
    
    def find_models(self, task: str, limit: int = 10) -> List[str]:
        """
        Find models for a specific task.
        
        Args:
            task: Task type (e.g., "text-generation", "summarization")
            limit: Maximum number of models to return
        
        Returns:
            List of model IDs
        
        TODO: Implement this method
        - Use list_models() with appropriate filters
        - Sort by downloads
        - Return model IDs as strings
        """
        # Your code here
        pass
    
    def get_model_details(self, model_id: str) -> ModelInfo:
        """
        Get detailed information about a model.
        
        Args:
            model_id: Full model ID (e.g., "meta-llama/Llama-3.2-3B")
        
        Returns:
            ModelInfo object with key details
        
        TODO: Implement this method
        - Use model_info() to fetch details
        - Extract relevant fields
        - Categorize model size based on parameters
        - Handle missing information gracefully
        """
        # Your code here
        pass
    
    def compare_models(self, model_ids: List[str]) -> Dict[str, ModelInfo]:
        """
        Compare multiple models side by side.
        
        Args:
            model_ids: List of model IDs to compare
        
        Returns:
            Dictionary mapping model IDs to ModelInfo objects
        
        TODO: Implement this method
        - Fetch details for each model
        - Return as dictionary for easy comparison
        - Handle errors for invalid model IDs
        """
        # Your code here
        pass
    
    def recommend_model(self, task: str, criteria: Dict[str, any]) -> str:
        """
        Recommend the best model based on criteria.
        
        Args:
            task: Task type
            criteria: Dictionary with keys like:
                - max_size: "small", "medium", "large"
                - commercial_use: bool
                - min_downloads: int
        
        Returns:
            Recommended model ID with justification
        
        TODO: Implement this method
        - Find models matching the task
        - Filter based on criteria
        - Rank by relevance
        - Return best match with reasoning
        
        Hint: Consider creating a scoring system
        """
        # Your code here
        pass


def test_model_selector():
    """Test the ModelSelector class."""
    
    selector = ModelSelector()
    
    # Test 1: Find text generation models
    print("Test 1: Finding text-generation models...")
    models = selector.find_models("text-generation", limit=5)
    assert len(models) > 0, "Should find at least one model"
    print(f"✓ Found {len(models)} models")
    
    # Test 2: Get model details
    print("\nTest 2: Getting model details...")
    if models:
        details = selector.get_model_details(models[0])
        assert details is not None, "Should return model details"
        print(f"✓ Retrieved details for {details.name}")
    
    # Test 3: Compare models
    print("\nTest 3: Comparing models...")
    comparison = selector.compare_models(models[:3])
    assert len(comparison) > 0, "Should compare models"
    print(f"✓ Compared {len(comparison)} models")
    
    # Test 4: Get recommendation
    print("\nTest 4: Getting recommendation...")
    criteria = {
        "max_size": "medium",
        "commercial_use": True,
        "min_downloads": 1000
    }
    recommendation = selector.recommend_model("text-generation", criteria)
    assert recommendation is not None, "Should return a recommendation"
    print(f"✓ Recommended: {recommendation}")
    
    print("\n✅ All tests passed!")


if __name__ == "__main__":
    # TODO: Complete the implementation and run tests
    # test_model_selector()
    
    # Example usage:
    # selector = ModelSelector()
    # models = selector.find_models("text-generation")
    # print(f"Found models: {models}")
    
    print("TODO: Implement the ModelSelector class methods")
    print("Run test_model_selector() when complete")
