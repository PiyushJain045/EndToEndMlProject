os.makedirs() is a function in Python that creates directories. It can create a single directory or a whole path of directories at once.

exist_ok Parameter:
If you set exist_ok=True, os.makedirs() won’t raise an error if the directory already exists.

-->What is os.path.dirname()?
os.path.dirname() is a function in Python that gets the directory name from a file path.

import os

# Get the directory name from a file path
file_path = "folder1/folder2/my_file.txt"
directory = os.path.dirname(file_path)
print(directory)  # Output: folder1/folder2

# Get the parent directory of a folder
folder_path = "folder1/folder2"
parent_directory = os.path.dirname(folder_path)
print(parent_directory)  # Output: folder1

## final result
os.makedirs('artifacts', exist_ok=True) -->creates a artifact directory if it dosent exists 