import subprocess


def test_flake8_compliance():
    result = subprocess.run(['flake8', 'api'], capture_output=True, text=True)
    assert result.returncode == 0, f"Flake8 found violations:\n{result.stdout}"
