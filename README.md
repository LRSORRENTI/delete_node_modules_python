# Node Modules Cleaner

## Overview
This Python script recursively searches for and deletes `node_modules` directories within a specified base directory. It is designed to help developers clean up disk space by removing unnecessary `node_modules` that can often consume a significant amount of space.

## Prerequisites
- Python 3.x installed on your system.
- Basic understanding of command line operations.
- Appropriate permissions to delete files in the target directories.

## Setup
1. **Download the Script**: Download the `delete_node_modules.py` file to your local machine.
2. **Modify the Base Directory**:
   - Open the `delete_node_modules.py` file in a text editor.
   - Locate the line that reads `base_directory = '/path/to/your/Desktop'`.
   - Replace `'/path/to/your/Desktop'` with the path to the directory where you want to start searching for `node_modules`. Ensure you have the correct path to avoid unintended deletions.
   

   ```
   base_directory = "C:\\Users\\username\\Desktop"
   ```

## Usage
To run the script, follow these steps:
1. Open your terminal or command prompt.
2. Navigate to the directory where the `delete_node_modules.py` file is saved.
3. Run the script by typing the following command and then press Enter:

```
python delete_node_modules.py
```
4. The script will start processing and will print paths of the `node_modules` directories as they are deleted.

## Caution
- This script will delete all `node_modules` directories found within the specified base directory and its subdirectories. Use it with caution, especially if pointing it towards directories with important projects.
- Always ensure you have backups or version control in place for any important data.

## License
This script is released under the MIT license.
