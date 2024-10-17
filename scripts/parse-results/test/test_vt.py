import sys
import os
import pytest

# Add the parent directory to the sys.path to import parse_vt
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from parse_vt import parse_json_file

def test_parse_vt_valid_file():
    file_test = r"D:\HocTap\projectDrVuDucLy\final\patd-results\scan-results\vt\dataset3\js\jellyfin-web-10.9.7-r0.apk.json"
    results = parse_json_file(file_test)
    assert len(results) > 0, "Expected non-empty results for a valid log file"


if __name__ == "__main__":
    pytest.main()