import random
import string

print("===== RANDOM PASSWORD GENERATOR =====")

length = int(input("Enter the password length: "))

if length < 4:
    print("Password length must be at least 4.")

else:
    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    all_characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    remaining = [
        random.choice(all_characters)
        for _ in range(length - 4)
    ]

    password_list = [
        uppercase,
        lowercase,
        digit,
        special
    ] + remaining

    random.shuffle(password_list)

    password = "".join(password_list)

    print("\nYour generated password is:", password)
