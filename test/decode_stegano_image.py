import numpy as np
from PIL import Image

def decode_stegano_image(image_filename):
    """Extrahiert versteckte Daten aus einem Bild"""
    img = Image.open(image_filename)
    img_data = np.array(img)
    
    binary_message = ""
    for row in img_data:
        for pixel in row:
            for col in range(3):  # RGB-Kanäle
                binary_message += bin(pixel[col])[-1]  # LSB auslesen
    
    # Finde das Ende der Nachricht (EOF-Marker '1111111111111110')
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if byte == '1111111111111110':
            break
        message += chr(int(byte, 2))
    
    return message

# Anwendung
image_filename = "stegano_image.png"
extracted_message = decode_stegano_image(image_filename)
print(f"Extrahierte Nachricht: {extracted_message}")