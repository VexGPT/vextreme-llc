import os
import sys
import subprocess

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    packages = ['flask', 'requests', 'python-dotenv']
    for package in packages:
        install_package(package)
    print("Packages installed successfully.")

if __name__ == '__main__':
    main()