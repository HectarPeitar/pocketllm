import os
from DIRNAME.FILENAME import FUNCTION_NAME

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    full_path = os.path.abspath(full_path)
    working_directory = os.path.abspath(working_directory)

    # Check if full_path is inside working_directory
    if os.path.commonpath([full_path, working_directory]) != working_directory:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    # Check if full_path is a directory
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    
    files = []

    for file in os.listdir(full_path):
        entry_path = os.path.join(full_path, file)
        size = os.path.getsize(entry_path)
        is_dir = os.path.isdir(entry_path)
        files.append(f"- {file}: file_size={size}, is_dir={is_dir}")
    return "\n".join(files)