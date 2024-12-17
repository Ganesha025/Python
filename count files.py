import os
def count_files(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    return len(files)
directory_path = '/home/sharkway/Documents'
file_count = count_files(directory_path)
print(f'Number of files in "{directory_path}": {file_count}')