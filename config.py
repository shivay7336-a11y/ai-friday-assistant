"""
AI Friday Assistant - Configuration
Central configuration for the application
"""

import os
from datetime import datetime

# App Info
APP_NAME = "AI Friday Assistant"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "An AI-powered Friday assistant for task management and automation"

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

# Ensure directories exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)

# Task Configuration
TASK_PRIORITIES = ["low", "medium", "high"]
DEFAULT_PRIORITY = "medium"

# Time Configuration
WEEK_START = "Monday"
TIMEZONE = "UTC"

# Features
FEATURES = {
    "task_management": True,
    "weekly_summaries": True,
    "priority_filtering": True,
    "automated_reminders": True,
    "email_notifications": False,
}

# Logging Configuration
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

def get_config():
    """Get all configuration as a dictionary"""
    return {
        "app_name": APP_NAME,
        "version": APP_VERSION,
        "description": APP_DESCRIPTION,
        "base_dir": BASE_DIR,
        "data_dir": DATA_DIR,
        "logs_dir": LOGS_DIR,
        "task_priorities": TASK_PRIORITIES,
        "features": FEATURES,
    }
