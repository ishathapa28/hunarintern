import os

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"File Name {filename}: Created Successfully!")
    except FileExistsError:
        print(f"File Name {filename} already exists")
    except Exception as E:
        print("An error occurred")

def view_all_files(path):
    if os.path.isdir(path):
        files = os.listdir(path)
        print("Files in directory:", files)
    elif os.path.isfile(path):
        print("File path:", path)
    else:
        print("The path is neither a file nor a directory.")

def delete_files(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully")
    except FileExistsError:
        print(f"File Name {filename} already exists")
    except Exception as E:
        print("An error occurred")

def read_file(directory, filename):
    full_path = os.path.join(directory, filename)
    print(f"Attempting to read file: {full_path}")
    print(f"Current working directory: {os.getcwd()}")
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"Content of '{filename}':\n{content}")
    except UnicodeDecodeError:
        print(f"Cannot decode '{filename}' with UTF-8 encoding.")
    except FileNotFoundError:
        print(f"File '{filename}' does not exist in directory '{directory}'.")
    except PermissionError:
        print(f"Permission denied for reading '{full_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def edit_file(filename):
    try:
        with open(filename, 'a') as f:
            content = input('Enter data to be added: ')
            f.write("\n" + content + "\n")
            print('Content added to {filename} Successfully!')
    except FileExistsError:
        print(f"File Name {filename} already exists")
    except Exception as E:
        print("An error occurred")

def main():
    while True:
        print('File Management App:')
        print('1: Create File')
        print('2: View all files')
        print('3: Delete file')
        print('4: Read file')
        print('5: Edit file')
        print('6: Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            filename = input("Enter the filename to be craeted: ")
            create_file(filename)
        elif choice == '2':
            path = input("Enter your path: ")
            view_all_files(path)
        elif choice == '3':
            filename = input('Enter the filename to be deleted: ')
            delete_files(filename)
        elif choice == '4':
            directory = input('Enter the directory path: ')
            filename = input('Enter the filename to be read: ')
            if os.path.isdir(directory):
                read_file(directory, filename)
            else:
                print(f"Directory '{directory}' does not exist.")
        elif choice == '5':
            filename = input('Enter the filename to be edited: ')
            edit_file(filename)
        elif choice == '6':
            print("Closing the app...")
            break
        else:
            print("Invalid syntax")

if __name__ == "__main__":
    main()