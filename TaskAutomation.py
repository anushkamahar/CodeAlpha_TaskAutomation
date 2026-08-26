import os
import shutil

source_folder = "photos"
destination_folder = "photos/jpg_files"
files = os.listdir(source_folder)

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for file in files:
    if file.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)
        print(f"Moved: {file}")

print("All JPG files moved successfully!")



