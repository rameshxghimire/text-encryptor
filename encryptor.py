"""
 encryptor.py

This is the main file that contains the encryption function.

"""


def encrypt(plaintext, key):
    """
    encrypt encryption function.

    Encrypts the text using the Caesar Cypher method.

    :param plaintext: text block input
    :type plaintext: str
    :param key: key for encryption
    :type key: int
    :return: text block output
    :rtype: str
    """
    cyphertext = ''
    for character in plaintext:
        if character.isalpha():
            number = ord(character)
            number += key
            if character.isupper():
                if number > ord('Z'):
                    number -= 26
                elif number < ord('A'):
                    number += 26
            elif character.islower():
                if number > ord('z'):
                    number -= 26
                elif number < ord('a'):
                    number += 26
            character = chr(number)
        cyphertext += character

    return cyphertext

#     # * Comment the return line and nncomment bellow
#     # * if you need to print the result.
#     print(cyphertext)

#     # ! Test if the function works.
# encrypt('This text here is for encrypting.', 20)
