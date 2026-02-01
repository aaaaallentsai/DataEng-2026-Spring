#!/usr/bin/env python3
"""
Simple Demo Web App - For Container Lab
A minimal Flask app to demonstrate containerization concepts
"""

from flask import Flask, jsonify
import os
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    """Main endpoint - shows container is working"""
    return jsonify({
        "message": "🎉 Container is running!",
        "timestamp": datetime.now().isoformat(),
        "hostname": socket.gethostname(),
        "container_tip": "You're seeing this from inside a Docker container!"
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "uptime": "running"
    })

@app.route('/data')
def data():
    """Sample data endpoint"""
    return jsonify({
        "students": ["Alice", "Bob", "Charlie"],
        "course": "DS551",
        "topic": "Containerization"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    print(f"🚀 Starting Flask app on port {port}...")
    print(f"📍 Access at: http://localhost:{port}/")
    app.run(host='0.0.0.0', port=port, debug=True)
