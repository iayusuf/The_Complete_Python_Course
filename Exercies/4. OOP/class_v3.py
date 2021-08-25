
# Modified  code. Trying to add a display method
class Student:

    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades


    def average(self):
        return sum(self.grades) / len(self.grades)


# I want the below method to display "Rolf Smith, has 86.75"
    def display(self):
       print(f"{self.name} has an average of {self.average()}")


student_one = Student('Rolf Smith', [70, 88, 90, 99])
student_two = Student('Jose', [50, 60, 99, 100])

student_one.display()
student_two.display()