from functions.run_python_file import run_python_file

print(f"Result for calculator's usage instructions:\n{run_python_file('calculator', 'main.py')}")
print(f"Result for running the calculator:\n{run_python_file('calculator', 'main.py', ['3 + 5'])}")
print(f"Result for running the calculator's test:\n{run_python_file('calculator', 'tests.py')}")
print(f"Result for running a file outside the dir:\n{run_python_file('calculator', '../main.py')}")
print(f"Result for running an non existent file:\n{run_python_file('calculator', 'nonexistent.py')}")
print(f"Result for running an non python file:\n{run_python_file('calculator', 'lorem.txt')}")