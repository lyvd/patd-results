import os
import json
import csv
from collections import Counter
import re

def parse_json_file(file_path, package_information):
    """
    Parses a JSON file to extract and count alerts for specific file types.
    Args:
        file_path (str): The path to the JSON file to be parsed.
        package_information (dict): A dictionary containing package information with keys 'dataset' and 'package'.
    Returns:
        list: A list of dictionaries, each containing:
            - 'dataset' (str): The dataset name from package_information.
            - 'package' (str): The package name from package_information.
            - 'file' (str): The file path of the alert.
            - 'number_of_alerts' (int): The count of alerts for the file.
    Raises:
        json.JSONDecodeError: If the JSON file cannot be decoded.
        IOError: If there is an error reading the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            results = []
            for run in data.get('runs', []):
                number_of_alert = Counter()
                for result in run.get('results', []):
                    for location in result.get('locations', []):
                        physical_location = location.get('physicalLocation', {})
                        file_path = physical_location.get('address', {}).get('fullyQualifiedName', 'Unknown')
                        # only get alerts for specific file types
                        if file_path.endswith(('.py', '.js', '.rb')):
                            number_of_alert[file_path] += 1
                    
                for file, count in number_of_alert.most_common():
                    results.append({
                        'dataset': package_information['dataset'],
                        'package': package_information['package'],
                        'file': file,
                        'number_of_alerts': count,
                    })
            
            return results
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error processing file {file_path}: {e}")
        return []

def save_results_to_csv(results, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Dataset', 'Package', 'File', 'Number of alerts']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for result in results:
            writer.writerow({
                'Dataset': result['dataset'],
                'Package': result['package'],
                'File': result['file'],
                'Number of alerts': result['number_of_alerts'],
            })


def explore_and_parse_files(root_dir):
    """return a list of results from parsing JSON files in the root directory."""
    all_results = []
    for dataset_folder in os.listdir(root_dir):
        package_information = {}
        package_information["dataset"] = dataset_folder

        dataset_path = os.path.join(root_dir, dataset_folder)
        if os.path.isdir(dataset_path) and dataset_folder.startswith("dataset"):
            for language_folder in os.listdir(dataset_path):
                language_path = os.path.join(dataset_path, language_folder)
                package_information["language"] = language_folder
                if os.path.isdir(language_path):
                    for package_file in os.listdir(language_path): 
                  
                        package_information["package"] = package_file
                        file_path = os.path.join(language_path, package_file)
                        results = parse_json_file(file_path, package_information)
                        all_results.extend(results)
    return all_results

def main():
    root_dir = r"D:\project\patd-results-main\patd-results-main\scan-results\oss-detect-backdoor"
    results = explore_and_parse_files(root_dir)
    
    output_file = r"D:\project\patd-results-main\patd-results-main\results-csv\oss-detect-backdoor\oss-detect-backdoor.csv"
    save_results_to_csv(results, output_file)
    


if __name__ == "__main__":
    main()