import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

    # Check if file_path is inside working_directory
    valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

    if not valid_target_file:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    # Check if file_path is a directory
    if not os.path.isfile(target_file):
        return f'Error: "{file_path}" does not exist or is not a regular file'

    # Check if the file_path is a python file
    if not target_file.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file'

    try:
        command = ['python', target_file]

        if args:
            command.extend(args)
    
        result = subprocess.run(command, cwd=working_dir_abs, capture_output=True, text=True, timeout=30)

        output = ""
        
        if result.returncode != 0:
            output += f'Process exited with code {result.returncode}'
        
        if not result.stdout and not result.stderr:
            output += 'No output produced'

        else:
            output += f'STDOUT: {result.stdout}\n STDERR: {result.stderr}'

        return output

    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns its stdout/stderr output, with a 30 second timeout",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the .py file to execute, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                ),
                description="Optional list of command-line arguments to pass to the Python file",
            ),
        },
        required=["file_path"],
    ),
)