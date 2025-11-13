import os
import json
from hashlib import sha256

USER_DB_PATH = os.path.join("cloudconnect", "data", "users.json")
os.makedirs(os.path.dirname(USER_DB_PATH), exist_ok=True)

class UserManager:
    """Handles user signup and login functionality."""
    
    def __init__(self):
        self._load_users()
        self._current_user = None

    def _load_users(self):
        """Load users from the database file."""
        if os.path.exists(USER_DB_PATH):
            with open(USER_DB_PATH, "r", encoding="utf-8") as f:
                self._users = json.load(f)
        else:
            self._users = {}

    def _save_users(self):
        """Save users to the database file."""
        with open(USER_DB_PATH, "w", encoding="utf-8") as f:
            json.dump(self._users, f, indent=4)

    def signup(self, username, name, email, password):
        """Register a new user."""
        if username in self._users:
            raise ValueError("User already exists. Please login.")
        self._users[username] = {
            "name": name,
            "email": email,
            "password": sha256(password.encode()).hexdigest()
        }
        self._save_users()
        return f"User '{username}' signed up successfully."

    def login(self, username, password):
        """Authenticate an existing user."""
        user = self._users.get(username)
        if not user or user["password"] != sha256(password.encode()).hexdigest():
            raise ValueError("Invalid username or password.")
        self._current_user = username
        return f"User '{username}' logged in successfully."

    def logout(self):
        """Log out the current user."""
        if not self._current_user:
            raise ValueError("No user is currently logged in.")
        self._current_user = None
        return "Logged out successfully."

    def get_current_user(self):
        """Get the currently logged-in user."""
        return self._current_user
