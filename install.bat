@echo off
REM AI Friday Assistant - Installation Script for Windows
REM Quick setup for the AI Friday Assistant

echo.
echo 🚀 Installing AI Friday Assistant...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.7 or higher.
    pause
    exit /b 1
)

echo ✅ Python found
echo.

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv
call venv\Scripts\activate.bat

echo ✅ Virtual environment created
echo.

REM Install dependencies
echo 📥 Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

echo ✅ Dependencies installed
echo.

REM Create data directories
echo 📁 Creating data directories...
if not exist data mkdir data
if not exist logs mkdir logs

echo ✅ Directories created
echo.

echo 🎉 Installation complete!
echo.
echo To activate the virtual environment, run:
echo   venv\Scripts\activate.bat
echo.
echo To run the AI Friday Assistant, use:
echo   python main.py
echo.
echo To run the voice demo, use:
echo   python voice_demo.py
echo.
echo Happy Friday! 🤖
echo.
pause
