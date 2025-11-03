#!/usr/bin/env python3
"""Simple test script"""

import os

def detect_project_type():
    """Simple project detection"""
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    print(f"Files in directory: {files}")
    
    if "package.json" in files:
        print("Found package.json")
        return "node"
    elif "requirements.txt" in files:
        print("Found requirements.txt")
        return "python-flask"
    elif "index.html" in files:
        print("Found index.html")
        return "static"
    else:
        print("Unknown project type")
        return "unknown"

if __name__ == "__main__":
    print("Running simple test...")
    project_type = detect_project_type()
    print(f"Detected project type: {project_type}")