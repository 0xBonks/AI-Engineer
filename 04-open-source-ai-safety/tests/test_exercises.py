"""
Module 04 - Test Suite
=======================

Comprehensive tests for all Module 04 exercises.

Run with: pytest test_exercises.py -v
"""

import pytest
import sys
from pathlib import Path

# Add exercises directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "exercises"))


class TestModule04Setup:
    """Test that environment is set up correctly."""
    
    def test_imports(self):
        """Test that required packages are installed."""
        try:
            import openai
            import huggingface_hub
            from dotenv import load_dotenv
            assert True
        except ImportError as e:
            pytest.fail(f"Missing required package: {e}")
    
    def test_env_file_exists(self):
        """Test that .env file exists."""
        env_file = Path(__file__).parent.parent.parent.parent / ".env"
        if not env_file.exists():
            pytest.skip(".env file not found - API keys may not be configured")


class TestExerciseFiles:
    """Test that exercise files exist and are valid Python."""
    
    @pytest.mark.parametrize("exercise_num", range(1, 7))
    def test_exercise_exists(self, exercise_num):
        """Test that exercise file exists."""
        exercise_names = [
            "model-selection",
            "huggingface-inference",
            "ollama-local",
            "input-validation",
            "output-filtering",
            "adversarial-testing"
        ]
        
        exercise_file = (
            Path(__file__).parent.parent / "exercises" / 
            f"0{exercise_num}-{exercise_names[exercise_num-1]}.py"
        )
        
        assert exercise_file.exists(), f"Exercise file {exercise_file} not found"
    
    @pytest.mark.parametrize("exercise_num", range(1, 7))
    def test_exercise_imports(self, exercise_num):
        """Test that exercise file is valid Python."""
        exercise_names = [
            "model-selection",
            "huggingface-inference",
            "ollama-local",
            "input-validation",
            "output-filtering",
            "adversarial-testing"
        ]
        
        module_name = f"0{exercise_num}-{exercise_names[exercise_num-1]}".replace("-", "_")
        
        try:
            # Compile the file to check syntax
            exercise_file = (
                Path(__file__).parent.parent / "exercises" / 
                f"0{exercise_num}-{exercise_names[exercise_num-1]}.py"
            )
            with open(exercise_file, 'r') as f:
                compile(f.read(), exercise_file, 'exec')
            assert True
        except SyntaxError as e:
            pytest.fail(f"Syntax error in exercise: {e}")


class TestInputValidation:
    """Tests for Exercise 04 - Input Validation."""
    
    def test_pattern_detection_exists(self):
        """Test that InputValidator class exists."""
        from exercises import input_validation
        assert hasattr(input_validation, 'InputValidator')
    
    def test_validation_result_dataclass(self):
        """Test that ValidationResult exists."""
        from exercises import input_validation
        assert hasattr(input_validation, 'ValidationResult')


# Placeholder tests - Students should implement these
class TestStudentImplementations:
    """Tests that verify student implementations."""
    
    def test_model_selector_placeholder(self):
        """
        TODO for students: Implement ModelSelector and enable this test.
        
        This test should verify:
        - ModelSelector.find_models() returns list of model IDs
        - ModelSelector.get_model_details() returns ModelInfo
        - ModelSelector.compare_models() returns comparison dict
        """
        pytest.skip("TODO: Implement in exercise")
    
    def test_inference_wrapper_placeholder(self):
        """
        TODO for students: Implement InferenceWrapper and enable this test.
        
        This test should verify:
        - InferenceWrapper.generate_text() returns InferenceResult
        - InferenceWrapper.generate_with_retry() handles rate limits
        - InferenceWrapper.compare_models() returns list of results
        """
        pytest.skip("TODO: Implement in exercise")
    
    def test_ollama_manager_placeholder(self):
        """
        TODO for students: Implement OllamaManager and enable this test.
        
        This test should verify:
        - OllamaManager.list_models() returns list
        - OllamaManager.generate() returns OllamaResponse
        - OllamaManager.stream_generate() yields tokens
        """
        pytest.skip("TODO: Implement in exercise - requires Ollama running")
    
    def test_input_validator_placeholder(self):
        """
        TODO for students: Implement InputValidator and enable this test.
        
        This test should verify:
        - InputValidator.detect_patterns() finds injection attempts
        - InputValidator.calculate_risk_score() returns 0-100
        - InputValidator.validate() returns ValidationResult
        - Safe inputs pass, malicious inputs blocked
        """
        pytest.skip("TODO: Implement in exercise")
    
    def test_content_moderator_placeholder(self):
        """
        TODO for students: Implement ContentModerator and enable this test.
        
        This test should verify:
        - ContentModerator.moderate() calls OpenAI API
        - ContentModerator.determine_action() returns correct action
        - ContentModerator.log_violation() stores violations
        """
        pytest.skip("TODO: Implement in exercise")
    
    def test_adversarial_tester_placeholder(self):
        """
        TODO for students: Implement AdversarialTester and enable this test.
        
        This test should verify:
        - AdversarialTester.generate_prompt_injection_attacks() creates attacks
        - AdversarialTester.test_system() runs tests
        - AdversarialTester.generate_report() creates VulnerabilityReport
        """
        pytest.skip("TODO: Implement in exercise")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
