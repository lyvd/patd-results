import os
import yaml
import csv

def parse_yaml_file(file_path):
    results = {}
    with open(file_path, 'r', encoding='utf-8' , errors='ignore') as file:
        try:
            data = yaml.safe_load(file)
            if isinstance(data, list):
                data = data[0]

            file_paths = file_path.split(os.sep)
            package = file_paths[-1]
            dataset = file_paths[-3]  
            if not dataset.startswith('dataset'):
                dataset = file_paths[-2]
                            
            results['package'] = package
            results['dataset'] = dataset
            results['av_results'] = data['results']
        except yaml.YAMLError as e:
            print(f"Error parsing YAML file {file_path}: {e}")
        except Exception as e:
            print(f"Unexpected error processing file {file_path}: {e}")

    return results




def save_results_to_csv(results, output_file):
    # Collect all AV names
    av_names = set()
    for av in results[0]['av_results'].keys():
        av_names.add(av)
    av_names = sorted(av_names)
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Package', 'Dataset', '#AVs'] + av_names
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for result in results:
            row = {
                'Package': result['package'],
                'Dataset': result['dataset'],
                '#AVs':len(result.get('av_results', {}).keys()) ,
            }
            for av in av_names:
                row[av] = result.get('av_results', {}).get(av, {}).get('category', 'undetected')
            writer.writerow(row)



def explore_and_parse_files(root_dir):
    results = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            results.append(parse_yaml_file(file_path))
    return results

def main():

    results_dir = os.path.abspath(r'..\..\scan-results\vt')
    output_file = os.path.abspath(r'..\..\results-csv\vt\vt.csv')
    results = explore_and_parse_files(results_dir)
    save_results_to_csv(results, output_file)
    
    

if __name__ == "__main__":
    main()