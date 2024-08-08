def edit_file(filename):
    try:
        with open(filename, 'a') as f:
            content = input('Enter data to be added: ')
            f.write("\n" + content + "\n")
            print(f'Content added to "{filename}" successfully!')
    except FileNotFoundError:
        print(f"File '{filename}' does not exist.")
    except PermissionError:
        print(f"Permission denied for file '{filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


