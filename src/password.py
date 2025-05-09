import os
import hashlib
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Get the hash secret from the .env file
HASH_SECRET = os.getenv("HASH_SECRET")

if not HASH_SECRET:
    raise ValueError("HASH_SECRET is not defined in the .env file")

def hash_password(password: str) -> str:
    """Hash a password using the secret key."""
    salted_password = f"{password}{HASH_SECRET}"
    return hashlib.sha256(salted_password.encode()).hexdigest()

# Example usage
if __name__ == "__main__":
    password = "my_secure_password"
    hashed = hash_password(password)
    print(f"Hashed password: {hashed}")