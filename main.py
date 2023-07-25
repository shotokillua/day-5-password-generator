import random

letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

symbols_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']

numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

print("Welcome to the PyPassword Generator!")

num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))

password = []
for letter in range(num_letters):
    random_letter = random.choice(letters_list)
    password.append(random_letter)

for symbol in range(num_symbols):
    random_symbol = random.choice(symbols_list)
    password.append(random_symbol)

for number in range(num_numbers):
    random_number = random.choice(numbers_list)
    password.append(random_number)

print(password)

random.shuffle(password)

print(password)

password_string = ""
for char in password:
    password_string += char

print(f"Your password is: {password_string}")