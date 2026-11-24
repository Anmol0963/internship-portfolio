import sys
import platform

def main():
    print("Hello, World! Internship development environment is ready.")
    print(f"Python Version: {sys.version.split()[0]}")
    print(f"Operating System: {platform.system()} {platform.release()}")

if __name__ == "__main__":
    main()
