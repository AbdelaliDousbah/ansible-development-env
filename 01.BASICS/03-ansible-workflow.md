# Ansible Workflow

## Workflow Overview
1. **Define Inventory**: List managed nodes.
2. **Create Playbooks**: Outline tasks to be executed.
3. **Run Playbooks**: Execute tasks on managed nodes.
4. **Review Results**: Check the output and status of tasks.

## Key Concepts
- **Playbooks**: YAML files that contain automation tasks.
- **Tasks**: Individual steps defined in playbooks.
- **Roles**: Collections of tasks and configurations for reuse.
- **Handlers**: Special tasks triggered by changes.

## Execution Flow
1. **Parsing**: Ansible reads the playbook and inventory.
2. **Execution**: Tasks are executed on managed nodes.
3. **Reporting**: Results and status are reported back to the control node.
