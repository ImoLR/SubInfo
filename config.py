import os

class Config:
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8080))
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# Subscription cache (seconds)
CACHE_TIME = 300

# Log level
LOG_LEVEL = "INFO"

# Project version
VERSION = "0.1.0"
