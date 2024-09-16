# Package managemenet Ad-Hoc Commands

```bash

# Update the package index and upgrade packages in a single command on all Ubuntu VMs
ansible vagrant_vms -m apt -a "update_cache=yes upgrade=yes"

# Perform a security update only on all Ubuntu VMs
ansible vagrant_vms -m apt -a "upgrade=dist" -b

# Install a specific version of a package and ensure its dependencies are resolved on all CentOS VMs
ansible vagrant_vms --limit=centos_vms -m dnf -a "name=httpd state=present enablerepo=updates"

# Remove a package and its dependencies that are no longer needed on all CentOS VMs
ansible vagrant_vms --limit=centos_vms -m dnf -a "name=vim state=absent autoremove=yes"

# Perform a full upgrade, including kernel updates, on all Ubuntu VMs
ansible vagrant_vms -m apt -a "upgrade=full-upgrade" -b

# Reinstall a package to ensure it is correctly configured and functioning on all VMs
ansible vagrant_vms -m apt -a "name=nginx state=reinstalled"  # For Ubuntu
ansible vagrant_vms --limit=centos_vms -m dnf -a "name=httpd state=reinstalled"  # For CentOS

```

## Explanation of Modules and Arguments (Package Management)

- **`apt` module**: Manages packages on Debian-based systems like Ubuntu.
  - **`update_cache=yes`**: Updates the package index cache.
  - **`upgrade=yes`**: Upgrades all installed packages.
  - **`upgrade=dist`**: Performs a security update only.
  - **`upgrade=full-upgrade`**: Upgrades all packages, including kernel updates.
  - **`state=reinstalled`**: Reinstalls the specified package to ensure correct configuration.

- **`dnf` module**: Manages packages on Red Hat-based systems like CentOS.
  - **`name`**: Specifies the package name.
  - **`state=present`**: Ensures the package is installed.
  - **`state=absent`**: Ensures the package is removed.
  - **`autoremove=yes`**: Removes packages that were installed as dependencies but are no longer needed.
  - **`enablerepo`**: Enables a specified repository.
  - **`--limit`**: Specifies the target VMs (e.g., `centos_vms`).

- **Common Arguments**:
  - **`-m`**: Specifies the module to use (e.g., `apt`, `dnf`).
  - **`-a`**: Defines the arguments passed to the module.
  - **`-b`**: Runs the command with escalated privileges (useful for package management requiring root access).

