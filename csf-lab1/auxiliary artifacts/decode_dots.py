def dots_to_bits(dot_string):
    # Convert dots and spaces to binary string
    binary_string = dot_string.replace('.', '1').replace(' ', '0')
    return binary_string

def binary_to_string(binary_string):
    # Split the binary string into 8-bit chunks and convert to characters
    chars = []
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        if len(byte) == 8:  # Ensure it's a complete byte
            chars.append(chr(int(byte, 2)))  # Convert binary to integer, then to character
    return ''.join(chars)

def process_file(file_path):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        input_string = file.read()

    # Step 1: Convert dots and spaces to binary
    binary_result = dots_to_bits(input_string)

    # Step 2: Convert binary to string
    final_string = binary_to_string(binary_result)

    return binary_result, final_string


# Example usage:
file_path = 'cartwheel_dots.txt'  # Specify your file path here

# Process the file and get the results
binary_output, text_output = process_file(file_path)

print(f"Binary: {binary_output}")
print(f"String: {text_output}")

with open("decode_dots_output.txt", 'w') as output_file:
    output_file.write(text_output)

with open("decode_dots_binary_output.txt", 'w') as output_file:
    output_file.write(binary_output)
