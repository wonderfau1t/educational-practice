def encode_string(string: str) -> str:
    """
    Encoding/decoding string with ROT13
    :param string: string to decode/encode
    :return: encoded/decoded string
    """
    encoded_string = ''
    # Encode/decode every char in string
    for char in string:
        # calculate encoded char
        if 'a' <= char <= 'z':
            encoded_string += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            encoded_string += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            encoded_string += char  # if char isn't eng symbol

    return encoded_string


string_to_encode = input('Enter sting to encode/decode (ROT13): ')
encoded_string = encode_string(string_to_encode)

print('Encoded/decoded string: {}'.format(encoded_string))
