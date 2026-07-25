APP_NAME = "Developer Toolbox"
VERSION = "1.0"

def show_banner(title):
    print("=" * 40)
    print(title)
    print("=" * 40)
    print("1. Greet User")
    print("2. Check Age")
    print("3. Exit")

def greet(name):
    print(f"Welcome {name}!")

def check_age(age):
    if age >= 18:
        print("Adult")
    else:
        print("Minor")

def main():
    show_banner(APP_NAME + " v" + VERSION)
    choice = int(input("Select an option: "))
    if choice == 1:
        name = input("Enter your name: ")
        greet(name)
    elif choice == 2:
        age = int(input("Enter your age: "))
        check_age(age)
    elif choice == 3:
        print("Goodbye!")
    else:
        print("Invalid Option. Please select 1, 2 or 3")

if __name__ == "__main__":
    main()