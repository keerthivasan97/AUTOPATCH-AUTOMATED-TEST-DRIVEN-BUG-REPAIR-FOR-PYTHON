import subprocess

def run_test(test_path: str, repo_path: str):
    result = subprocess.run(
        ["pytest", test_path, "-v"],
        cwd=repo_path,
        capture_output=True,
        text=True,
        timeout=30
    )
    return {
        "passed": result.returncode == 0,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }