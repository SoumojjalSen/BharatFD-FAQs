"""Description: This file contains the test cases for linting the code.
Returns:
    None
"""
import subprocess


def test_flake8_compliance():
    """Test that the code is flake8 compliant."""
    result = subprocess.run(
        ['flake8', 'api'], capture_output=True, text=True, check=False)
    assert result.returncode == 0, f"Flake8 found violations:\n{result.stdout}"
