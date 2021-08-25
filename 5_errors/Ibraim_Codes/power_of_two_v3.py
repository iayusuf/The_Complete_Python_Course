
def power_of_two():
    user_input =input('Please enter a number: ')
    try:
        n = float(user_input)
    except ValueError:
        print('Your input was invalid.')
        n = 0
    finally:
        n_square = n ** 2
        return n_square

print(power_of_two())
print(power_of_two())
