#!/usr/bin/env python3
"""Verify Flask app and Vercel deployment setup"""

import sys
import os

def test_app_import():
    """Test that we can import the Flask app"""
    try:
        from app import app, application
        print("✅ Successfully imported Flask app from app.py")
        print(f"✅ App name: {app.name}")
        print(f"✅ Application object: {type(application)}")
        return True
    except Exception as e:
        print(f"❌ Failed to import Flask app from app.py: {e}")
        return False

def test_api_import():
    """Test that we can import the API entry point"""
    try:
        from api.index import application
        print("✅ Successfully imported API entry point from api/index.py")
        print(f"✅ Application object: {type(application)}")
        return True
    except Exception as e:
        print(f"❌ Failed to import API entry point from api/index.py: {e}")
        return False

def check_files():
    """Check that required files exist"""
    required_files = ['app.py', 'api/index.py', 'vercel.json', 'requirements.txt']
    missing_files = []
    
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing files: {missing_files}")
        return False
    else:
        print("✅ All required files exist")
        return True

def check_vercel_config():
    """Check vercel.json configuration"""
    try:
        import json
        with open('vercel.json', 'r') as f:
            config = json.load(f)
        
        if config.get('builds') and len(config['builds']) > 0:
            build = config['builds'][0]
            if build.get('src') == 'api/index.py' and build.get('use') == '@vercel/python':
                print("✅ Vercel configuration is correct")
                return True
            else:
                print(f"❌ Vercel configuration incorrect: {build}")
                return False
        else:
            print("❌ Vercel configuration missing builds section")
            return False
    except Exception as e:
        print(f"❌ Failed to check Vercel configuration: {e}")
        return False

if __name__ == "__main__":
    print("Verifying Flask app and Vercel deployment setup...")
    print("=" * 50)
    
    # Change to the flask-app directory if not already there
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    checks = [
        ("File existence", check_files),
        ("Vercel configuration", check_vercel_config),
        ("App import", test_app_import),
        ("API import", test_api_import)
    ]
    
    results = []
    for check_name, check_func in checks:
        print(f"\n{check_name}:")
        result = check_func()
        results.append(result)
    
    print("\n" + "=" * 50)
    if all(results):
        print("✅ All checks passed! Ready for Vercel deployment.")
    else:
        print("❌ Some checks failed. Please review the errors above.")
        
    print(f"Results: {sum(results)}/{len(results)} checks passed")