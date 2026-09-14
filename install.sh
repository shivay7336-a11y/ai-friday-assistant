#!/bin/bash
# AI Friday Assistant - Installation Script
# Quick setup for the AI Friday Assistant

echo "🚀 Installing AI Friday Assistant..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.7 or higher."
    exit 1
fi

echo "✅ Python 3 found"
echo ""

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "✅ Virtual environment created"
echo ""

# Install dependencies
echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Dependencies installed"
echo ""

# Create data directories
echo "📁 Creating data directories..."
mkdir -p data logs

echo "✅ Directories created"
echo ""

echo "🎉 Installation complete!"
echo ""
echo "To activate the virtual environment, run:"
echo "  source venv/bin/activate"
echo ""
echo "To run the AI Friday Assistant, use:"
echo "  python main.py"
echo ""
echo "To run the voice demo, use:"
echo "  python voice_demo.py"
echo ""
echo "Happy Friday! 🤖"
