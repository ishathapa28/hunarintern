def read_file(directory, filename):
    full_path = os.path.join(directory, filename)
    print(f"Attempting to read file: {full_path}")
    print(f"Current working directory: {os.getcwd()}")
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"Content of '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"File '{filename}' does not exist in directory '{directory}'.")
    except PermissionError:
        print(f"Permission denied for reading '{full_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


