# Ansible Architecture

## Components
- **Control Node**: Where Ansible runs and executes commands.
- **Managed Nodes**: Target systems managed by Ansible.
- **Inventory**: Defines the list of managed nodes.
- **Modules**: Predefined scripts or commands executed on managed nodes.

## How Ansible Works
- **Agentless**: No need for agents on managed nodes.
- **Push-based**: Control node pushes configurations to managed nodes.
- **Idempotency**: Ensures desired state without repeated actions.

## Data Flow
1. **Inventory File**: Lists managed nodes.
2. **Playbook**: Defines tasks and roles.
3. **Control Node**: Executes tasks using modules.
4. **Managed Nodes**: Receives and applies configurations.
