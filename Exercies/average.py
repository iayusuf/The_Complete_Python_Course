
#
# # My own code = working
#
# total = 0
# # my_student  = {
#     'name': 'Rolf',
#     'grade': [70, 88, 90, 99]
# }
#
# def average():
#     total = (sum(my_student["grade"]))
#     number_of_grades = len(my_student["grade"])
#     average = total / number_of_grades
#
#     #print(total)
#     #print(number_of_grades)
#     print(average)
#
# name = my_student["name"]
#
# print(f"{name} has an average grade of:")
# average()

#Solution from instructor

my_student  = {
    'name': 'Rolf',
    'grades': [70, 88, 90, 99]
}
def average_grade(student):
    return sum(student['grades']) / len(student['grades'])
print(average_grade(my_student))