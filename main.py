TO_MORSE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ': ' '}

FROM_MORSE_DICT = { '': ' '}
for key, value in TO_MORSE_DICT.items():
    FROM_MORSE_DICT[value] = key


def decrypt_code(code: list):
    decrypted_code = ""
    for item in code:
        try:
            decrypted_code += FROM_MORSE_DICT[item]
        except KeyError:
            print("Warning: Character not found -> "+item)
            exit(1)

    return decrypted_code.replace("  ", " ")


def encrypt_code(code: list):
    encrypted_code = []
    for item in code:
        try:
            encrypted_code.append(TO_MORSE_DICT[item])
        except KeyError:
            print("Warning: Character not found -> "+item)
            exit(1)

    return encrypted_code


if __name__ == '__main__':
    operation = input("Do you want to encode or decode? ")
    message = input(f'Enter message to {operation}: ')
    if len(message) == 0:
        print('Message is empty')
        exit(1)
    else:
        if operation == "encode":
            print(encrypt_code(list(message.upper())))
        elif operation == "decode":
            print(decrypt_code(message.split(" ")))
        else:
            print("Warning: Wrong operation chosen. Please choose between encode or decode")
            exit(1)

