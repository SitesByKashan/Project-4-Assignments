import hashlib

def hash_password(password: str) -> str:
    """Hashes a password using SHA256 and returns the hex digest."""
    return hashlib.sha256(password.encode()).hexdigest()

def login(email: str, password_to_check: str, stored_logins: dict) -> bool:
    """
    Checks if the hashed version of password_to_check matches the stored hashed password.
    Returns True if they match, otherwise False.
    """
    if email in stored_logins:
        return stored_logins[email] == hash_password(password_to_check)
    return False

stored_logins = {
    "user1@example.com": hash_password("securepassword123"),
    "user2@example.com": hash_password("mypassword"),
}

# Testing the login function
print(login("user1@example.com", "securepassword123", stored_logins))  
print(login("user2@example.com", "wrongpassword", stored_logins))  
print(login("nonexistent@example.com", "password", stored_logins))  
