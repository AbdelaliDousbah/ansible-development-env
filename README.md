# Ansible Development Environment with Vagrant and Libvirt

## Overview

This project sets up an Ansible development environment using Vagrant and Libvirt. The environment consists of a host machine running as the Ansible control node and two virtual machines (VMs) managed by Vagrant. 

### Description of the Environment

- **Host Machine**: The host machine serves as the control node for Ansible. It runs Ansible and orchestrates configuration management tasks on the VMs.
  
- **Virtual Machines**:
  - **Ubuntu 20.04 VM**: One of the managed nodes. This VM uses the `generic/ubuntu2004` box and is configured with 1 GB of memory and 1 CPU.
  - **CentOS 8 VM**: The other managed node. This VM uses the `generic/centos8` box with the same configuration as the Ubuntu VM.

- **Vagrant with Libvirt**:
  - **Vagrant**: Used for managing and provisioning the VMs. The `Vagrantfile` specifies the configuration for the VMs, including the box type and resources.
  - **Libvirt**: Acts as the provider for Vagrant, handling the VM lifecycle and resource management.

The Vagrant-managed VMs are set up to allow Ansible to connect and manage them via SSH. The dynamic inventory script, `vagrant_inventory.py`, generates an inventory file for Ansible by retrieving SSH configurations directly from Vagrant. 

### Purpose of the Setup

- **Development and Testing**: This setup provides a controlled environment for developing and testing Ansible playbooks and configurations. By using VMs from different families (Ubuntu and CentOS), it simulates diverse environments and helps ensure compatibility across various systems.

- **Learning and Experimentation**: It allows users to experiment with Ansible in a practical environment without affecting their main system. The use of Vagrant and Libvirt simplifies VM management, enabling quick provisioning and teardown of environments for testing.

- **Configuration Management**: The environment demonstrates how to use Ansible with Vagrant-managed VMs, focusing on setting up and managing nodes through automated scripts and configurations.

This setup is ideal for those looking to improve their skills in Ansible, test configurations in isolated environments, or prepare for real-world deployment scenarios.
