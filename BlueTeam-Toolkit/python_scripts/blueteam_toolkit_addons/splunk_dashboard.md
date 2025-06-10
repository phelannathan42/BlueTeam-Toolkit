# Splunk Dashboard Overview

This dashboard includes:
- Failed login attempts over time
- Top 10 source IPs for failed logins
- Event type classification

**Search Sample:**
```
sourcetype=auth_log "Failed password" | timechart count by src_ip
```
