import os
import shutil

source_dir = "/Users/alexbanoun/Documents"  # Adjust as necessary
destination_dir = "/Users/alexbanoun/Downloads"  # Adjust to your desired path

# Ensure the destination directory exists, create if not
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)


# Move each file from the source to the destination directory
for file_name in os.listdir(source_dir):
    source_file = os.path.join(source_dir, file_name)

    # Check if the item is a file before moving
    if os.path.isfile(source_file):
        destination_file = os.path.join(destination_dir, file_name)

        # Ensure there's no filename clash in the destination directory
        if not os.path.exists(destination_file):
            shutil.move(source_file, destination_file)
        else:
            print(f"File {file_name} already exists at the destination. Consider renaming or manually handling this file.")
    else:
        # If the item is not a file, you can choose to print a message or handle directories differently
        print(f"Skipping directory {file_name}.")
