## Overview

This project is designed to establish an Ansible development environment using Vagrant and Libvirt. The setup includes a host machine operating as the Ansible control node and two virtual machines (VMs) that are managed via Vagrant.

### Description of the Environment

- **Host Machine**: The control node for Ansible, which executes playbooks and manages configuration tasks across the VMs.
- **Virtual Machines**: Includes an Ubuntu 20.04 VM and a CentOS 8 VM, provisioned with specified resource allocations.
- **Vagrant with Libvirt**: Manages VM provisioning and lifecycle, with configurations defined in the `Vagrantfile` and VM management handled by Libvirt.

The VMs are configured to enable Ansible to manage them through SSH. A dynamic inventory script, `vagrant_inventory.py`, generates the inventory file for Ansible.

### Purpose of the Setup

- **Development and Testing**: Provides a controlled environment for developing and testing Ansible playbooks and configurations.
- **Learning and Experimentation**: Offers a practical environment for experimenting with Ansible without impacting your primary system.
- **Configuration Management**: Demonstrates the use of Ansible in conjunction with Vagrant-managed VMs for automated setup and node management.

### Topics Covered

- **Ansible Basics**: Introduction to Ansible, its architecture, workflow, and installation.
- **Ad-Hoc Commands**: Practical examples of using Ansible ad-hoc commands, categorized into system management, file operations, package management, service management, user management, resource management, log management, network management, application deployment, and scheduled tasks.

### Project Status

**This project is actively in progress.** The current structure includes foundational topics and practical examples, but ongoing updates will introduce additional sections and more comprehensive instructions as the project evolves.

### Installation and Setup Instructions

- **Host Machine Details**:
  - **Operating System**: Ubuntu

- **Software Versions**:
  - **libvirt**: `libvirtd (libvirt) 10.0.0`
  - **Vagrant**: `Vagrant 2.4.1`
  - **Vagrant Plugin**: `vagrant-libvirt (0.12.2, global)`
  - **Python**: `Python 3.12.3`
