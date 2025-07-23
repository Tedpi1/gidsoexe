class Person:
    person_count = 0  # class variable

    def __init__(self, name, age, national_id):
        self.name = name
        self.age = age
        self.__national_id = national_id  # private attribute
        Person.person_count += 1

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"


class Student(Person):
    def __init__(self, name, age, national_id, student_id):
        super().__init__(name, age, national_id)
        self.student_id = student_id

    def get_role(self):
        return "Student"

    def __str__(self):
        return f"{super().__str__()}, Student ID: {self.student_id}"

    def __repr__(self):
        return f"Student('{self.name}', {self.age}, '{self.student_id}')"


class Teacher(Person):
    def __init__(self, name, age, national_id, employee_id, subject):
        super().__init__(name, age, national_id)
        self.employee_id = employee_id
        self.subject = subject

    def get_role(self):
        return "Teacher"

    def __str__(self):
        return f"{super().__str__()}, Employee ID: {self.employee_id}, Subject: {self.subject}"

    def __repr__(self):
        return f"Teacher('{self.name}', {self.age}, '{self.employee_id}', '{self.subject}')"


# ✅ Test the classes
s1 = Student("Alice", 19, "ID001", "S101")
t1 = Teacher("Mr. Smith", 40, "ID002", "T202", "Math")

print(s1)         # __str__
print(t1)
print(repr(s1))   # __repr__
print(repr(t1))

print(s1.get_role())  # Polymorphism
print(t1.get_role())

print("Total people created:", Person.person_count)
