import os

# Define the directories that need to be packages
folders = [
    'sequential_workflows',
    'sequential_workflows/bmi_calculate_workflow',
    'src'
]

for folder in folders:
    if os.path.exists(folder):
        init_file = os.path.join(folder, '__init__.py')
        if not os.path.exists(init_file):
            with open(init_file, 'a'):
                os.utime(init_file, None)
            print(f"Created: {init_file}")
        else:
            print(f"Already exists: {init_file}")
    else:
        print(f"Folder not found: {folder}")