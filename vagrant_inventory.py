#!/usr/bin/env python
import subprocess  # This module allows us to run external commands from within Python
import json        # This module is used to work with JSON data (useful for generating the dynamic inventory format)

# Function to retrieve the SSH configuration from Vagrant
def get_vagrant_ssh_config():
    """
    Runs the `vagrant ssh-config` command, which retrieves the SSH connection
    details for all VMs managed by Vagrant, including IP addresses and private keys.
    The output is then returned as a decoded string.
    """
    result = subprocess.run(['vagrant', 'ssh-config'], stdout=subprocess.PIPE)
    # Capture the command's output and decode it from bytes to a string
    return result.stdout.decode('utf-8')

# Function to parse the SSH config and convert it into an Ansible inventory format
def parse_ssh_config(ssh_config):
    """
    Takes the Vagrant SSH config as input (a plain text string) and converts it
    into a Python dictionary structured as an Ansible inventory. The inventory
    includes a 'vagrant_vms' group containing all Vagrant-managed VMs, along with
    host-specific details like the SSH private key and host address.
    """
    # Initialize the inventory structure
    inventory = {
        "vagrant_vms": {  # This group will hold all Vagrant-managed VMs
            "hosts": [],  # The list of VM hostnames
            "vars": {}    # Group-level variables (can be empty for now)
        },
        "_meta": {  # This section holds additional host-specific variables (called 'hostvars')
            "hostvars": {}  # Host-specific details like IP addresses and SSH keys
        }
    }
    
    host = None  # This variable will track the current VM being parsed

    # Iterate over each line of the SSH config output
    for line in ssh_config.splitlines():
        # When we encounter a 'Host' line, it indicates a new VM entry
        if line.startswith('Host '):
            host = line.split()[1]  # Extract the VM's name (e.g., 'vm1')
            inventory["vagrant_vms"]["hosts"].append(host)  # Add the VM to the 'vagrant_vms' group
            # Initialize the host-specific variables for this VM
            inventory["_meta"]["hostvars"][host] = {
                "ansible_host": None,  # This will be the VM's IP address
                "ansible_user": "vagrant",  # Vagrant uses the 'vagrant' user by default
                "ansible_ssh_private_key_file": None  # This will be the path to the private key
            }

        # Parse the VM's hostname (its IP address) from the 'HostName' line
        if 'HostName' in line and host:
            # Set the 'ansible_host' variable to the VM's IP address
            inventory["_meta"]["hostvars"][host]["ansible_host"] = line.split()[1]

        # Parse the path to the VM's private key from the 'IdentityFile' line
        if 'IdentityFile' in line and host:
            # Set the 'ansible_ssh_private_key_file' to the path of the SSH private key
            inventory["_meta"]["hostvars"][host]["ansible_ssh_private_key_file"] = line.split()[1]

    return inventory  # Return the final inventory dictionary

# Main section that generates and prints the dynamic inventory in JSON format
if __name__ == "__main__":
    """
    This section runs when the script is executed. It retrieves the Vagrant SSH config,
    parses it into an Ansible-compatible inventory structure, and then prints the 
    inventory as a JSON string, which Ansible can read as input.
    """
    ssh_config = get_vagrant_ssh_config()  # Retrieve the SSH config
    inventory = parse_ssh_config(ssh_config)  # Parse the config into an Ansible inventory
    print(json.dumps(inventory, indent=2))  # Print the inventory in pretty-printed JSON format
