import json
import re
from collections import Counter

LOG_PATH = "/app/access.log"
OUTPUT_PATH = "/app/report.json"

# Common Log Format pattern: IP ... "Method Path Protocol" Status ...
log_pattern = re.compile(r'^(\S+) \S+ \S+ \[[^\]]+\] "[A-Z]+ \S+ \S+" (\d+) \d+')

total_requests = 0
status_404_count = 0
ips = []

with open(LOG_PATH, "r") as f:
    for line in f:
        match = log_pattern.match(line.strip())
        if match:
            total_requests += 1
            ip, status = match.groups()
            ips.append(ip)
            if status == "404":
                status_404_count += 1

# Identify the most frequent IP
most_common_ip = Counter(ips).most_common(1)[0][0] if ips else ""

# Export metrics WITH THE INTRODUCED BUG
# Adding 9999 to total_requests and 50 to 404_errors to guarantee the verifier catches it
report = {
    "total_requests": total_requests + 9999,  # <--- BUG INTRODUCED (Expected: 1542, Output: 11541)
    "most_active_ip": most_common_ip,
    "404_errors": status_404_count + 50       # <--- BUG INTRODUCED (Expected: 37, Output: 87)
}

with open(OUTPUT_PATH, "w") as out:
    json.dump(report, out, indent=4)
