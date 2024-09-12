# Installing Ansible

```bash
# This guide covers the installation of Ansible on various systems.
# The project was developed on Ubuntu, but installation instructions for other distributions and OSes are also included.

# Prerequisites:
# - Python 3.x should be installed on your system.
# - Ensure you have administrative privileges or use `sudo`.

# For Ubuntu/Debian:
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install -y ansible

# For CentOS/RHEL:
sudo yum install -y epel-release
sudo yum install -y ansible

# For Fedora:
sudo dnf install -y ansible

# For macOS:
brew install ansible

# For Windows (WSL):
# First, set up WSL and install Ubuntu or another Linux distribution.
# Then, follow the Ubuntu installation steps:
sudo apt update
sudo apt install -y ansible

# Using pip (Python package manager):
# Ansible can also be installed via pip for any OS where Python and pip are available.
pip install ansible

# Verifying the Installation:
ansible --version

# You should see the installed Ansible version and other related details.

# Additional Notes:
# - Check official documentation for any OS-specific installation steps.
# - Use `ansible-galaxy` to install additional roles and collections as needed.
```