import os


def get_file_content(working_directory, file_path):
    try:
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
        working_directory_abs = os.path.abspath(working_directory)

        if not full_path.startswith(working_directory_abs):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(full_path, 'r', encoding='utf-8') as file:
            content = file.read()

            if len(content) > 10000:
                content = content[:10000] + \
                    f'[...File "{file_path}" truncated at 10000 characters]'
        return content
    except Exception as e:
        return f"Error: {e}"
