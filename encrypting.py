try:
    # take path of image as a input
    path = input(r'Enter path of Image : ')
     
    # using a specific fixed encryption key
    key = 73  
    print('The path of file : ', path)
    print('Using fixed key for encryption : ', key)
     
    # open file for reading purpose
    fin = open(path, 'rb')
    image = fin.read()
    fin.close()
     
    # convert image into byte array
    image = bytearray(image)
 
    # XOR encryption
    for index, values in enumerate(image):
        image[index] = values ^ key
 
    # write back the encrypted data
    fin = open(path, 'wb')
    fin.write(image)
    fin.close()
    
    print('✅ Encryption Done...')

except Exception as e:
    print('❌ Error caught : ', str(e))


