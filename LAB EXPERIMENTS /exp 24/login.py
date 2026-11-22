def login(username: str, password: str) -> bool:
    """Demo-only login check. Replace with secure hashed-password auth in production."""
    return username == "student" and password == "lab123"

if __name__ == "__main__":
    print("Login successful" if login("student", "lab123") else "Login failed")
