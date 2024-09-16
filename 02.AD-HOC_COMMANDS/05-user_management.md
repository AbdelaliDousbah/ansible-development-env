# User Management Ad-Hoc Commands

```bash

# Create a new user with a home directory on all Ubuntu VMs
ansible vagrant_vms -m user -a "name=johndoe state=present create_home=yes" --limit=ubuntu_vms

# Create a new user with a specified shell and group on all CentOS VMs
ansible vagrant_vms --limit=centos_vms -m user -a "name=johndoe state=present shell=/bin/bash group=users"

# Delete a user and remove their home directory on all Ubuntu VMs
ansible vagrant_vms -m user -a "name=johndoe state=absent remove=yes" --limit=ubuntu_vms

# Add a user to a specific group on all CentOS VMs
ansible vagrant_vms --limit=centos_vms -m user -a "name=johndoe groups=admins append=yes"

# Change a user's shell on all Ubuntu VMs
ansible vagrant_vms -m user -a "name=johndoe shell=/bin/zsh" --limit=ubuntu_vms

# Lock a user account to prevent login on all CentOS VMs
ansible vagrant_vms --limit=centos_vms -m shell -a "passwd -l johndoe"

# Unlock a user account to allow login on all CentOS VMs
ansible vagrant_vms --limit=centos_vms -m shell -a "passwd -u johndoe"

# Verify user accounts and their details (e.g., check existing users)
ansible vagrant_vms -m shell -a "getent passwd | grep johndoe" --limit=ubuntu_vms
ansible vagrant_vms --limit=centos_vms -m shell -a "getent passwd | grep johndoe"


```

## Explanation of Modules and Arguments (User Management)

- **`user` module**: Manages user accounts and groups.
  - **`name=johndoe`**: Specifies the username.
  - **`state=present`**: Ensures the user account exists.
  - **`state=absent`**: Ensures the user account is removed.
  - **`create_home=yes`**: Creates a home directory for the user.
  - **`shell=/bin/bash`**: Sets the user's login shell.
  - **`group=users`**: Assigns the user to a specific group.
  - **`remove=yes`**: Removes the user's home directory when deleting the account.
  - **`groups=admins`**: Adds the user to the specified group(s).
  - **`append=yes`**: Appends the user to the group without removing from existing groups.
  - **`passwd='password'`**: Sets the user's password.

- **`shell` module**: Executes shell commands on the managed nodes.
  - **`getent passwd`**: Retrieves user account information from the system's databases.
  - **`passwd -l johndoe`**: Locks the user account.
  - **`passwd -u johndoe`**: Unlocks the user account.
