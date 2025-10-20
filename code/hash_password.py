# Hashing passwords for secure storage

import bcrypt


def hash_password(password):
    """Hash a password for storing."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed


def check_password(password, hashed):
    """Check a hashed password."""
    return bcrypt.checkpw(password.encode("utf-8"), hashed)


# Example usage
if __name__ == "__main__":
    password = "my_secure_password"
    hashed = hash_password(password)
    print(f"Hashed password: {hashed}")

    # Verify the password
    is_correct = check_password("my_secure_password", hashed)
    print(f"Password is correct: {is_correct}")
