#!/usr/bin/env python3

def main():
    #print(extract_strings_from_image('encoded_image.png'))
    #decode_stepic()
    #decode_bade64()
    #decode_encoding()
    #decode_stegano()
   print(decode_end_binary_hex())

def decode_end_binary_hex():
    data = decode_reader()

    for binary_data in data:
        print("---------------")
        print(binary_data[0])
        continue
        hex_data = binary_data.hex()
        print("Hexadecimal data:", hex_data)

        # Try interpreting the data as text in different encodings
        for encoding in ['utf-8', 'latin-1', 'utf-16', 'utf-32']:
            try:
                text_data = binary_data.decode(encoding)
                print(f"Decoded with {encoding}:", text_data)
            except UnicodeDecodeError as e:
                print(f"Decoding error with {encoding}:", e)


def decode_end_binary_zlib():
    data = decode_reader()

    for _, binary_data in data:
        binary_data = b'\x9e\xe7\x0by\x9e\x9b\x83A\x1fA\xe0#...'

        # Attempt to decompress the data using zlib
        try:
            decompressed_data = zlib.decompress(binary_data)
            print("Decompressed data:", decompressed_data)
        except zlib.error as e:
            print("Zlib decompression error:", e)

        # Try interpreting the data as text in different encodings
        for encoding in ['utf-8', 'latin-1', 'utf-16']:
            try:
                text_data = binary_data.decode(encoding)
                print(f"Decoded with {encoding}:", text_data)
            except UnicodeDecodeError as e:
                print(f"Decoding error with {encoding}:", e)

def decode_reader():
    import png

    # Replace 'path_to_image.png' with the actual path to your image
    r = png.Reader('encoded_image.png')
    output = []
    for chunk in r.chunks():
        output.append((chunk[0], chunk[1]))
    return output

def decode_stegano():
    from stegano import lsb

    # Replace 'path_to_image.png' with the actual path to your image
    hidden_message = lsb.reveal('path_to_image.png')
    print('Hidden message:', hidden_message)


def extract_strings_from_image(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
    # Filter out non-printable characters and return only the printable string portions
    return ''.join(c if 31 < ord(c) < 127 else '\n' for c in content.decode('latin-1'))


def decode_stepic():
    from PIL import Image
    import stepic

    file_path = 'encoded_image.png'  # replace with your image file path
    img = Image.open(file_path)

    # Decode the hidden message
    hidden_message = stepic.decode(img)
    print('Hidden message: %s' % hidden_message)

def decode_bade64():
    import base64

    # This is assuming 'tÐ' is part of a base64-encoded string. 
    # Since base64 strings are typically longer, this might be just a portion of it.
    encoded_data = 'tÐ'  # Replace this with the actual string if it's longer

    # We need to ensure the encoded data is the correct length for base64 decoding
    # Base64 strings should be a multiple of 4 in length
    padding = '=' * ((4 - len(encoded_data) % 4) % 4)
    encoded_data += padding

    try:
        # Attempt to decode the data
        decoded_data = base64.b64decode(encoded_data)
        print('Decoded message:', decoded_data)
    except base64.binascii.Error as e:
        print('Decoding error:', e)

def decode_encoding():
    data = 'tÐ'.encode('latin1')  # Ensure encoding is set to handle non-ASCII characters

    # Display the hexadecimal representation of the data
    print('Hexadecimal:', data.hex())

    # Attempt to print the data in different encodings
    for encoding in ['latin1', 'utf-8', 'utf-16', 'utf-32']:
        try:
            print(f'Decoded with {encoding}:', data.decode(encoding))
        except UnicodeDecodeError as e:
            print(f'Could not decode with {encoding}:', e)

if __name__ == "__main__":
    main()
