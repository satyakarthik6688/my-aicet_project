# Image Steganography with Python

This project provides a simple implementation of image steganography using Python and OpenCV. It allows users to hide a secret message inside an image and retrieve it using a passcode.

## Features
- Encrypt a message into an image.
- Decrypt the hidden message using the correct passcode.
- Uses OpenCV for image processing.

## Requirements
Ensure you have Python installed along with the following dependencies:

```sh
pip install opencv-python
```

## How to Use

### **1. Encrypt a Message**
1. Place your image (e.g., `mypic.jpg`) in the project directory.
2. Run the encryption script:
   ```sh
   python encrypt.py
   ```
3. Enter the secret message and a passcode when prompted.
4. The encrypted image (`encryptedImage.jpg`) will be generated.

### **2. Decrypt a Message**
1. Run the decryption script:
   ```sh
   python decrypt.py
   ```
2. Enter the correct passcode to reveal the hidden message.

## File Structure
```
|-- encrypt.py       # Script to hide a message in an image
|-- decrypt.py       # Script to extract the hidden message
|-- mypic.jpg        # Input image file
|-- encryptedImage.jpg  # Image containing the encrypted message
|-- password.txt     # Stores the encryption passcode
```

## Notes
- Ensure the input image (`mypic.jpg`) is present in the project directory before running the encryption script.
- The decryption process will only work if the correct passcode is entered.
