student = {
    "name": "Ali",
    "age": 20,
    "city": "Lahore"
}

languages = {
    "py": "Python",
    "js": "JavaScript",
    "cpp": "C++"
}
print(student["name"])
print(student["age"])
print(student["city"])
print(languages["py"])
student["age"] = 21
# print(student["email"])
print(student.get("email"))
student["country"] = "Pakistan"
print(student)