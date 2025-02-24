import cv2

# Read the encrypted image
img = cv2.imread("encryptedImage.png")

# Take user input for password
pas = input("Enter passcode for decryption: ")
original_password = input("Enter the original passcode used during encryption: ")

# Decoding dictionary
c = {i: chr(i) for i in range(256)}

n, m, z = 0, 0, 0
message = ""

# Verify password
if pas == original_password:
    while True:
        char = c[img[n, m, z]]  # Retrieve ASCII character
        if char == "~":  # Stop at end marker
            break
        message += char
        z = (z + 1) % 3
        if z == 0:
            m += 1
        if m >= img.shape[1]:  # Move to next row if needed
            m = 0
            n += 1

    print("Decrypted message:", message)
else:
    print("YOU ARE NOT AUTHORIZED")
