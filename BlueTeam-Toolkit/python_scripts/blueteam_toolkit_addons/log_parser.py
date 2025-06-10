import re, json

def parse_log_line(line):
    pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+).*[\[](?P<time>[^\]]+)[\]].*"(\w+) (.*?) HTTP.*?" (?P<status>\d+)'
    match = re.search(pattern, line)
    return match.groupdict() if match else None

with open("access.log", "r") as f:
    logs = [parse_log_line(line) for line in f if parse_log_line(line)]

with open("normalized_logs.json", "w") as f:
    json.dump(logs, f, indent=2)
