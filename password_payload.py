import random
import string


def password_payload(lenght=5, lowercase_characters=True, uppercase_character=False, numbers=False,
                     special_characters=False):
    char = string.ascii_lowercase
    if uppercase_character:
        char = string.ascii_uppercase
    if lowercase_characters:
        char = string.ascii_lowercase
    if special_characters:
        char = string.punctuation
    if numbers:
        char = string.digits
    password = []
    for i in range(lenght):
        generated_char = random.choice(char)
        password.append(generated_char)
    print(''.join(password))


password_payload(lenght=3, uppercase_character=True)
