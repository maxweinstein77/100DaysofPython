import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level
password = []

for letter in range(nr_letters):
    random_letters = random.choice(letters)
    password.append(random_letters)

for symbol in range(nr_symbols):
    random_symbols = random.choice(symbols)
    password.append(random_symbols)

for number in range(nr_numbers):
    random_numbers = random.choice(numbers)
    password.append(random_numbers)

password = "".join(password)

print(f"Your password is: {password}")

# Hard Level

password = []

for letter in range(nr_letters):
    random_letters = random.choice(letters)
    password.append(random_letters)

for symbol in range(nr_symbols):
    random_symbols = random.choice(symbols)
    password.append(random_symbols)

for number in range(nr_numbers):
    random_numbers = random.choice(numbers)
    password.append(random_numbers)

password = "".join(password)

hard_password = list(password)

random.shuffle(hard_password)

hard_password = "".join(hard_password)

print(f"Your password is: {hard_password}")