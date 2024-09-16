# Service Management Ad-Hoc Commands

```bash
## Reload a service configuration without stopping the service (Ubuntu VMs)
ansible vagrant_vms -m service -a "name=nginx state=reloaded" --limit=ubuntu_vms

# Mask a service to prevent it from being started manually or automatically (CentOS VMs)
ansible vagrant_vms --limit=centos_vms -m service -a "name=httpd masked=yes"

# Unmask a service to allow it to be started manually or automatically (CentOS VMs)
ansible vagrant_vms --limit=centos_vms -m service -a "name=httpd masked=no"

# Restart all services that have been updated by package updates (Ubuntu VMs)
ansible vagrant_vms -m shell -a "systemctl daemon-reload && systemctl restart $(systemctl list-units --state=loaded --no-pager)"

# Check for failed services and restart them if necessary (CentOS VMs)
ansible vagrant_vms --limit=centos_vms -m shell -a "systemctl --failed --no-pager | grep -q 'loaded units listed' && systemctl restart $(systemctl list-units --failed --no-pager)"

# Stop and disable a service simultaneously on all Ubuntu VMs
ansible vagrant_vms -m service -a "name=nginx state=stopped enabled=no" --limit=ubuntu_vms

# Enable and start multiple services in one command (CentOS VMs)
ansible vagrant_vms --limit=centos_vms -m service -a "name=httpd enabled=yes state=started"
ansible vagrant_vms --limit=centos_vms -m service -a "name=firewalld enabled=yes state=started"

# Ensure a service is running, and if it's not, start it and send an alert (Ubuntu VMs)
ansible vagrant_vms -m shell -a "systemctl is-active nginx || (systemctl start nginx && echo 'Service nginx started' | mail -s 'nginx Service Alert' admin@example.com)" --limit=ubuntu_vms
```

## Explanation of Advanced Commands

- **`state=reloaded`**: Reloads the service configuration without stopping the service, useful for applying configuration changes.
- **`masked=yes/no`**: Masks or unmasks the service, preventing or allowing it to be started manually or automatically.
- **`systemctl daemon-reload`**: Reloads the systemd manager configuration to apply changes after package updates.
- **`--failed`**: Lists failed services, and with `grep`, checks if any failures exist, then restarts them if found.
- **`is-active`**: Checks the service's current status, and the command starts the service if it's not running and sends an alert.
 