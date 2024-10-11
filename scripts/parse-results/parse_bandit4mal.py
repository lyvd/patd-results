import json
import csv
import os
import sys
from collections import Counter

VALID_FILE_EXTENSIONS = ['.html', '.css', '.js', '.ts', '.php', '.rb', '.py', '.java', '.cs', '.go', 
    '.r', '.pl', '.c', '.cpp', '.h', '.rs', '.swift', '.kt', '.lua', '.sh']

def parse_analysis_results(results_dir):
    results = []
    for root, dirs, files in os.walk(results_dir):
        for file in files:
            file_path = os.path.join(root, file)
            package_name = file_path.split("/")[-1].replace(".json", "")
            with open(file_path, "rb") as f:
                data_bytes = f.read()
                data_str = data_bytes.decode("utf-8", errors='ignore')
                data = json.loads(data_str)
                for result in data["results"]:
                    results.append([package_name, result["filename"], result['issue_text']])
    return results



def parse_bandit_results(file_path):
    package_information = {}
    package_information['dataset'] = file_path.split(os.sep)[-3]
    package_information['package'] = file_path.split(os.sep)[-1]
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            results = []
            number_of_alert = Counter()
            for result in data.get('results', []):
               file_path = result.get('filename', 'Unknown')
               if file_path.endswith(tuple(VALID_FILE_EXTENSIONS)):
                     number_of_alert[file_path] += 1
            
            for file, count in number_of_alert.most_common():
                results.append({
                    'dataset': package_information['dataset'],
                    'package': package_information['package'],
                    'file': file_path.replace('/home/lyvd/', ''),
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
    all_results = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                results = parse_bandit_results(file_path)
                all_results.extend(results)
    return all_results




def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    results_dir = os.path.abspath(os.path.join(script_dir, "../../scan-results/bandit4mal"))
    output_file = os.path.abspath(os.path.join(script_dir, "../../results-csv/bandit4mal/bandit4mal.csv"))


    results = explore_and_parse_files(results_dir)
    
    save_results_to_csv(results, output_file)
    


if __name__ == "__main__":
    main()
