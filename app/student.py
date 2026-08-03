class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Marks must be between 0 and 100.")

    @property
    def grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 80:
            return "B"
        elif self.__marks >= 70:
            return "C"
        elif self.__marks >= 60:
            return "D"
        else:
            return "F"

students = [
    Student("Ali Hussain Abid", 95),
    Student("Muhammad Abdullah Khan", 88),
    Student("Babur", 76),
    Student("Kashif", 65),
    Student("Nasir", 45)
]
print("+--------------------+----------+--------+" )
print(f"|{'Name'[:20]:^20}|{'Marks':^10}|{'Grade':^8}|")
print("+--------------------+----------+--------+")

for student in students:
    print(f"|{student.name[:20]:<20}|{student.marks:^10}|{student.grade:^8}|")
print("+--------------------+----------+--------+")