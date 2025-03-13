import os
import sys
import subprocess
import time

def main():
    print("=" * 50)
    print("RAILWAY DEBUGGING SCRIPT")
    print("=" * 50)
    
    # Print Python info
    print(f"\nPython version: {sys.version}")
    print(f"Python executable: {sys.executable}")
    print(f"Python path: {sys.path}")
    
    # Print environment
    print("\nEnvironment variables:")
    for key, value in os.environ.items():
        print(f"  {key}={value}")
    
    # List directory contents
    print("\nCurrent directory: " + os.getcwd())
    print("\nFiles in current directory:")
    for item in os.listdir('.'):
        print(f"  {item}")
    
    # Check pip
    print("\nPip version:")
    subprocess.run([sys.executable, "-m", "pip", "--version"], check=False)
    
    # Try to install dash explicitly
    print("\nAttempting to install dash:")
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", "dash==2.9.3", "--verbose"], 
        capture_output=True, 
        text=True,
        check=False
    )
    print(f"Installation stdout: {result.stdout}")
    print(f"Installation stderr: {result.stderr}")
    
    # List installed packages
    print("\nInstalled packages:")
    subprocess.run([sys.executable, "-m", "pip", "list"], check=False)
    
    # Try to import dash
    print("\nAttempting to import dash:")
    try:
        import dash
        print(f"Success! Dash version: {dash.__version__}")
        print(f"Dash location: {dash.__file__}")
    except ImportError as e:
        print(f"Failed to import dash: {e}")
    
    print("\nDebugging complete")
    
if __name__ == "__main__":
    main()
