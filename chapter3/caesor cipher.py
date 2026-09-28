import string

# Source alphabet (A–Z)
src_str = string.ascii_uppercase

# Destination alphabet shifted by 3
dst_str = src_str[3:] + src_str[:3]

def cipher(a):
    idx = src_str.index(a)
    return dst_str[idx]

# Input from user
src = input("Enter the sentence: ")

print("Encrypted text:", end=" ")
for ch in src:
    if ch.upper() in src_str:   # check if it's a letter
        enc = cipher(ch.upper())
        # Preserve case
        print(enc if ch.isupper() else enc.lower(), end="")
    else:
        print(ch, end="")
print()
