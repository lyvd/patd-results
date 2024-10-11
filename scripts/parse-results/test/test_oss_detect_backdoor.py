import pytest
import os
import sys

# Add the parent directory to the sys.path to import bandit4mal
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from parse_oss_detect_backdoor import parse_oss_detect_backdoor_file

def test_parse_oss_detect_backdoor_valid_file():
    file_test = os.path.join(os.path.dirname(__file__), '../../../scan-results/oss-detect-backdoor/dataset1/js/add-position-99.10.9')
    results = parse_oss_detect_backdoor_file(file_test)
    assert len(results) == 1, "Expected 1 result for a valid log file"
    assert results[0]['number_of_alerts'] == 21, "Expected 1 alert in the log file"


def test_parse_oss_detect_backdoor_invalid_file():
    file_test = os.path.join(os.path.dirname(__file__), '../../../scan-results/oss-detect-backdoor/dataset1/js/add-position-99.10.9-invalid')
    results = parse_oss_detect_backdoor_file(file_test)
    assert len(results) == 0, "Expected no results for an invalid log file"

def test_parse_oss_detect_backdoor_2():
    file_test = os.path.join(os.path.dirname(__file__), '../../../scan-results/oss-detect-backdoor/dataset5/EVIL_RABBIT-4.5.1-r0')
    results = parse_oss_detect_backdoor_file(file_test)
    assert len(results) == 1, "Expected 1 result for a valid log file"
    assert results[0]['file'].endswith('.c'), "Expected file with .c extension"


def test_parse_oss_detect_backdoor_3():
    file_test = os.path.join(os.path.dirname(__file__), '../../../scan-results/oss-detect-backdoor/dataset5/shadowpass_steal-4.5.1-r0')
    results = parse_oss_detect_backdoor_file(file_test)
    assert len(results) == 0, "Expected 0 result because no path file code"

def test_parse_oss_detect_backdoor_4():
    file_test = os.path.join(os.path.dirname(__file__), '../../../scan-results/oss-detect-backdoor/dataset4/python/deprecation')
    results = parse_oss_detect_backdoor_file(file_test)
    assert len(results) == 4, "Expected 4 result for a valid log file"
    for result in results:
        assert result['file'].endswith('.py'), "Expected file with .py extension"

if __name__ == "__main__":
    pytest.main()

