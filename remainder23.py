

number = int(input("Enter a number...: "))

print(f"You have entered {number}")

answer = number / 2
print(f"Dividing {number} by 2 is {answer}")

answer = number % 2

print(f"The remainder {answer}")

if answer != 0:
    print(f" {number} is therefore an odd number")
else:
    print(f" {number} is therefore an even number")
