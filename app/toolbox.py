APP_NAME = "Developer Toolbox"
VERSION = "1.0"

def show_banner(title):
    print("=" * 40)
    print(title)
    print("=" * 40)


def greet(name):
    print(f"Welcome {name}!")

def main():
    show_banner(APP_NAME + " CLI")
    print()
    name = input("Enter your name: ")
    print()
    greet(name)
    print()
    print(f"Version: {VERSION}")

if __name__ == "__main__":
    main()

	



