# Application Deployment Ad-Hoc Commands (Ubuntu)

```bash

# Update package cache and install Nginx on the Ubuntu VM
ansible vagrant_vms --limit=ubuntu_vm -m apt -a "name=nginx state=present update_cache=yes" -b

# Ensure the Nginx service is started and enabled to start on boot
ansible vagrant_vms --limit=ubuntu_vm -m service -a "name=nginx state=started enabled=yes" -b

# Copy a custom index.html to the Nginx web root on the Ubuntu VM
ansible vagrant_vms --limit=ubuntu_vm -m copy -a "src=/path/to/local/index.html dest=/var/www/html/index.html owner=www-data group=www-data mode=0644" -b

# Ensure UFW firewall allows HTTP traffic on port 80
ansible vagrant_vms --limit=ubuntu_vm -m ufw -a "rule=allow port=80 proto=tcp" -b


```

## Explanation of Modules and Arguments (Application Deployment)

- **`apt` module**: Manages the installation of the Nginx package on Ubuntu.
  - **`update_cache=yes`**: Updates the package cache.
  - **`state=present`**: Ensures that Nginx is installed.

- **`service` module**: Manages the Nginx service.
  - **`state=started`**: Ensures that the service is running.
  - **`enabled=yes`**: Enables the service to start on boot.

- **`copy` module**: Copies the `index.html` file to the web server root.
  - **`src`**: Specifies the local file to be copied.
  - **`dest`**: Specifies the destination path on the managed node.
  - **`owner` and `group`**: Sets the appropriate ownership for the web server user.
  - **`mode=0644`**: Ensures the file has the correct permissions.

- **`ufw` module**: Configures the firewall to allow HTTP traffic on port 80.
  - **`rule=allow`**: Allows the specified firewall rule.
  - **`port=80`**: Opens port 80 for HTTP traffic.
