#To avoid the tons of errors you might see, remove the last block of text in friends_json.txt"
import json

with open('friends_json.txt', 'r') as file:
    file_contents = json.load(file) #reads file and turns it to dictionary


#print(file_contents['friends'],[0])

cars =[
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'},
]

#I investigate on how to use json.dump

with open('cars_json.txt', 'a') as file:
    json.dump(cars, file, indent = 6)

#If you had a string variable and wanted to turn into a dictionary, you do like this

my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'

incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])