import hashlib
import zipfile
import os

# File path for the seed
SEED_PATH = "seed.txt"


# Function to read the password from the file
def create_seed_with_pass(password):
    seed = f"1\t{password}"  # Read and strip any extra spaces or newlines
    return int(seed[0]), seed[1].strip()  # Return the seed and password


# Function to generate the next seed from the password
def generate_seed(seed):
    # Convert the password to bytes and hash it using SHA-256
    sha256_hash = hashlib.sha256(seed.encode("utf-8")).hexdigest()
    print(f"SHA-256 hash of the password: {sha256_hash}")
    # next seed

    return sha256_hash
    # return next_seed


def open_wordlist():
    with open("wordlist.txt", "r", encoding="utf-8") as f:
        return f.read().splitlines()


def create_password(seed, ts):
    combined = seed + ts
    password = hashlib.sha256(combined.encode("utf-8")).hexdigest()
    return password


# Main function that runs the script
def main():

    seed = "TheBiteOf87"

    for i in range(78):
        # Generate the next seed based on the password
        seed = generate_seed(seed)
        print(f"Next seed generated: {i, seed}")

        # unzip the backup files with the seed
        zip_ts = [
            "1727365201",
            "1727365801",
            "1727366402",
            "1727367001",
            "1727367601",
            "1727368201",
            "1727368801",
        ]

        for ts in zip_ts:
            extract_folder = f"backup_{ts}"

            # Create the extraction folder if it doesn't exist
            if not os.path.exists(extract_folder):
                os.makedirs(extract_folder)

            try:
                password = create_password(seed, ts)
                with zipfile.ZipFile(f"backup_{ts}.zip", "r") as zip_ref:
                    zip_ref.extractall(path=extract_folder, pwd=bytes(password, "utf-8"))
                    print(f"{f"backup_{ts}.zip"} successfully unzipped with seed gen {i}.")
            except Exception:
                continue


# Entry point of the script
if __name__ == "__main__":
    main()
