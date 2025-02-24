import cv2
import os

# Read the image (use PNG format)
img = cv2.imread("mypic.png")

# Take user inputs
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Append a special character (~) to mark the end of the message
msg += "~"

# Encoding dictionary
d = {chr(i): i for i in range(256)}

n, m, z = 0, 0, 0

# Encode the message into the image
for char in msg:
    img[n, m, z] = d[char]  # Store ASCII value
    z = (z + 1) % 3  # Cycle through RGB channels
    if z == 0:
        m += 1
    if m >= img.shape[1]:  # Move to next row if needed
        m = 0
        n += 1

# Save encrypted image
cv2.imwrite("encryptedImage.png", img)  # Save as PNG to avoid compression
print("Message encrypted and saved as 'encryptedImage.png'.")

# Open the encrypted image (Windows only)
os.system("start encryptedImage.png")
