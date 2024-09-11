## Overview

This project is designed to establish an Ansible development environment using Vagrant and Libvirt. The setup includes a host machine operating as the Ansible control node and two virtual machines (VMs) that are managed via Vagrant.

### Description of the Environment

- **Host Machine**: The control node for Ansible, which executes playbooks and manages configuration tasks across the VMs.

- **Virtual Machines**:
  - **Ubuntu 20.04 VM**: One of the managed nodes. It is provisioned using the `generic/ubuntu2004` box and is allocated 1 GB of memory and 1 CPU.
  - **CentOS 8 VM**: The second managed node, utilizing the `generic/centos8` box with the same resource configuration as the Ubuntu VM.

- **Vagrant with Libvirt**:
  - **Vagrant**: Handles the provisioning and management of the VMs. The `Vagrantfile` defines the VM configurations, including box types and resource allocations.
  - **Libvirt**: Serves as the provider for Vagrant, managing VM lifecycle and resources.

The VMs are configured to enable Ansible to manage them through SSH. A dynamic inventory script, `vagrant_inventory.py`, is used to generate the inventory file for Ansible by extracting SSH configurations from Vagrant.

### Purpose of the Setup

- **Development and Testing**: Provides a controlled environment for developing and testing Ansible playbooks and configurations. The use of both Ubuntu and CentOS VMs ensures compatibility and testing across different Linux distributions.

- **Learning and Experimentation**: Offers a practical environment for experimenting with Ansible without impacting your primary system. Vagrant and Libvirt simplify VM management, allowing for quick environment provisioning and teardown.

- **Configuration Management**: Demonstrates the use of Ansible in conjunction with Vagrant-managed VMs, focusing on automated setup and node management.

### Project Status

Please note that this project is still in progress. Future updates will include additional sections covering various Ansible topics and more comprehensive instructions.

### Installation and Setup Instructions

- **Host Machine Details**:
  - **Operating System**: Ubuntu

- **Software Versions**:
  - **libvirt**: `libvirtd (libvirt) 10.0.0`
  - **Vagrant**: `Vagrant 2.4.1`
  - **Vagrant Plugin**: `vagrant-libvirt (0.12.2, global)`
  - **Python**: `Python 3.12.3`
