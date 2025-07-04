from functions.write_file import write_file


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
    result = write_file("calculator", "lorem.txt",
                        "wait, this isn't lorem ipsum")
    print(result)
    result = write_file("calculator", "pkg/morelorem.txt",
                        "lorem ipsum dolor sit amet")
    print(result)
    result = write_file("calculator", "/tmp/temp.txt",
                        "this should not be allowed")
    print(result)
