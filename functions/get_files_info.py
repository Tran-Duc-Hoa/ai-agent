import os


def get_files_info(working_directory, directory=None):
    try:
        if directory:
            full_path = os.path.abspath(
                os.path.join(working_directory, directory))
        else:
            full_path = os.path.abspath(working_directory)
        if directory and not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'

        working_directory_abs = os.path.abspath(working_directory)
        if not full_path.startswith(working_directory_abs):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        entries = []
        for entry in os.listdir(full_path):
            entry_path = os.path.join(full_path, entry)
            is_dir = os.path.isdir(entry_path)
            try:
                file_size = os.path.getsize(entry_path)
            except Exception as e:
                return f"Error: Could not get size for '{entry}': {e}"
            entries.append(
                f"- {entry}: file_size={file_size} bytes, is_dir={is_dir}")

        return "\n".join(entries)
    except Exception as e:
        return f"Error: {e}"

    # Continue with your logic here, e.g., listing files, etc.
