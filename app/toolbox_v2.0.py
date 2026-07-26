from datetime import datetime

APP_NAME = "Developer Toolbox"
VERSION = "2.0"

def show_banner(title):
    print("=" * 40)
    print(title)
    print("=" * 40)

def show_menu():
    print("1. Greet User")
    print("2. Check Age")
    print("3. Show Current Year")
    print("4. Show Current Date & Time")
    print("5. Exit")

def greet(name):
    print(f"Welcome {name}!")

def check_age(age):
    if age >= 18:
        print("Adult")
    else:
        print("Minor")

def show_current_year():
    print(f"Current year is: " + datetime.today().strftime("%Y"))

def show_current_date_time():
    print(datetime.today())
    print("Today is: " + datetime.today().strftime("%A %d-%m-%Y"))
    print("Current Time is:" + datetime.today().strftime("%H:%M:%S"))

def main():
    while True:
        show_banner(f"{APP_NAME} v{VERSION}")
        print()
        show_menu()
        choice = int(input("Select option (1-5): "))
        if choice == 1:
            name=input("Enter your name: ")
            greet(name)
        elif choice == 2:
            age = int(input("Enter your age: "))
            check_age(age)
        elif choice == 3:
            show_current_year()
        elif choice == 4:
            show_current_date_time()
        elif choice == 5:
            print("Thank you for using Developer Toolbox.")
            break
        else:
            print("Invalid Option. Please Enter (1-5).")

if __name__ == "__main__":
    main()

	



