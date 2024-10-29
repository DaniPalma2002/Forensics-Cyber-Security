import re
import base64


def decode_base64_from_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    # Regular expression to find potential Base64 strings
    base64_pattern = re.compile(r"([A-Za-z0-9+/=]{20,})")
    base64_strings = base64_pattern.findall(content)

    decoded_strings = []
    for b64_string in base64_strings:
        try:
            decoded_data = base64.b64decode(b64_string).decode("utf-8")
            decoded_strings.append(decoded_data)
        except Exception as e:
            print(f"Failed to decode string: {b64_string}, Error: {e}")

    return decoded_strings


if __name__ == "__main__":
    file_path = "Inbox"
    decoded_strings = decode_base64_from_file(file_path)
    for decoded in decoded_strings:
        print(decoded)
    #save to file as utf8
    
    with open("decoded.txt", "w", encoding="utf-8") as file:
        for decoded in decoded_strings:
            file.write(decoded + "\n")
