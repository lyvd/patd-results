import os
import sys

def list_directories(path):
    # List all items in the specified path
    items = os.listdir(path)
    
    # Filter and return only directories
    directories = [(item, os.path.join(path, item)) for item in items if os.path.isdir(os.path.join(path, item))]
    return directories

# Example usage:
directory_path = sys.argv[1]  # Change to your desired directory
directories = list_directories(directory_path)
print("Directories:", directories)

for directory, path in directories:
    print(directory, path)
    dest_dir = os.path.join(sys.argv[2], directory)
    command = 'bandit -r {} -f json -o {}'.format(path, dest_dir)
    os.system(command)

