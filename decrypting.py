try:
    # Choose mode
    mode = input("Type  'D' to Decrypt: ").upper()
    if mode not in [ 'D']:
        raise ValueError("Invalid mode. Use  'D'.")

    # Take image path and key
    path = input(r'Enter path of Image: ')
    key = int(input('Enter Key (number): '))

    print(f"{'Decrypting'} file: {path}")
    print('Using Key:', key)

    # Read image
    with open(path, 'rb') as f:
        image = bytearray(f.read())

    # XOR each byte with the key
    for index in range(len(image)):
        image[index] ^= key

    # Write back the file
    with open(path, 'wb') as f:
        f.write(image)

    print(f"{ 'Decryption'} Done!")

except ValueError as ve:
    print("Value Error:", str(ve))
except FileNotFoundError:
    print("File not found. Please check the path.")
except Exception as e:
    print("An error occurred:", str(e))
    