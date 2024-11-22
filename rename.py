import os

# Optionally, change the working directory to where the files are
os.chdir("/Users/alexbanoun/Documents/Office")

# Loop through all files in the current directory
for file_name in os.listdir():
    # Check if it's a file
    if os.path.isfile(file_name):
        # Replace spaces with underscores in the file name
        new_file_name = file_name.replace(" ", "_")
        
        # Rename the file if the new name is different from the old name
        if new_file_name != file_name:
            os.rename(file_name, new_file_name)
            print(f"Renamed '{file_name}' to '{new_file_name}'")
