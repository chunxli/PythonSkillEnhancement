import secrets
import string

# Generate a strong password
length = 32  # Recommended length for strong passwords
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(characters) for i in range(length))

print(password)
