app_name = "Developer Toolbox"
version = "1.0"

print(app_name)
print(version)

def show_banner():
    print("=" * 40)
    print("Developer Toolbox CLI")
    print("=" * 40)


show_banner()

def greet(name):
    print(f"Welcome {name}!")
name=input("Enter your name: ")
greet(name)

