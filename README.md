# Ansible Development Environment with Vagrant

## Overview

This project provides a comprehensive development environment for Ansible and Vagrant, utilizing virtual machines (VMs) managed by Vagrant with the Libvirt provider. The setup is designed to facilitate the development and testing of Ansible playbooks across different Linux distributions.

### Environment and Purpose

**Basic Environment**:
- **Ubuntu VM**: Runs Ubuntu, a popular Linux distribution known for its user-friendliness and widespread use.
- **CentOS VM**: Runs CentOS, a distribution derived from Red Hat Enterprise Linux (RHEL), known for its stability and enterprise-level features.

**Purpose**:
- **Cross-Platform Testing**: Ensures compatibility of Ansible playbooks across various distributions.
- **Comprehensive Development**: Allows thorough testing of configurations and automation tasks.

**Key Features**:
- **Dynamic Inventory**: Managed by `vagrant_inventory.py`.
- **Simple Setup**: Configured via `Vagrantfile`.
- **Customizable Environment**: VMs and configurations are adaptable for various scenarios.

## Requirements

### Software Requirements

1. **Vagrant**
   - **Version**: [Specify version or range]
   - **Installation**: [Download and install Vagrant](https://www.vagrantup.com/downloads)

2. **Ansible**
   - **Version**: [Specify version or range]
   - **Installation**: [Install Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)

3. **Python**
   - **Version**: Python 3.x
   - **Installation**: [Download and install Python](https://www.python.org/downloads/)

4. **Python Libraries** (for dynamic inventory script)
   - **Required Libraries**: [List libraries, e.g., `pyyaml`]
   - **Installation**: Install using pip:
     ```bash
     pip install pyyaml
     ```

5. **Libvirt**
   - **Version**: [Specify version or range]
   - **Installation**: [Install Libvirt](https://libvirt.org/install.html)

6. **Vagrant Libvirt Plugin**
   - **Version**: [Specify version or range]
   - **Installation**: Install the Vagrant Libvirt plugin:
     ```bash
     vagrant plugin install vagrant-libvirt
     ```

### System Requirements

- **Memory**: Minimum of 4 GB RAM (recommended: 8 GB)
- **CPU**: Minimum of 2 CPU cores (recommended: 4 cores)
- **Disk Space**: At least 20 GB free space

### Optional Dependencies

- **VirtualBox** or other Vagrant-compatible providers (if applicable)

### Installation Instructions

1. **Install Vagrant**: Follow the [installation guide](https://www.vagrantup.com/downloads).
2. **Install Ansible**: Follow the [installation guide](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html).
3. **Install Python**: Ensure Python 3.x is installed from [Python.org](https://www.python.org/downloads/).
4. **Install Required Python Libraries**: Use pip to install any necessary libraries.
5. **Install Libvirt**: Follow the [installation instructions](https://libvirt.org/install.html) for your system.
6. **Install Vagrant Libvirt Plugin**: Use the command provided above to install the plugin.

## Setup Instructions

1. Clone the Repository
2. Install Dependencies
3. Start the Virtual Machines
4. Verify SSH Configuration (Optional)
5. Run Ansible Commands

## File Descriptions

- `Vagrantfile`
- `ansible.cfg`
- `vagrant_inventory.py`
- `.gitignore`

## Example Playbook

## Troubleshooting

## Additional Notes
