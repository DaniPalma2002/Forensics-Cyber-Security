from PIL import Image

# Load the image to inspect its dimensions
image_path = "tagus.png"
img = Image.open(image_path)

# Get the size of the image
img_size = img.size
print(img_size)

import numpy as np

def get_image_bytes(image_path):
    """
    Load an image and return its pixel data as a numpy array.
    """
    img = Image.open(image_path)
    img = img.convert('RGB')  # Ensure it's in RGB mode
    return np.array(img), img.size

def extract_5lsb_until_eof(host_image_array, corner_width, corner_height):
    """
    Extract a hidden message using 5 LSB from each color channel, starting from the top-left corner
    and traversing diagonally from right to left until an EOF is found.
    """
    host_rows, host_cols, _ = host_image_array.shape
    data_bits = []  # To store bits for each channel (R, G, B)
    
    # Traverse diagonally from right to left in the defined corner
    for diag in range(corner_width + corner_height - 1):
        for i in range(min(diag + 1, corner_height)):  # Limit i to the corner height
            j = diag - i
            if 0 <= j < corner_width:
                pixel = host_image_array[i, j]
                for color in range(3):  # Iterate over R, G, B channels
                    # Extract the 5 LSB of each color channel
                    data_bits.append(pixel[color] & 0b11111)

    # Now we have the data bits, stop when an EOF marker (e.g., 40 zero bits) is found
    bit_sequence = ''.join([bin(val)[2:].zfill(5) for val in data_bits])
    
    # Define EOF marker
    eof_marker = '1001001010001010100111001000100'
    eof_index = bit_sequence.find(eof_marker)

    # if eof_index != -1:
    #     bit_sequence = bit_sequence[:eof_index]  # Stop at EOF

    return bit_sequence

# Load the image and limit the region to the left corner (e.g., half the width and height)
host_image_array, _ = get_image_bytes(image_path)

corner_width = img_size[0]  # Use half the width for the corner
corner_height = img_size[1]  # Use half the height for the corner

# Extract the 5 LSBs until EOF
extracted_bits = extract_5lsb_until_eof(host_image_array, corner_width, corner_height)
print(len(extracted_bits), extracted_bits[:100])  # Show the length of extracted bits and first 100 bits

with open("tagus_output.txt", 'w') as output_file:
    output_file.write(extracted_bits)

