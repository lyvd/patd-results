import os
import time
import requests
import json
import sys
# Define your VirusTotal API key
API_KEY = '9542385c2c440a0e561aa5c1e4ac5b84307428589d854a969d52ab2dacff5e27'

import sys
# Directories for input (samples) and output (scan results)
INPUT_DIR = sys.argv[1] 
OUTPUT_DIR = sys.argv[2] 

# VirusTotal API endpoints
FILE_SCAN_URL = 'https://www.virustotal.com/vtapi/v2/file/scan'
REPORT_URL = 'https://www.virustotal.com/vtapi/v2/file/report'

# Function to submit a file for scanning
def submit_file_to_virustotal(file_path):
    with open(file_path, 'rb') as file:
        params = {'apikey': API_KEY}
        files = {'file': (os.path.basename(file_path), file)}
        response = requests.post(FILE_SCAN_URL, files=files, params=params)
        return response.json()

# Function to get scan results from VirusTotal
def get_scan_report(resource):
    params = {'apikey': API_KEY, 'resource': resource}
    response = requests.get(REPORT_URL, params=params)
    return response.json()

# Function to save the scan report to a file
def save_report_to_file(report, output_path):
    with open(output_path, 'w') as file:
        json.dump(report, file, indent=4)

# Main function to scan all files in the directory
def scan_samples_in_directory(input_dir, output_dir):
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)
        output_file_path = os.path.join(output_dir, f"{file_name}_report.json")
        
        if not os.path.exists(output_file_path):
            if os.path.isfile(file_path):  # Only process files
                print(f"Submitting {file_name} to VirusTotal...")
                response = submit_file_to_virustotal(file_path)
                
                if 'scan_id' in response:
                    scan_id = response['scan_id']
                    print(f"File {file_name} submitted, waiting for scan results...")

                    # Sleep to allow VirusTotal to process the file (VirusTotal may need some time)
                    time.sleep(25)

                    # Fetch scan report
                    report = get_scan_report(scan_id)

                    # Save the report
                    save_report_to_file(report, output_file_path)
                    print(f"Scan results saved to {output_file_path}")
                else:
                    print(f"Error submitting {file_name} to VirusTotal: {response}")
                    continue

# Run the script
if __name__ == '__main__':
    scan_samples_in_directory(INPUT_DIR, OUTPUT_DIR)

