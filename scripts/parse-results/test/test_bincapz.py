import os
import sys
import pytest

# Add the parent directory to the sys.path to import parse_bincapz
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from parse_bincapz import explore_and_parse_logs, parse_result_file

# def test_parse_bincapz_valid_file():
#     file_test = os.path.join(os.path.dirname(__file__), '../../../scan-results/bincapz/dataset1/js/add-position-99.10.9')
#     results = parse_result_file(file_test)
#     assert len(results) > 0, "Expected non-empty results for a valid log file"
#     assert results[0]['number_of_alerts'] == 16, "Expected 1 alert in the log file"

# def test_parse_bincapz_invalid_file():
#     file_test = os.path.join(os.path.dirname(__file__), '../../../scan-results/bincapz/dataset1/js/add-position-99.10.9-invalid')
#     results = parse_result_file(file_test)
#     assert len(results) == 0, "Expected no results for an invalid log file"

# def test_parse_bincapz_2():
#     file_test = os.path.join(os.path.dirname(__file__), '../../../scan-results/bincapz/dataset1/js/spring-projects-6.0.2')
#     results = parse_result_file(file_test)
#     assert len(results) == 3, "Expected 3 result because only 3 path file code"


from parse_bincapz import explore_and_parse_logs, parse_bincapz_file

def test_parse_bincapz_valid_file():
    # Construct the path to the test file
    file_test = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 
        '../../../scan-results/bincapz/dataset1/js/add-position-99.10.9.json'
    ))
    results = parse_bincapz_file(file_test)
    assert len(results) > 0, "Expected non-empty results for a valid log file"
    assert results[0]['risk_level'].lower() == "critical", "Expected critical  alert in the log file" 


def test_parse_bincapz_invalid_file():
    # Construct the path to the test file
    file_test = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 
        '../../../scan-results/bincapz/dataset1/js/add-position-99.10.9-invalid.json'
    ))
    results = parse_bincapz_file(file_test)
    assert len(results) == 0, "Expected no results for an invalid log file"

def test_parse_bincapz_2():
    file_test = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 
        '../../../scan-results/bincapz/dataset5/Backdoor.Linux.Rootin.b-4.5.1-r0.json'
    ))
    results = parse_bincapz_file(file_test)
    assert len(results) == 1, "Expected 1 because high alert"




    



if __name__ == "__main__":
    pytest.main()