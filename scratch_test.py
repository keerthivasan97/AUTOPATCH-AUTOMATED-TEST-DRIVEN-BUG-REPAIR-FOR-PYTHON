from autopatch.capture import run_test
from autopatch.prompt import generate_fix

result = run_test("test_calculator.py", "practice_repo")
print("Passed:", result["passed"])
print(result["stdout"])

if not result["passed"]:
    with open("practice_repo/calculator.py") as f:
        src_code = f.read()
    fix = generate_fix(result["stdout"],src_code)
    print("Suggested Fix:\n", fix)
    print(fix)