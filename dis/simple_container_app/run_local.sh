#!/bin/bash
# Quick demo script - Run this to test the app locally

echo "🚀 Setting up demo environment..."

# Create venv if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate venv
source venv/bin/activate

# Install requirements
echo "📥 Installing dependencies..."
pip install -q -r requirements.txt

# Run the app
echo ""
echo "✅ Starting Flask app..."
echo "📍 Open http://localhost:5000/ in your browser"
echo "⌨️  Press Ctrl+C to stop"
echo ""
python app.py
