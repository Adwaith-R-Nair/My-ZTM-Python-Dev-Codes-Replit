
import subprocess
import sys
import os

def run_script(script_name):
    try:
        subprocess.run([sys.executable, f"PythonBasics1/{script_name}"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")
    except FileNotFoundError:
        print(f"File {script_name} not found!")

def get_python_files():
    """Get all Python files in the PythonBasics1 folder except main.py"""
    python_files = []
    for file in os.listdir("PythonBasics1"):
        if file.endswith(".py") and file != "main.py":
            python_files.append(file)
    return sorted(python_files)

def main():
    python_files = get_python_files()
    
    if not python_files:
        print("No Python files found in PythonBasics1 folder!")
        return
    
    print("Choose a script to run:")
    for i, file in enumerate(python_files, 1):
        print(f"{i}. {file}")
    
    try:
        choice = int(input(f"Enter your choice (1-{len(python_files)}): "))
        if 1 <= choice <= len(python_files):
            run_script(python_files[choice - 1])
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please enter a valid number!")

if __name__ == "__main__":
    main()
