import pikepdf
from tqdm import tqdm

# load password list

passwords = [ line.strip() for line in open( "enter your path") ]
# iterate over passwords
for password in tqdm(passwords, "Decrypting PDF"):
    try:
        # open PDF file
        with pikepdf.open( "enter PDF path", password=password) as pdf:
            # Password decrypted successfully, break out of the loop
            print("[+] Password found:", password)
            break
    except pikepdf._core.PasswordError as e:
        # wrong password, just continue in the loop
        continue