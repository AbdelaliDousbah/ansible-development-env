# Resource Management Ad-Hoc Commands

```bash

# Check disk usage on all VMs
ansible vagrant_vms -m shell -a "df -h"

# Check memory usage on all VMs
ansible vagrant_vms -m shell -a "free -h"

# Check CPU usage and load average on all VMs
ansible vagrant_vms -m shell -a "top -bn1 | grep 'Cpu(s)'"

# Display the top 10 processes by memory usage on all VMs
ansible vagrant_vms -m shell -a "ps aux --sort=-%mem | head -n 10"

# Display the top 10 processes by CPU usage on all VMs
ansible vagrant_vms -m shell -a "ps aux --sort=-%cpu | head -n 10"

# Check the amount of free and used memory on all VMs
ansible vagrant_vms -m shell -a "vmstat -s"

# Check the number of currently running processes on all VMs
ansible vagrant_vms -m shell -a "ps aux | wc -l"

```

## Explanation of Modules and Arguments (Resource Management)

- **`shell` module**: Executes shell commands on the managed nodes.
  - **`df -h`**: Displays disk usage in a human-readable format.
  - **`free -h`**: Shows memory usage in a human-readable format.
  - **`top -bn1 | grep 'Cpu(s)'`**: Retrieves CPU usage and load average.
  - **`ps aux --sort=-%mem | head -n 10`**: Lists the top 10 processes by memory usage.
  - **`ps aux --sort=-%cpu | head -n 10`**: Lists the top 10 processes by CPU usage.
  - **`vmstat -s`**: Provides a summary of system memory, swap, and I/O statistics.
  - **`ps aux | wc -l`**: Counts the number of currently running processes.
