contacts = {
    "Ali": "03001234567",
    "Ahmed": "03111234567",
    "Sara": "03221234567"
}

contact_name = input("Enter contact name to find: ")
number = contacts.get(contact_name)
if number:
    print(f"Contact number of {contact_name}: {number}")
else:
    print("Contact not found.")