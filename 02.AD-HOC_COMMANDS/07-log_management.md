# Log Management Ad-Hoc Commands

```bash

# Rotate logs immediately without waiting for scheduled log rotation
ansible vagrant_vms -m shell -a "logrotate -f /etc/logrotate.conf"

# Monitor the Apache logs in real-time for critical errors on all VMs
ansible vagrant_vms -m shell -a "tail -f /var/log/apache2/error.log | grep -i 'crit'"  # Ubuntu
ansible vagrant_vms --limit=centos_vms -m shell -a "tail -f /var/log/httpd/error_log | grep -i 'crit'"  # CentOS

# Find logs for failed SSH login attempts and output details (Ubuntu)
ansible vagrant_vms -m shell -a "grep 'Failed password' /var/log/auth.log | awk '{print \$1, \$2, \$3, \$11}'"

# Search for log entries across multiple rotated log files (gzip) for a specific error
ansible vagrant_vms -m shell -a "zgrep -i 'out of memory' /var/log/syslog.*.gz"

# Automatically delete logs older than 7 days on all VMs to save disk space
ansible vagrant_vms -m shell -a "find /var/log -type f -mtime +7 -exec rm -f {} \;"

# Filter kernel logs for OOM (Out Of Memory) killer events on all VMs
ansible vagrant_vms -m shell -a "dmesg | grep -i 'oom-killer'"

# Analyze the system's disk usage for log files larger than 100MB
ansible vagrant_vms -m shell -a "find /var/log -type f -size +100M -exec ls -lh {} \;"

# Archive logs older than 30 days and compress them into a tarball
ansible vagrant_vms -m shell -a "find /var/log -type f -mtime +30 | tar -czvf /backup/logs_archive.tar.gz -T -"

# Monitor logs in real-time for multiple critical services using journalctl (systemd-based systems)
ansible vagrant_vms -m shell -a "journalctl -f -u nginx -u ssh -u mysql"

# Clear journal logs older than 2 weeks to free up space on Ubuntu VMs
ansible vagrant_vms -m shell -a "journalctl --vacuum-time=2weeks"

```
## Explanation of Modules and Arguments (Advanced Log Management)

- **`logrotate -f`**: Forces immediate rotation of logs based on the logrotate configuration file.
- **`tail -f | grep -i 'crit'`**: Monitors logs in real-time, filtering only critical log entries.
- **`awk`**: Extracts specific fields from logs, such as date and user information.
- **`zgrep`**: Searches within compressed (gzip) log files.
- **`find -mtime +7 -exec rm -f {}`**: Deletes log files older than 7 days.
- **`dmesg | grep 'oom-killer'`**: Filters kernel logs for Out Of Memory killer events.
- **`find /var/log -size +100M`**: Lists log files larger than 100MB to identify space issues.
- **`tar -czvf`**: Archives and compresses log files into a tarball.
- **`journalctl -f -u`**: Monitors logs in real-time for specified systemd services.
- **`journalctl --vacuum-time=2weeks`**: Clears journal logs older than 2 weeks to free up disk space.
