

friend1 = input("Enter the first friend's name: ")
friend2 = input("Enter the second friend's name: ")
friend3 = input("Enter the thirst friend's name: ")

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


