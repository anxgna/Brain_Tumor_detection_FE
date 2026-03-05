import os

# Backend API Configuration
# Default to localhost if not specified in environment
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")
UPLOAD_ENDPOINT = f"{API_URL}/upload"
PREDICT_ENDPOINT_BASE = f"{API_URL}/predict"

# Application Settings
APP_TITLE = "🧠✨ Cute Brain Tumor Detector ✨🧠"
APP_DESCRIPTION = (
    "Welcome to the **Brain Tumor Detection System**! 💕\n\n"
    "Upload your MRI scan below, and our smart AI will help analyze it for you. "
    "Please wait a moment while we process the image! 🌸"
)

# UI Settings
THEME_PRIMARY_HUE = "pink"
THEME_SECONDARY_HUE = "rose"

# Error Messages
ERROR_BACKEND_OFFLINE = "Oops! 😥 The backend server seems to be offline. Please try again later! 🌸"
ERROR_INVALID_IMAGE = "Oh no! 😟 The image format is invalid. Please upload a valid MRI scan (JPG/PNG). 💖"
