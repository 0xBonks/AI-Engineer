"""Tests for type safety exercises."""
import pytest
from pydantic import ValidationError

def test_pydantic_validation():
    """Test Pydantic validates types."""
    from pydantic import BaseModel
    
    class TestModel(BaseModel):
        value: int
    
    # Valid
    m = TestModel(value=42)
    assert m.value == 42
    
    # Invalid
    with pytest.raises(ValidationError):
        TestModel(value="not an int")

def test_type_coercion():
    """Test Pydantic coerces compatible types."""
    from pydantic import BaseModel
    
    class TestModel(BaseModel):
        count: int
    
    # String number gets converted
    m = TestModel(count="42")
    assert m.count == 42
    assert isinstance(m.count, int)
