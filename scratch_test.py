from autopatch.capture import run_test

result = run_test("test_calculator.py", "practice_repo")
print("Passed:", result["passed"])
print(result["stdout"])