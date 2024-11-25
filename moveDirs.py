import os
import shutil

# Specify the source directory (where the "other" category items are currently located)
source_dir = "/Users/alexbanoun/Downloads"
# Specify the destination directory
destination_dir = "/Users/alexbanoun/Documents"  # Adjust as necessary

# List all items in the source directory
for item in os.listdir(source_dir):
    source_item = os.path.join(source_dir, item)
    destination_item = os.path.join(destination_dir, item)

    # Check if the item already exists in the destination directory
    if not os.path.exists(destination_item):
        # Move the item (file or directory) to the destination
        shutil.move(source_item, destination_dir)
    else:
        # Handle existing items, perhaps by renaming or manually resolving
        print(f"Item {item} already exists in {destination_dir}. Consider renaming or manually handling this item.")

