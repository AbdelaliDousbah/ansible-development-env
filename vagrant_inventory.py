#!/usr/bin/env python
import subprocess
import json

# Define the command to get the SSH configuration from Vagrant
def get_vagrant_ssh_config():
    result = subprocess.run(['vagrant', 'ssh-config'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

# Parse the SSH configuration and generate an inventory
def parse_ssh_config(ssh_config):
    inventory = {
        "vagrant_vms": {
            "hosts": [],
            "vars": {}
        },
        "_meta": {
            "hostvars": {}
        }
    }
    host = None

    for line in ssh_config.splitlines():
        if line.startswith('Host '):
            host = line.split()[1]
            inventory["vagrant_vms"]["hosts"].append(host)
            inventory["_meta"]["hostvars"][host] = {"ansible_host": None, "ansible_user": "vagrant", "ansible_ssh_private_key_file": None}

        if 'HostName' in line and host:
            inventory["_meta"]["hostvars"][host]["ansible_host"] = line.split()[1]

        if 'IdentityFile' in line and host:
            inventory["_meta"]["hostvars"][host]["ansible_ssh_private_key_file"] = line.split()[1]

    return inventory

# Generate and print the JSON dynamic inventory
if __name__ == "__main__":
    ssh_config = get_vagrant_ssh_config()
    inventory = parse_ssh_config(ssh_config)
    print(json.dumps(inventory, indent=2))
