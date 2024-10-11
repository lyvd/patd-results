import sys
import os
import pytest

# Add the parent directory to the sys.path to import parse_vt
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from parse_vt import parse_yaml_file

def test_parse_vt_valid_file():
    file_test = os.path.join(os.path.dirname(__file__), '../../../scan-results/vt/dataset1/js/add-position-99.10.9')
    results = parse_yaml_file(file_test)
    assert results['av_results']['Kaspersky']['category'] == 'malicious', "Expected malicious result for Kaspersky AV"
    assert results['av_results']['ZoneAlarm']['category'] == 'malicious', "Expected malicious result for ZoneAlarm AV"
    assert results['av_results']['Yandex']['category'] == 'undetected', "Expected undetected result for Yandex AV"

def test_parse_vt_invalid_file():
    file_test = os.path.join(os.path.dirname(__file__), '../../../scan-results/vt/dataset1/js/add-position-99.10.9-invalid')
    results = parse_yaml_file(file_test)
    assert results == {}, "Expected empty results for an invalid log file"


if __name__ == "__main__":
    pytest.main()