from collections import defaultdict
import time

ip_attempts = defaultdict(list)

with open("auth.log") as f:
    for line in f:
        if "Failed password" in line:
            parts = line.split()
            ip = parts[-4]
            timestamp = time.time()
            ip_attempts[ip].append(timestamp)

for ip, attempts in ip_attempts.items():
    if len(attempts) > 5 and (max(attempts) - min(attempts)) < 60:
        print(f"[ALERT] Potential brute-force from {ip}")
