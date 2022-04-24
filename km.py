import os
import shutil
import sys

sys.argv = sys.argv[1:]

for path, folders, files in os.walk(sys.argv[0]):
    if 'node_modules' in folders:
        try:
            if len(sys.argv) > 1 and sys.argv[1] == '--delete-all':
                    shutil.rmtree(path + '/node_modules')

            else:
                delete = input(f'Delete file on {path}: ')

                if delete == 'y':
                    shutil.rmtree(path + '/node_modules')

            print(f'Deleted {path}\\node_modules')

        except PermissionError:
            print(f'Cannot delete {path}\\node_modules')
