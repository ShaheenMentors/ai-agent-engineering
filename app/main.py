from app.greetings import greet
from app.datetime_utils import (
    show_current_year,
    show_current_datetime
)

from app.notes import (
    read_note,
    save_note
)

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
    print("5. Save Note")
    print("6. Read Note")
    print("7. Exit")

def check_age(age):
    if age >= 18:
        print("Adult")
    else:
        print("Minor")


def main():
    while True:
        try:
            show_banner(f"{APP_NAME} v{VERSION}")
            print()
            show_menu()
            choice = int(input("Select option (1-7): "))
            if choice == 1:
                name=input("Enter your name: ")
                greet(name)
            elif choice == 2:
                try:
                    age = int(input("Enter your age: "))
                    check_age(age)
                except ValueError:
                    print("Invalid age. Please enter a number.")
            elif choice == 3:
                show_current_year()
            elif choice == 4:
                show_current_datetime()
            elif choice == 5:
                save_note()
            elif choice == 6:
                try:
                    read_note()
                except FileNotFoundError:
                    print("File does not exist!")
            elif choice == 7:
                print("Thank you for using Developer Toolbox.")
                break
            else:
                print("Invalid Option. Please Enter (1-7).")
        except ValueError:
            print("Please enter a number between 1 and 7.")
if __name__ == "__main__":
    main()

	



