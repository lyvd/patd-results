# patd-results: A Study of Malware Prevention in Linux Distributions

This repository contains the source code and data for the paper titled "A Study of Malware Prevention in Linux Distributions". The main objective is to evaluate the performance of six open-source malware detection scanners.

## Repository Contents

- **Jupyter Notebook**: [`PATD_data_analysis.ipynb`](./notebooks/PATD_data_analysis.ipynb) - Contains code to generate tables and ROC curves for the paper.
- **Scan Results**: [`scan-results`](./scan-results/) - Results from malware detection scanners.
- **Parsed Results format CSV**: [`results-csv`](./results-csv/) - Contains CSV files with parsed results from the [`scan-results`](./scan-results/). These files include only HIGH or CRITICAL alerts, except for [`results-csv/full`](./results-csv/full/), which contains all alerts.
- **Scripts**: 
    - [`scripts`](./scripts/) - Contains automation scripts for running malware detection scanners.
    - [`parse-results`](./scripts/parse-results/) - Scripts to parse raw scan results into CSV format.
    - [`wolfi_modified_apk_download.sh`](./scripts/wolfi_modified_apk_download.sh) - Script to download APK files from Wolfi registries with available source code. Use the following command to execute:
        ```sh
        $ scripts/wolfi_modified_apk_download.sh --save-path /path-to-save --csv-file datasets/upstream_repos_filtered.csv
        ```
        - **--csv-file (optional)**: [`datasets/upstream_repos_filtered.csv`](./datasets/upstream_repos_filtered.csv) - This file contains a list of APK files with available source code in the Wolfi registry. This option will download only the APKs listed in the CSV.

## Setup Malware Scanners

1. **VirusTotal**: [VirusTotal](https://www.virustotal.com/gui/home/upload)
2. **Malcontent**: [Install Malcontent](https://github.com/chainguard-dev/malcontent#:~:text=pacman%20%2DS%20yara-,Install%20malcontent%3A,-go%20install%20github)
3. **Bandit4mal**: [Install Bandit4mal](https://github.com/lyvd/bandit4mal)
4. **Packj**: [`scripts\cg-packj`](./scripts/cg-packj/) - Modified Packj tool supporting three languages:
     - **Python**: [`cg_scanner.py`](./scripts/cg-packj/cg_scanner.py) - Script to scan Python samples.
     - **JavaScript**: [`cg_scanner_js.py`](./scripts/cg-packj/cg_scanner_js.py) - Script to scan JavaScript samples.
     - **Ruby**: [`cg_scanner_ruby.py`](./scripts/cg-packj/cg_scanner_ruby.py) - Script to scan Ruby samples.
5. **Oss-detect-backdoor**: [Install Oss-detect-backdoor](https://github.com/microsoft/OSSGadget?tab=readme-ov-file)


## Citation

If you use this repository or find it helpful, please cite our paper:

```bibtex
@article{vu2024study,
    title={A Study of Malware Prevention in Linux Distributions},
    author={Vu, Duc-Ly and Dunlap, Trevor and Obermeier-Velazquez, Karla and Gilbert, Paul and Meyers, John Speed and Torres-Arias, Santiago},
    journal={arXiv preprint arXiv:2411.11017},
    year={2024}
}
```
