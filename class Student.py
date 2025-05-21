class Student:
    total_students = 0  # class variable

    def __init__(self, name, grade):
        self.name = name          # instance variable
        self.grade = grade
        Student.total_students += 1

    def get_details(self):  # instance method
        return f"{self.name} - Grade {self.grade}"

    @classmethod
    def get_total_students(cls):  # class method
        return f"Total Students: {cls.total_students}"

# Test
s1 = Student("John", 10)

s2 = Student("Alice", 12)

print(s1.get_details()) 
print(s2.get_details())
print(Student.get_total_students())  # Total Students: 2
