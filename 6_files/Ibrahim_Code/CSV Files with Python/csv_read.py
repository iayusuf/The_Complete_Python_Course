
file = open('csv_data.txt', 'r')
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines[1:]]

for line in lines:
    person_data = line.split(',')
    name = person_data[0].title()
    age = person_data[1]
    university = person_data[2].title()
    degree = person_data[3].capitalize()

    #print(f'{name.title()} is {age}, studying {degree.capitalize()} at {university.title()}.')
    print(f'{name.title()} is {age}, studying {degree.capitalize()} at {university.title()}.')

#This is how you would print CSV formated list
sample_csv_value = ','.join(['Ibrahim', '33', 'Royal Holloway', 'Computer Science'])
print(sample_csv_value)

#This is how you would write to a CSV file
csv_file = open('csv_data.txt', 'a')
csv_file.write(sample_csv_value)
csv_file.close()
