Analyze the server traffic access log located at `/app/access.log`. Parse the data and generate a JSON summary report.

Write your final summary report to the following path:
`/app/report.json`

The JSON output must contain the following keys with their respective calculations:
1. "total_requests": The total count of all request entries in the access log file.
2. "unique_ips": The total count of unique client IP addresses identified in the log file.
3. "top_path": The resource path (e.g. `/index.html`) that was requested most frequently in the log file.
