import os
import sys
import pandas as pd
import subprocess
import shutil

# Function to clone a GitHub repository into a specified directory
def clone_repo(package_name, repo_url, base_dir):
    package_dir = os.path.join(base_dir, package_name)
    
    # Check if directory already exists
    if not os.path.exists(package_dir):
        os.makedirs(package_dir)
        print(f"Cloning {package_name} from {repo_url} into {package_dir}")
        
        try:
            # Run the git clone command with a timeout of 1 minute
            subprocess.run(['git', 'clone', repo_url, package_dir], timeout=60, check=True)
            return True
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError):
            print(f"Cloning {package_name} from {repo_url} failed or timed out. Deleting directory and moving to the next.")
            shutil.rmtree(package_dir)
            return False
    else:
        print(f"Directory {package_name} already exists, skipping...")
        return False

# Function to zip the directory and remove the cloned repository
def zip_and_delete(package_name, base_dir):
    package_dir = os.path.join(base_dir, package_name)
    zip_file = os.path.join(base_dir, f"{package_name}.zip")
    
    # Zip the directory
    print(f"Zipping directory {package_name}...")
    shutil.make_archive(package_dir, 'zip', package_dir)
    
    # Delete the directory after zipping
    print(f"Deleting directory {package_name}...")
    shutil.rmtree(package_dir)

# Main function to parse CSV and clone repositories, zip them, and delete the original directories
def main(csv_file, base_dir):
    # Read CSV into a pandas dataframe
    df = pd.read_csv(csv_file)
    
    # Iterate through each row, assuming first column is package name and last column is GitHub URL
    for index, row in df.iterrows():
        package_name = row[0]  # First column: package name
        repo_url = row[-1]     # Last column: GitHub URL
        
        if pd.notna(repo_url) and repo_url.strip():
            if clone_repo(package_name, repo_url, base_dir):
                # Zip the directory and delete it only if cloning was successful
                zip_and_delete(package_name, base_dir)

if __name__ == '__main__':
    # CSV file containing package names and GitHub URLs
    csv_file = sys.argv[1] 
    
    # Base directory to store the cloned repositories
    base_dir = sys.argv[2]
    
    # Make sure the base directory exists
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    
    # Parse CSV and clone repositories, zip them, and remove directories
    main(csv_file, base_dir)