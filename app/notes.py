def save_note():
    note=input("Enter your note: ")
    with open("notes.txt","a") as file:
        file.write(note + "\n")
    print("Note saved successfully.")

def read_note():
    with open("notes.txt", "r") as file:
        content = file.read()
        if content:
            print(file.read())
        else:
            print("No Notes available!")
