# System Management Ad-Hoc Commands

```bash
# Check the disk space usage on all VMs
ansible vagrant_vms -m shell -a "df -h"

# Display memory usage on all VMs
ansible vagrant_vms -m shell -a "free -m"

# Show CPU usage statistics on all VMs
ansible vagrant_vms -m shell -a "top -bn1 | grep 'Cpu(s)'"

# List swap space usage on all VMs
ansible vagrant_vms -m shell -a "swapon --show"

# Reboot all VMs
ansible vagrant_vms -m command -a "reboot"

# Display the system uptime on all VMs
ansible vagrant_vms -m shell -a "uptime"

# List all running services on all VMs
ansible vagrant_vms -m shell -a "systemctl list-units --type=service --state=running"

# Show all active processes on all VMs
ansible vagrant_vms -m shell -a "ps aux"

# Check for available package updates on Ubuntu VMs
ansible vagrant_vms -m apt -a "update_cache=yes"  # For Ubuntu

# Check for available package updates on CentOS VMs
ansible vagrant_vms -m dnf -a "update_cache=yes"   # For CentOS

# Apply system updates on Ubuntu VMs
ansible vagrant_vms -m apt -a "upgrade=yes"  # For Ubuntu

# Apply system updates on CentOS VMs
ansible vagrant_vms -m dnf -a "upgrade=yes"   # For CentOS

# Add a new system user on all VMs
ansible vagrant_vms -m user -a "name=new_user state=present"

# Remove an existing system user on all VMs
ansible vagrant_vms -m user -a "name=old_user state=absent"

# Check for open network ports on all VMs
ansible vagrant_vms -m shell -a "netstat -tuln"
```

## Explanation of Modules and Arguments

- **`shell` module**: Executes commands on the remote hosts. It is used here to run various shell commands.
  - **`-a "df -h"`**: Shows disk space usage in a human-readable format.
  - **`-a "free -m"`**: Displays memory usage in megabytes.
  - **`-a "top -bn1 | grep 'Cpu(s)'"`**: Provides CPU usage statistics.
  - **`-a "swapon --show"`**: Lists swap space usage.
  - **`-a "uptime"`**: Displays system uptime.
  - **`-a "systemctl list-units --type=service --state=running"`**: Lists all running services.
  - **`-a "ps aux"`**: Shows all active processes.
  - **`-a "netstat -tuln"`**: Lists all open network ports.

- **`command` module**: Runs commands on the remote hosts. Used here to reboot the VMs.
  - **`-a "reboot"`**: Reboots the system.

- **`apt` module**: Manages packages on Debian-based systems like Ubuntu.
  - **`-a "update_cache=yes"`**: Updates the package index cache.
  - **`-a "upgrade=yes"`**: Upgrades all installed packages.

- **`dnf` module**: Manages packages on Red Hat-based systems like CentOS.
  - **`-a "update_cache=yes"`**: Updates the package index cache.
  - **`-a "upgrade=yes"`**: Upgrades all installed packages.

- **`user` module**: Manages system users.
  - **`-a "name=new_user state=present"`**: Adds a new user.
  - **`-a "name=old_user state=absent"`**: Removes an existing user.
