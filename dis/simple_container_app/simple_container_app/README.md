# Simple Container Demo App

A minimal Flask application for teaching Docker containerization concepts.

## What's This For?

This is a simple, single-container demo for your lab session. No databases, no compose - just one container running one app.

## Files

- `app.py` - Simple Flask web server with 3 endpoints
- `requirements.txt` - Just Flask
- `Containerfile.template` - Fill-in-the-blanks version for students
- `Containerfile` - Complete solution for TA reference

## How to Use in Your Lab

### Part 1: Show the App Running Locally (5 min)

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# In another terminal, test it
curl http://localhost:5000/
curl http://localhost:5000/data
```

### Part 2: Build the Container Together (15 min)

**Interactive approach - fill in blanks with students:**

1. Open `Containerfile.template`
2. Project it on screen
3. Ask students for each blank
4. Explain WHY each answer is correct
5. Save completed version

**Questions to ask students:**

```dockerfile
FROM _____  
# "What base image do we need?" 
# → python:3.12-slim

WORKDIR _____  
# "Where should we work inside the container?"
# → /app

COPY _____ /app/requirements.txt  
# "What file has our dependencies?"
# → requirements.txt

RUN pip install -r _____  
# "How do we install packages?"
# → requirements.txt

COPY _____ /app/  
# "What's our main file?"
# → app.py

EXPOSE _____  
# "What port does Flask use?"
# → 5000

CMD ["python", "_____"]  
# "How do we start the app?"
# → app.py
```

### Part 3: Build and Run (10 min)

```bash
# Build the image
docker build -t demo-app .

# Run the container
docker run -p 8080:5000 demo-app

# In another terminal, test
curl http://localhost:8080/
curl http://localhost:8080/data
open http://localhost:8080/
```

### Part 4: Explore the Container (5 min)

```bash
# List running containers
docker ps

# View logs
docker logs <container-id>

# Enter the container
docker exec -it <container-id> /bin/bash

# Inside container:
ls -la
cat app.py
exit

# Stop the container
docker stop <container-id>
```

## Teaching Points

### Port Mapping
```
-p 8080:5000
   ↑    ↑
   |    └─ Container internal port (Flask uses 5000)
   └────── Host external port (you access 8080)
```

### Why This Order?
```dockerfile
COPY requirements.txt   # Copy deps FIRST
RUN pip install         # Install packages
COPY app.py            # Copy code LAST
```

**Why?** Docker caches layers. If app.py changes, you don't reinstall packages!

### Accessing the App
- From host: `http://localhost:8080/`
- Inside container: `http://localhost:5000/`
- The `-p 8080:5000` maps host→container

## Endpoints in the Demo App

1. **/** - Main endpoint, shows container is running
2. **/health** - Health check (returns status)
3. **/data** - Sample JSON data

## Common Issues

### Port Already in Use
```bash
# Find what's using port 8080
lsof -i :8080

# Use different port
docker run -p 9090:5000 demo-app
```

### Container Won't Start
```bash
# Check logs
docker logs <container-id>

# Common: typo in app.py
# Fix it and rebuild
docker build -t demo-app .
```

## Lab Timeline (35 minutes total)

- **0-5 min:** Show app running locally
- **5-20 min:** Build Containerfile together (interactive)
- **20-30 min:** Build and run container, test endpoints
- **30-35 min:** Explore container (ps, logs, exec)

## Why Single Container?

This demo focuses on **containerization fundamentals**:
- How to create a container
- How port mapping works
- How to interact with containers
- Debugging and inspection

**NOT covered** (to keep it simple):
- Docker Compose
- Multi-container apps
- Databases
- Networks
- Volumes

Keep it simple - master one container first!
