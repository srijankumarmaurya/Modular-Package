import datetime as datetime
import math
import time 
import uuid
import random

def date_time_operations():

    while True:
        print("Display of usage of modules")
        print()
        print("1. Display current date and time")
        print("2. Display difference between two dates")
        print("3. Format dates into custom formats using strftime()")
        print("4. Simple time stopwatch using time module")
        print("5. Generate a random number")
        print("6. Countdown")
        print("7. Back to main menu")
        print()
        raw_choice = input("Enter your choice (1-7): ")

        if not raw_choice.isdigit():
            print("Invalid input! Please enter a number between 1 and 7.")
            choice = None
        else:
            choice = int(raw_choice)
        print()
        if choice == 1:
            current_date_time= datetime.datetime.now()
            print(current_date_time)
            print()
        elif choice==2:
            date1=input("Enter the first date yyyy/mm/dd:  ")
            date2=input("Enter the second date yyyy/mm/dd:  ")
            date1=datetime.datetime.strptime(date1,"%Y/%m/%d")
            date2=datetime.datetime.strptime(date2,"%Y/%m/%d")
            diff=date2-date1
            print(f"The difference between the two dates is {diff.days} days.")
            print()

        elif choice==3:
            print("1. Custom time")
            print("2. Custom date")
            choice=int(input("Enter your choice from 1-2: "))
            print()
            if choice == 1:
                time_input = input("Enter the time in HH:MM:SS format: ")
                
                time_obj = datetime.datetime.strptime(time_input, "%H:%M:%S") 
                
                print("1. 12-hour format")
                print("2. 24-hour format")
                format_choice = int(input("Enter your choice from 1-2: "))
                if format_choice == 1:
                    print(time_obj.strftime("%I:%M:%S %p"))
                elif format_choice == 2:
                    print(time_obj.strftime("%H:%M:%S"))
                else:
                    print("Invalid choice! Please enter 1 or 2.")
                print()
        elif choice == 4:
            print("Starting stopwatch...")
            start_time = time.time()
            input("Press Enter to stop the stopwatch.")
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Elapsed time: {elapsed_time:.2f} seconds.")
            
        elif choice==5:
            random_number = random.randint(1, 100)
            print(f"Random number generated: {random_number}")
            print()
    
    
        elif choice==6:
            countdown_time = int(input("Enter the countdown time in seconds: "))
        
            for i in range(countdown_time, 0, -1):
                print(i)
                time.sleep(1)
            print("Countdown finished!")
            print()
    
        elif choice==7:
            print("Returning to main menu...")
            break
        print()
def math_operation():
    while True:
        print("Mathematical operations using math module")
        print()
        print("1. Calculate factorial of a number")
        print("2. Solve compound interest")
        print("3. Trigonometric calculations")
        print("4. Area of geometric shapes")
        print("5. back to main menu")
        print()
        raw_choice = input("Enter your choice (1-5): ")
        print()
        if not raw_choice.isdigit():
            print("Invalid input! Please enter a number between 1 and 5.")
            continue
        choice = int(raw_choice)
        print()
        if choice == 1:
            num = int(input("Enter the number you want the factorial of: "))
            if num < 0:
                print("Factorial is not defined for negative numbers.")
            else:
                factorial = math.factorial(num)
                print(f"The factorial of {num} is {factorial}.")
            print()
        elif choice == 2:
            principal= float(input("Enter the principal amount: ")) 
            rate=float(input("Enter the rate of interest (in %): "))
            time_peroid=int(input("Enter the time period (in years): "))
            compound_interest= principal * (1 + rate/100)**time_peroid - principal
            
            print(f"The compound interest is: {compound_interest:.2f}")
            print()
        elif choice==3:
            print("1. Calculate sine")
            print("2. Calculate cosine")
            print("3. Calculate tangent")
            print()
            choice = int(input("Enter your choice (1-3): "))
            print()
            if choice == 1:
                angle = float(input("Enter the angle in degrees: "))
                sine_value = math.sin(math.radians(angle))
                print(f"The sine of {angle} degrees is {sine_value:.2f}.")
                print()
            elif choice == 2:
                angle = float(input("Enter the angle in degrees: "))
                cosine_value = math.cos(math.radians(angle))
                print(f"The cosine of {angle} degrees is {cosine_value:.2f}.")          
          
            elif choice == 3:
                angle = float(input("Enter the angle in degrees: "))
                tangent_value = math.tan(math.radians(angle))
                
                print(f"The tangent of {angle} degrees is {tangent_value:.2f}.")
                print()
        elif choice==4:
            print("1. Area of Circle")
            print("2. Area of Square")
            print("3. Area of Rectangle")
            print("4. Area of Triangle")
            print()
            area_choice = int(input("Enter your choice (1-4): "))
            print()
            if area_choice == 1:
                radius = float(input("Enter the radius of the circle: "))
                area = math.pi * radius ** 2
            
                print(f"The area of the circle is {area:.2f}.")
                print()
            elif area_choice == 2:
                side = float(input("Enter the side length of the square: "))
                area = side ** 2
                print(f"The area of the square is {area:.2f}.")
                print()
            elif area_choice == 3:
                length = float(input("Enter the length of the rectangle: "))
                width = float(input("Enter the width of the rectangle: "))
                area = length * width
                print(f"The area of the rectangle is {area:.2f}.")
                print()
            elif area_choice == 4:
                base = float(input("Enter the base length of the triangle: "))
                height = float(input("Enter the height of the triangle: "))
                area = 0.5 * base * height
                print(f"The area of the triangle is {area:.2f}.")
                print()
        elif choice==5:
            print("Returning to main menu...")
            break
def random_operation():
     while True:
        print("Select an option: ")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")
        print()
        choice = int(input("Enter your choice: "))
        print()
        if choice == 1:
            random_number = random.randint(1, 100)
            print(f"Random number generated: {random_number}")
            print()
        elif choice == 2:
            list_size = int(input("Enter the size of the random list: "))
            random_list = [random.randint(1, 100) for _ in range(list_size)]
            print(f"Random list generated: {random_list}")
        elif choice == 3:
            length = int(input("Enter the desired password length: "))
            characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
            password = ''.join(random.choice(characters) for x in range(length))
            print(f"Random password generated: {password}")
        elif choice == 4:
            otp_length = int(input("Enter the desired OTP length: "))
            otp = ''.join(random.choice("0123456789") for _ in range(otp_length))
            print(f"Random OTP generated: {otp}")
        elif choice == 5:
            print("Returning to main menu...")
            break

def uuid_function():
    id = uuid.uuid4()
    print("\nGenerate Unique Identifiers: ")
    print(f"Generated UUID: {id}") 