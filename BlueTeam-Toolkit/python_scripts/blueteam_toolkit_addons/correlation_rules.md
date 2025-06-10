# SIEM Correlation Rules (Basic)

1. **Brute Force Detection:**
   - 5+ failed logins from one IP in 1 minute → Trigger Alert

2. **Unusual Country Login:**
   - GeoIP shows access from outside US → Alert

3. **Command Injection Detected:**
   - Keywords like `;`, `wget`, or `/bin/bash` in URI or POST

4. **High Volume Requests:**
   - >1000 requests from one IP in 5 minutes → Alert
