import os

def get_files_info(working_directory, directory="."):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

    # Check if full_path is inside working_directory
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    # Check if full_path is a directory
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    try:
        files = []
        for file in os.listdir(target_dir):
            entry_path = os.path.join(target_dir, file)
            size = os.path.getsize(entry_path)
            is_dir = os.path.isdir(entry_path)
            files.append(f"- {file}: file_size={size}, is_dir={is_dir}")
        return "\n".join(files)
    except Exception as e:
        return f'Error: {e}'