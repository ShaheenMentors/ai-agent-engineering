from datetime import datetime
choice = input("Enter a number (1-3): ")

if choice == "1":
    print("You selected option 1.")
elif choice == "2":
    print("You selected option 2.")
elif choice == "3":
    print("You selected option 3.")
else:
    print("Invalid option.")

def show_current_datetime():
    print("=" * 40)
    print("Current Date & Time")
    print("=" * 40)
    current=datetime.today()
    print(current.strftime("%A, %d %B %Y"))
    print(current.strftime("%I:%M:%S %p"))

show_current_datetime()
