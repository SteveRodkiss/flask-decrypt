def xor_encrypt(input_string):
    #function to return the encrypted string using the xor method of encryption
    new_text = ""
    for letter in input_string:
        new_text += chr(ord(letter)^ 27)
    return new_text


def xor_decrypt(input_string):
    #function to decrypt text using the XOR method.
    new_text = ""
    for letter in input_string:
        new_text += chr(ord(letter)^27)
    return new_text