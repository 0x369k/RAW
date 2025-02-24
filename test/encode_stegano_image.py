import numpy as np
from PIL import Image

# Parameter für das Test-Bild
image_filename = "stegano_image.png"
image_width = 800  # Moderate Größe für genügend Speicherplatz
image_height = 600

# Maximale Zeichenanzahl basierend auf LSB-Steganographie
max_characters = (image_width * image_height * 3) // 8  # Jeder Pixel hat 3 Kanäle, 8 Bit pro Zeichen

# Dummy-Textdaten generieren (maximale Kapazität nutzen)
hidden_text = "Steganographie-Testbild! " * (max_characters // 30)
hidden_text = hidden_text[:max_characters]  # Kürzen auf die maximale Kapazität

# Text in Binärformat umwandeln
binary_message = ''.join(format(ord(c), '08b') for c in hidden_text) + '1111111111111110'  # EOF-Marker

# Zufälliges Farbbild generieren
img_data = np.random.randint(0, 256, (image_height, image_width, 3), dtype=np.uint8)

# Text in LSB der Pixel verstecken
data_idx = 0
for row in img_data:
    for pixel in row:
        for col in range(3):  # RGB-Kanäle
            if data_idx < len(binary_message):
                pixel[col] = int(bin(pixel[col])[2:-1] + binary_message[data_idx], 2)  # LSB setzen
                data_idx += 1

# Bild speichern
image = Image.fromarray(img_data)
image.save(image_filename)

print(f"Bild mit versteckter Nachricht gespeichert: {image_filename}")