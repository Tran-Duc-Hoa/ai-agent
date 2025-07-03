from functions.get_file_content import get_file_content


def print_result(description, result):
    print(description)
    if isinstance(result, str):
        print(f"    {result}")
    elif isinstance(result, list):
        for entry in result:
            name = entry.get('name')
            size = entry.get('file_size')
            is_dir = entry.get('is_dir')
            print(f" - {name}: file_size={size} bytes, is_dir={is_dir}")
    print()


if __name__ == "__main__":
    # Test 1: List contents of calculator directory
    result = get_file_content("calculator", "main.py")
    print(result)
    result = get_file_content("calculator", "pkg/calculator.py")
    print(result)
    result = get_file_content("calculator", "/bin/cat")
    print(result)
