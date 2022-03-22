import os


class Config:
    TRELLO_API_KEY = os.environ.get("TRELLO_API_KEY")
    TRELLO_API_SECRET = os.environ.get("TRELLO_API_SECRET")
    TRELLO_BOARD_ID = os.environ.get("TRELLO_BOARD_ID")
    TRELLO_TOKEN = os.environ.get("TRELLO_TOKEN")
    TRELLO_USERNAME = os.environ.get("TRELLO_USERNAME")

    def __init__(self):
        """Base configuration variables."""
        self.SECRET_KEY = os.environ.get("TRELLO_API_SECRET")
        if not self.SECRET_KEY:
            raise ValueError("No SECRET_KEY set for Flask application. Did you follow the setup instructions?")

