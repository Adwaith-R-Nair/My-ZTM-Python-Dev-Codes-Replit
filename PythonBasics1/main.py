
import subprocess
import sys

def run_script(script_name):
    try:
        subprocess.run([sys.executable, f"PythonBasics1/{script_name}"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")
    except FileNotFoundError:
        print(f"File {script_name} not found!")

def main():
    print("Choose a script to run:")
    print("1. name.py")
    print("2. datatypes.py")
    
    choice = input("Enter your choice (1-2): ")
    
    if choice == "1":
        run_script("name.py")
    elif choice == "2":
        run_script("datatypes.py")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
