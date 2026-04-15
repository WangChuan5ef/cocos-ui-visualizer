#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cocos UI Visualizer - One-Click Installer
Automatic installation script for setting up the Cocos UI Visualizer
"""

import sys
import subprocess
import platform
from pathlib import Path


def print_header(text):
    """Print a formatted header"""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60)


def print_success(text):
    """Print success message"""
    print(f"✓ {text}")


def print_error(text):
    """Print error message"""
    print(f"✗ {text}")


def check_python_version():
    """Check if Python version is compatible"""
    print_header("Checking Python Version")
    
    version = sys.version_info
    version_str = f"{version.major}.{version.minor}.{version.micro}"
    
    print(f"Current Python version: {version_str}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print_error(f"Python 3.8+ is required, but you have {version_str}")
        return False
    
    print_success(f"Python {version_str} is compatible")
    return True


def check_os():
    """Check operating system"""
    print_header("Checking Operating System")
    
    system = platform.system()
    print(f"Current OS: {system}")
    
    if system not in ["Windows", "Darwin", "Linux"]:
        print_error(f"Unsupported OS: {system}")
        return False
    
    if system == "Windows":
        print_success("Windows detected")
    elif system == "Darwin":
        print_success("macOS detected")
    else:
        print_success("Linux detected")
    
    return True


def install_dependencies():
    """Install required Python packages"""
    print_header("Installing Dependencies")
    
    requirements_file = Path(__file__).parent / "requirements.txt"
    
    if not requirements_file.exists():
        print_error(f"requirements.txt not found at {requirements_file}")
        return False
    
    print(f"Installing from: {requirements_file}")
    
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", str(requirements_file)
        ])
        print_success("All dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"Failed to install dependencies: {e}")
        return False


def create_ui_directory():
    """Create ui directory if it doesn't exist"""
    print_header("Setting Up Project Structure")
    
    ui_dir = Path(__file__).parent / "cocos" / "ui"
    
    try:
        ui_dir.mkdir(parents=True, exist_ok=True)
        print_success(f"UI directory ready at: {ui_dir}")
        print("  → Add your .csb/.json UI files here")
        return True
    except Exception as e:
        print_error(f"Failed to create UI directory: {e}")
        return False


def main():
    """Main installation flow"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "  Cocos UI Visualizer - One-Click Installer".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "=" * 58 + "╝")
    
    steps = [
        ("Python Version Check", check_python_version),
        ("Operating System Check", check_os),
        ("Dependency Installation", install_dependencies),
        ("Project Structure Setup", create_ui_directory),
    ]
    
    failed_steps = []
    
    for step_name, step_func in steps:
        try:
            if not step_func():
                failed_steps.append(step_name)
        except Exception as e:
            print_error(f"Unexpected error in {step_name}: {e}")
            failed_steps.append(step_name)
    
    # Summary
    print_header("Installation Summary")
    
    if failed_steps:
        print_error(f"Installation incomplete. {len(failed_steps)} step(s) failed:")
        for step in failed_steps:
            print(f"  - {step}")
        print("\nPlease fix the issues above and run the installer again.")
        return False
    else:
        print_success("Installation completed successfully!")
        print("\nNext steps:")
        print("  1. Add your Cocos UI files (.csb/.json) to the 'cocos/ui' folder")
        print("  2. Run the application:")
        print("     python cocos/cocos_gui.py")
        print("  3. Or run with a specific folder:")
        print("     python cocos/cocos_gui.py path/to/ui/folder")
        return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
