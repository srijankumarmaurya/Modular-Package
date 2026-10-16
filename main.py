import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from package.math_utils import date_time_operations,math_operation,uuid_function,random_operation
from  package.explore_module import explore_module
from package.file_operation import file_operation 

def main_menu():
    while True:
        print("===== MAIN MENU =====")
        print()
        print("Select an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathemetical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers(UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes(dir())")
        print("7. Exit")
        print()

        choice = input("Enter your choice (1-7): ")
        if not choice.isdigit():
            print("Invalid input! Please enter a number between 1 and 7.")
            continue

        choice = int(choice)
        if choice == 1:
            date_time_operations()
        elif choice == 2:
            math_operation()
        elif choice == 3:
            random_operation()
        elif choice == 4:
            uuid_function()
        elif choice == 5:
            file_operation()
        elif choice == 6:
            explore_module()
        elif choice == 7:
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 7.")
main_menu()