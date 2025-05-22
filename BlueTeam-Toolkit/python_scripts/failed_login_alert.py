import re

with open("../log_samples/nginx_attack.log", "r") as file:
    lines = file.readlines()

for line in lines:
    if "Failed password" in line or "401 Unauthorized" in line:
        print("[ALERT] Suspicious login attempt:", line.strip())
