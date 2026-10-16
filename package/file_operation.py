def create_file():
    name = input("Enter the name of the file to create: ")
    with open(name, 'w') as file:
        pass
    print(f"File '{name}' created successfully.")

def add_entry():
    entry = input("Enter the name of the file to add content to: ")
    content = input("Enter the content you want to add: ")
    with open(entry, 'a') as file:
        file.write(content + '\n')
    print("Content added successfully.")

def read_file():
    name = input("Enter the name of the file to read: ")
    try:
        with open(name, 'r') as file:
            print("--- File Content ---")
            print()
            print(file.read())
            print("--------------------")
    except FileNotFoundError:
        print(f"Error: The file '{name}' does not exist.")

def append_to_file():
    name = input("Enter the name of the file to append content to: ")
    
    with open(name, 'a') as file:
        file.write(name + '\n')
    print(f"Appended '{name}' to the file.")

def file_operation():
    while True:
        print("===== FILE MANAGEMENT MENU =====")
        print()
        print("1. Create a new file")
        print("2. Add entry to a file")
        print("3. Read a file")
        print("4. Append filename to a file")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            create_file()
        elif choice == '2':
            add_entry()
        elif choice == '3':
            read_file()
        elif choice == '4':
            append_to_file()
        elif choice == '5':
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

