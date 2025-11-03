#!/usr/bin/env python3
"""Manual deployment script"""

import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from core.file_manager import create_required_files
from core.git_handler import init_git_repo
from core.builder import build_project
from core.deployer import deploy_to_platform_flask

def manual_deploy():
    """Manual deployment process"""
    print("Starting manual deployment...")
    
    # Project type is known
    project_type = "python-flask"
    platform = "Render"  # Default for Flask
    
    print(f"Project type: {project_type}")
    print(f"Target platform: {platform}")
    
    # Create required files
    print("\n1. Creating required files...")
    if not create_required_files(project_type, platform):
        print("Failed to create required files")
        return False
    
    # Initialize git repo
    print("\n2. Initializing Git repository...")
    if not init_git_repo():
        print("Failed to initialize Git repository")
        return False
    
    # Build project (not needed for Flask)
    print("\n3. Building project...")
    if not build_project(project_type):
        print("Failed to build project")
        return False
    
    # Deploy to platform
    print("\n4. Deploying to platform...")
    # Note: This will require manual steps for Render
    print(f"Deployment to {platform} requires manual steps:")
    print("1. Create an account at render.com")
    print("2. Connect your Git repository")
    print("3. Set environment to Python")
    print("4. Set build command to: pip install -r requirements.txt")
    print("5. Set start command to: gunicorn app:app")
    
    return True

if __name__ == "__main__":
    print("Manual Deployment Script")
    print("=" * 30)
    success = manual_deploy()
    if success:
        print("\nDeployment process completed!")
    else:
        print("\nDeployment process failed!")