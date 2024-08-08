import subprocess
import os

# Define the directories containing the scripts
directories = ['indeed', 'linkedin', 'glassdoor']

# Get the current directory
base_dir = os.getcwd()

# Run each app.py script
for directory in directories:
    dir_path = os.path.join(base_dir, directory)
    
    if os.path.isdir(dir_path):
        os.chdir(dir_path)
        print(f"Running app.py in {directory}...")
        result = subprocess.run(['python', 'app.py'], capture_output=True, text=True)
        print("Output:", result.stdout)
        print("Errors:", result.stderr)
        # Return to the base directory after running the script
        os.chdir(base_dir)
    else:
        print(f"Directory {directory} does not exist.")

print("Scripts have been executed.")
