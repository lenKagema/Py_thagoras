"""
Vigenère Cipher, by Al Sweigart al@inventwithpython.com
The Vigenère cipher is a poly-alphabetic substitution cipher
    that was powerful enough to remain unbroken for centuries.
More info at: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, cryptography, math
"""

try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass

# Every possible symbol that can be encrypted/decrypted:
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    print('''
        Vigenère Cipher, by Al Sweigart al@inventwithpython.com
        The Vigenère cipher is a poly-alphabetic substitution cipher that was
        powerful enough to remain unbroken for centuries.
    ''')

    # Let the user specify if they are encrypting or decrypting:
    while True:
        # Keep asking until the user selects e or d.
        print('Do you want to (e)ncrypt or (d)ecrypt?')
        response = input('> ').lower()
        if response.startswith('e'):
            my_mode = 'encrypt'
            break
        elif response.startswith('d'):
            my_mode = 'decrypt'
            break
        print('Please enter the letter e or d!')

    # Let the user specify the key to use:
    while True:
        # Keep asking until the user enters a valid key.
        print('Please specify the key to use.')
        print('It can be a word or any combination of letters:')
        response = input('> ').lower()
        if response.isalpha():
            my_key = response
            break

    # Let the user specify the message to encrypt/decrypt:
    print('Enter the message to {}.'.format(my_mode))
    my_message = input('> ')

    # Perform the encryption/decryption:
    if my_mode == 'encrypt':
        translated = encryptMessage(my_message, my_key)
    elif my_mode == 'decrypt':
        translated = decryptMessage(my_message, my_key)

    print('%sed message:' % (my_mode.title()))
    print(translated)

    try:
        pyperclip.copy(translated)
        print('Full %sed text copied to clipboard' % (my_mode))
    except:
        pass  # Do nothing if pyperclip wasn't installed.


def encryptMessage(message, key):
    """Encrypt the message using the key."""
    return translateMessage(message, key, 'encrypt')


def decryptMessage(message, key):
    """Decrypt the message using the key."""
    return translateMessage(message, key, 'decrypt')


def translateMessage(message, key, mode):
    """Encrypt or decrypt the message using the key."""
    translated = []  # Stores the encrypted/decrypted message string.

    key_index = 0
    key = key.upper()

    for symbol in message:  # Loop through each character in message.
        num = LETTERS.find(symbol.upper())
        if num != -1:
            if mode == 'encrypt':
                # Add if encrypting:
                num += LETTERS.find(key[key_index])
            elif mode == 'decrypt':
                # Subtract if encrypting:
                num -= LETTERS.find(key[key_index])

            num %= len(LETTERS)  # handle the potential wraparound.

            # Add the encrypted/decrypted symbol to translated
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            key_index += 1  # Move to the next letter in the key.
            if key_index == len(key):
                key_index = 0
        else:
            # Add the symbol without encrypting/decrypting:
            translated.append(symbol)

    return ''.join(translated)


# If the program was run (instead of imported), run the program:
if __name__ == '__main__':
    main()