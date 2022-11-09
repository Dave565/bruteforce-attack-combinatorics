import itertools
import string
import time


def guess_common_words(word):
    with open('words.txt', 'r') as words:
        data = words.read().splitlines()

    for count, match in enumerate(data):
        if match == word:
            return f'the word {match} was found on attempt no:{count}'
    return 0


def brute_force(word, min_password_length=4, max_password_length=10, digits=False, symbols=False,
                uppercase=False):
    chars = string.ascii_lowercase
    if digits:
        chars = string.digits + string.ascii_lowercase
    elif symbols:
        chars = string.punctuation + string.ascii_lowercase
    elif uppercase:
        chars = string.ascii_uppercase + string.ascii_lowercase

    attempts = 0
    for wordLength in range(min_password_length, max_password_length):
        for guess in itertools.product(chars, repeat=wordLength):
            attempts += 1
            guess = ''.join(guess)
            if guess == word:
                number_of_attempts = '{:,}'.format(attempts)
                print(attempts)
                print(number_of_attempts)
                if number_of_attempts[::-1] == 1:
                    return f'Your Password \'{search_term}\' was found on the {number_of_attempts}ST guess'
                if number_of_attempts[::-1] == 2:
                    return f'Your Password \'{search_term}\' was found on the {number_of_attempts}ND guess'
                if number_of_attempts[::-1] == 3:
                    return f'Your Password \'{search_term}\' was found on the {number_of_attempts}RD guess'
                else:
                    return f'Your Password \'{search_term}\' was found on the {number_of_attempts}TH guess'


search_term = input('enter your password: ').lower()
start_time = time.time()
common_search = guess_common_words(search_term)
print('Searching...')
if common_search != 0:
    print(common_search)
else:
    request = brute_force(search_term, min_password_length=3, max_password_length=10)
    print(request)
print('Time Taken: ' + str(round(time.time() - start_time, 2)) + 's')
