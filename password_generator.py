import random
import string

# characters to choose from
chars = string.ascii_letters + string.digits + "!@#$%"

# pick 12 random characters
password = "".join(random.choice(chars) for _ in range(12))

print("generated password:", password)
