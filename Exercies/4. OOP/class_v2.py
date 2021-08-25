class Student:

    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades


    def average(self):
        return sum(self.grades) / len(self.grades)

# I want the below method to display "Rolf Smith, has 86.75"
    def display(self):
        av = average()
        print(f"{self.name}, has {av}")

student_one = Student('Rolf Smith', [70, 88, 90, 99])
student_two = Student('Jose', [50, 60, 99, 100])


print(student_one.name)
print(student_one.average())

# My display method should achieve this
av = student_one.average()
name = student_one.name

print(f"{name}, has {av}")

