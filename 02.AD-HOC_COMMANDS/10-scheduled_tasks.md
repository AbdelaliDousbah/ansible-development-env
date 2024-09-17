# Scheduled Tasks Ad-Hoc Commands (Ubuntu)

```bash

# Schedule a cron job to run a script every day at 2 AM
ansible vagrant_vms --limit=ubuntu_vm -m cron -a "name='Run daily backup' minute=0 hour=2 job='/usr/local/bin/backup.sh' state=present" -b

# Remove a cron job by name
ansible vagrant_vms --limit=ubuntu_vm -m cron -a "name='Run daily backup' state=absent" -b

# List all cron jobs for the vagrant user
ansible vagrant_vms --limit=ubuntu_vm -m shell -a "crontab -l"

# Ensure a systemd timer is enabled and started
ansible vagrant_vms --limit=ubuntu_vm -m systemd -a "name=daily.timer state=started enabled=yes" -b

# Check the status of the systemd timer
ansible vagrant_vms --limit=ubuntu_vm -m systemd -a "name=daily.timer state=status"

```

## Explanation of Modules and Arguments (Scheduled Tasks)

- **`cron` module**: Manages cron jobs on Ubuntu.
  - **`name`**: Specifies the name of the cron job.
  - **`minute` and `hour`**: Define the schedule for the cron job.
  - **`job`**: The command to run.
  - **`state=present`**: Ensures the cron job is created.
  - **`state=absent`**: Ensures the cron job is removed.

- **`shell` module**: Executes shell commands on the managed node.
  - **`crontab -l`**: Lists all cron jobs for the user.

- **`systemd` module**: Manages systemd timers.
  - **`name`**: Specifies the name of the systemd timer.
  - **`state=started`**: Ensures the timer is started.
  - **`enabled=yes`**: Ensures the timer starts on boot.
  - **`state=status`**: Checks the current status of the timer.
