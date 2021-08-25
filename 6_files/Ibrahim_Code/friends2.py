
class Friends():

    def __init__(self, friend1, friend2, friend3):
        self.friend2_name = friend2
        self.friend2_name = friend2
        self.friend3_name = friend3

    def name_input(self):
        friend1_name = input("Enter the first friend's name: ")
        friend2_name = input("Enter the second friend's name: ")
        friend3_name = input("Enter the thirst friend's name: ")

    def open_fil_for_r(self):
        my_file = open('people.txt', 'r')
        file_content = my_file.readlines()
        # This removes whitespace characters like `\n` at the end of each line
        file_content = [x.strip() for x in file_content]
        my_file.close()


    def open_file_for_a(self):
        if friend in file_content:
            print("Your friend", friend, "is a nearby friend")
            my_file_writing = open('nearby_friends.txt', 'a')
            my_file_writing.write(friend)
            my_file_writing.write("\n")
            my_file_writing()



print(name_input())



"""
my_file = open('people.txt', 'r')
file_content = my_file.readlines()
# This removes whitespace characters like `\n` at the end of each line
file_content = [x.strip() for x in file_content]

if friend1 in file_content:
    print("Your friend", friend1, "is a nearby friend")
    my_file_writing = open('nearby_friends.txt', 'a')
    my_file_writing.write(friend1)
    my_file_writing.write("\n")

if friend2 in file_content:
    print("Your friend", friend2, "is a nearby friend")
    my_file_writing = open('nearby_friends.txt', 'a')
    my_file_writing.write(friend2)
    my_file_writing.write("\n")

if friend3 in file_content:
    print("Your friend", friend3, "is a nearby friend")
    my_file_writing = open('nearby_friends.txt', 'a')
    my_file_writing.write(friend3)
    my_file_writing.write("\n")

print("Exiting")

my_file.close()
my_file_writing()
"""




