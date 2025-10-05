import pytest

def test_sample_function():
    """Sample test to demonstrate CI functionality."""
    assert 2 + 2 == 4

def test_imports():
    """Test that required packages can be imported."""
    try:
        import requests
        import pandas
        import numpy
        assert True, "All packages imported successfully"
    except ImportError as e:
        pytest.fail(f"Failed to import required package: {e}")

def test_cache_environment():
    """Test that we're running in the expected CI environment."""
    import os
    
    # Check if we're in GitHub Actions
    if 'GITHUB_ACTIONS' in os.environ:
        assert os.environ['GITHUB_ACTIONS'] == 'true'
        print("✅ Running in GitHub Actions environment")
    
    # Test Python version
    import sys
    assert sys.version_info.major == 3
    print(f"✅ Python version: {sys.version}")

if __name__ == "__main__":
    test_sample_function()
    test_imports()
    test_cache_environment()
    print("🧪 All tests passed!")
