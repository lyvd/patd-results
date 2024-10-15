import csv
import os
import json
import argparse

VALID_FILE_EXTENSIONS = ['.html', '.css', '.js', '.ts', '.php', '.rb', '.py', '.java', '.cs', '.go', 
    '.r', '.pl', '.c', '.cpp', '.h', '.rs', '.swift', '.kt', '.lua', '.sh']

def parse_bincapz_file(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return []
    
    file_path_parts = file_path.split(os.sep)
    package_information = {}
    
    # Determine the dataset name based on the file path structure
    if file_path_parts[-3].startswith(('dataset', 'wolfi-apks')):
        package_information['dataset'] = file_path_parts[-3]
    else:
        package_information['dataset'] = file_path_parts[-2]
    
    # Extract the package name from the file path
    package_information['package'] = file_path_parts[-1][:-5]

    # Parse the json file

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

            data = data.get('Files', {})

            results = []

            for dataPath in data:
                if dataPath.endswith(tuple(VALID_FILE_EXTENSIONS)):
                    if data[dataPath].get('RiskLevel', '') in ['CRITICAL', 'HIGH']:
                        results.append({
                            'package': package_information['package'],
                            'dataset': package_information['dataset'],
                            'file': dataPath,
                            'risk_level': data[dataPath].get('RiskLevel', '')
                        })
            return results
        
    except Exception as e:
        print(f"Error parsing JSON file {file_path}: {e}")
        return []


def explore_and_parse_logs(root_dir):
    all_results = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path) and file_path.endswith('.json'):
                results = parse_bincapz_file(file_path)
                all_results.extend(results)
    return all_results


def save_results_to_csv(results, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Package name', 'Dataset', 'File path', 'Risk level (high/critical)']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for result in results:
            writer.writerow({
                'Package name' : result['package'],
                'Dataset' : result['dataset'],
                'File path' : result['file'],
                'Risk level (high/critical)' : result['risk_level']
            })

def main():
    parser = argparse.ArgumentParser(description="Parse bincapz scan results and save to CSV.")
    parser.add_argument('-i', '--input', type=str, required=True, help='Directory containing bincapz scan results.')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output CSV file path.')
    
    args = parser.parse_args()
    
    results_dir = os.path.abspath(args.input)
    output_file = os.path.abspath(args.output)
    
    results = explore_and_parse_logs(results_dir)
    save_results_to_csv(results, output_file)

if __name__ == "__main__":
    main()
