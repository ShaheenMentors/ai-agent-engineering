from datetime import datetime

dt = datetime.today()
print(dt.year)
count = 1

while count <= 5:
    print(count)
    count = count + 1

while True:
    name = input("Enter your name (or quit): ")

    if name == "quit":
        break
    print(f"Hello {name}")
