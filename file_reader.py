def read_file_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except UnicodeDecodeError:
        try:
            # If UTF-8 fails, try with ISO-8859-1
            with open(file_path, 'r', encoding='iso-8859-1') as file:
                return file.read()
        except Exception as e:
            print(f"Error reading file {file_path}: {str(e)}")
            return ""


if __name__ == "__main__":
    # Test the function
    test_file = "file_crawler.py"  # Assuming this file exists
    content = read_file_content(test_file)
    # Print first 200 characters
    print(f"Content of {test_file}:\n{content[:200]}...")
