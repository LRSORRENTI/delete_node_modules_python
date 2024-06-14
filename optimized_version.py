import os
import shutil
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed

def delete_node_modules(directory, verbose=False):
    # Expand the user directory (e.g., ~/Desktop to /home/user/Desktop)
    directory = os.path.expanduser(directory)
    
    # Gather all node_modules directories
    node_modules_dirs = []
    for root, dirs, files in os.walk(directory):
        if 'node_modules' in dirs:
            nm_path = os.path.join(root, 'node_modules')
            node_modules_dirs.append(nm_path)
    
    # Function to delete a single node_modules directory
    def delete_directory(nm_path):
        try:
            shutil.rmtree(nm_path)
            if verbose:
                print(f"Deleted {nm_path}")
        except Exception as e:
            print(f"Error deleting {nm_path}: {e}")
    
    # Use ThreadPoolExecutor for concurrent deletion
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(delete_directory, nm_path) for nm_path in node_modules_dirs]
        for future in as_completed(futures):
            future.result()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Delete all node_modules directories in a given path.")
    parser.add_argument("directory", help="The base directory to search for node_modules.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity.")
    args = parser.parse_args()
    
    delete_node_modules(args.directory, args.verbose)

# EX: python delete_node_modules.py ~/Desktop/delete_node_modules_with_python/ -v

# Deleted Desktop/delete_node_modules_with_python/node_modules
# Deleted Desktop/delete_node_modules_with_python/backend/node_modules
# Deleted Desktop/delete_node_modules_with_python/backend/test/node_modules
# Deleted Desktop/delete_node_modules_with_python/modules/node/node_modules
# Deleted Desktop/delete_node_modules_with_python/modules/node/api/node_modules
# Deleted Desktop/delete_node_modules_with_python/test/node_modules
# Deleted Desktop/delete_node_modules_with_python/test/routes/node_modules