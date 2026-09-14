#!/usr/bin/env python3
"""
AI Friday Assistant - Main Application
Entry point for the AI Friday Assistant
"""

import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from demo import AIFridayAssistant, main

if __name__ == "__main__":
    main()
