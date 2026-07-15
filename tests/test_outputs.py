import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")

def test_report_exists_and_valid_json():
    """1. Verify that the file exists and is valid JSON."""
    assert REPORT_PATH.exists(), "no report.json found"
    try:
         with open(REPORT_PATH) as f:
              data = json.load(f)
    except json.JSONDecodeError:
         assert False, "report.json is not valid JSON"

def test_report_content_integrity():
    """
    2. Verify total_requests, unique_ips, and top_path correspond 
    to the instruction criteria.
    """
    with open(REPORT_PATH) as f:
         data = json.load(f)
    
    assert "total_requests" in data, "Missing 'total_requests' key"
    assert "unique_ips" in data, "Missing 'unique_ips' key"
    assert "top_path" in data, "Missing 'top_path' key"
    
    # Assert actual parsed log outcomes
    assert data["total_requests"] == 6, f"Expected 6 total requests, got {data['total_requests']}"
    assert data["unique_ips"] == 3, f"Expected 3 unique IPs, got {data['unique_ips']}"
    assert data["top_path"] == "/index.html", f"Expected top_path to be '/index.html', got {data['top_path']}"
