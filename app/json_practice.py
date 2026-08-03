import json

#student = {
#    "name": "Ali",
#    "marks": 95,
#    "grade": "A"
#}

#with open("student.json","w") as file:
#    json.dump(student, file, indent=8)

#print("Student data saved successfully.")

with open("student.json", "r") as file:
    student = json.load(file)

print(student)
print(type(student))
print(student["name"])
print(student["grade"])

#json_student = json.dumps(student)
#print(json_student)

#print(type(student))
#print(type(json_student))

#book = {
#    "title": "Python Basics",
#    "author": "John",
#    "pages": 350,
#    "available": True
#}

#print(book)
#print(type(book))
#json_book = json.dumps(book)
#print(json_book)
#print(type(json_book))

