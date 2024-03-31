import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
ambiguous_symbols = 'il1Lo0O'

chars = ''


def number_of_passwords():
    print('How many passwords to generate?')
    number_psw = input()
    while not number_psw.isdigit():
        print('Please enter a valid number')
        number_psw = input()
    return int(number_psw)


def length_of_password():
    print('Enter the length of passwords')
    length_psw = input()
    while not length_psw.isdigit():
        print('Please enter a valid number')
        length_psw = input()
    return int(length_psw)


def digits_on():
    print(f'Should we include digits {digits} (Y/N)?')
    if input().lower() in ['y', 'Y', 'д', 'Д']:
        return True
    else:
        return False


def uppercase_letters_on():
    print(f'Should we include uppercase letters {uppercase_letters} (Y/N)?')
    if input().lower() in ['y', 'Y', 'д', 'Д']:
        return True
    else:
        return False


def lowercase_letters_on():
    print(f'Should we include lowercase letters {lowercase_letters} (Y/N)?')
    if input().lower() in ['y', 'Y', 'д', 'Д']:
        return True
    else:
        return False


def punctuation_symbols_on():
    print(f'Should we include punctuation symbols {punctuation} (Y/N)?')
    if input().lower() in ['y', 'Y', 'д', 'Д']:
        return True
    else:
        return False


def ambiguous_symbols_off():
    print(f'Should ambiguous symbols {ambiguous_symbols} be excluded (Y/N)?')
    if input().lower() in ['y', 'Y', 'д', 'Д']:
        return True
    else:
        return False


# Asking user data
number_of_passwords()
length_of_password()
if digits_on():
    chars += digits
if uppercase_letters_on():
    chars += uppercase_letters
if lowercase_letters_on():
    chars += lowercase_letters
if punctuation_symbols_on():
    chars += punctuation
if ambiguous_symbols_off():
    for symbol in chars:
        if symbol in ambiguous_symbols:
            chars = chars.replace(symbol, '')

# Setting up generated passwords
print(f'Available symbols: {chars}')
