# File Operations Ad-Hoc Commands

```bash
# Create a directory on all VMs
ansible vagrant_vms -m file -a "path=/tmp/new_directory state=directory"

# Create an empty file on all VMs
ansible vagrant_vms -m file -a "path=/tmp/new_file state=touch"

# Set file permissions for an existing file on all VMs
ansible vagrant_vms -m file -a "path=/tmp/new_file mode=0644"

# Change ownership of a file on all VMs
ansible vagrant_vms -m file -a "path=/tmp/new_file owner=user1 group=group1"

# Remove a file on all VMs
ansible vagrant_vms -m file -a "path=/tmp/new_file state=absent"

# Remove a directory and its contents on all VMs
ansible vagrant_vms -m file -a "path=/tmp/new_directory state=absent"

# Create a symbolic link on all VMs
ansible vagrant_vms -m file -a "src=/var/log/target_file dest=/tmp/symlink_name state=link"

# Recursively set permissions for a directory on all VMs
ansible vagrant_vms -m file -a "path=/opt/new_structure mode=0750 recurse=yes"

# Check if a file exists and retrieve its checksum on all VMs
ansible vagrant_vms -m stat -a "path=/etc/important_config checksum_algo=sha256"

# Remove files older than 7 days from a directory on all VMs
ansible vagrant_vms -m find -a "paths=/var/log/ age=7d recurse=yes state=absent"
```

## Explanation of Modules and Arguments (File Operations)

- **`file` module**: Manages files, directories, and symbolic links.
  - **`path`**: Specifies the file or directory path.
  - **`state=directory`**: Ensures the specified path is a directory.
  - **`state=touch`**: Creates an empty file if it doesn’t already exist.
  - **`state=absent`**: Removes the file or directory if it exists.
  - **`mode`**: Sets the file permissions (e.g., `0644` for read/write by owner, read-only by others).
  - **`owner` and `group`**: Set the owner and group of the file or directory.
  - **`recurse=yes`**: Applies changes (like permissions) recursively to all files and subdirectories.
  - **`src` and `dest`**: Used for symbolic links, `src` defines the original file, and `dest` specifies the link name.
  
- **`stat` module**: Gathers information about files (e.g., checksums, permissions).
  - **`checksum_algo`**: Defines the algorithm used to calculate the checksum (e.g., `sha256`).
  - **`exists`**: Returns `true` if the file exists.
  - **`mode`**: Reports the permissions of the file.
  
- **`find` module**: Searches for files and directories that meet specified criteria.
  - **`paths`**: Specifies the directory to search in.
  - **`age`**: Filters files based on their modification time (e.g., `age=7d` to find files older than 7 days).
  - **`recurse=yes`**: Searches recursively through all subdirectories.
  - **`state=absent`**: Deletes files that match the criteria.
  
- **Common Arguments**:
  - **`-m`**: Specifies the module to use (e.g., `file`, `stat`, `find`).
  - **`-a`**: Defines the arguments passed to the module.
  - **`become=yes`**: Runs the command with escalated privileges (useful for file operations requiring root access).
