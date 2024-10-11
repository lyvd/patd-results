import pytest
import os
import sys

# Add the parent directory to the sys.path to import bandit4mal
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from parse_bandit4mal import parse_bandit_results, explore_and_parse_files

def test_parse_bandit4mal_valid_file():
    file_test = os.path.join(os.path.dirname(__file__), '../../../scan-results/bandit4mal/dataset1/python/cis_publishers-1.2.3.tar')
    results = parse_bandit_results(file_test)
    assert len(results) > 0, "Expected non-empty results for a valid log file"
    assert results[0]['number_of_alerts'] == 8, "Expected 8 alert in the log file"

def test_parse_bandit4mal_invalid_file():
    file_test = os.path.join(os.path.dirname(__file__), '../../../scan-results/bandit4mal/dataset1/python/cis_publishers-1.2.3.tar-invalid')
    results = parse_bandit_results(file_test)
    assert len(results) == 0, "Expected no results for an invalid log file"


def test_parse_bandit4mal_2():
    file_test = os.path.join(os.path.dirname(__file__), '../../../scan-results/bandit4mal/dataset4/js/vite')
    results = parse_bandit_results(file_test)
    assert len(results) == 0, "Expected 0 result because no path file code"

def test_parse_bandit4mal_3():
    file_test = os.path.join(os.path.dirname(__file__), '../../../scan-results/bandit4mal/dataset4/js/jellyfin-web-master')
    results = parse_bandit_results(file_test)
    assert len(results) == 4, "Expected 4 result because it has 4 path file code"
    for result in results:
        assert result['file'].endswith('.py'), "Expected file with .py extension"

if __name__ == "__main__":
    pytest.main()
