import os
import re
import filecmp
import subprocess


def preprocess_scala_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Remove block comments (/** ... */)
    content = re.sub(r'/\*(.*?)\*/', '', content, flags=re.DOTALL)

    # Remove line comments (// ...)
    content = re.sub(r'//.*', '', content)

    # Remove docstrings (/** ... */)
    content = re.sub(r'/\*\*.*?\*/', '', content, flags=re.DOTALL)

    return content.strip()


def get_corresponding_files(dir1, dir2):
    files1 = os.listdir(dir1)
    files2 = os.listdir(dir2)

    # Only consider files with the same name in both directories
    common_files = set(files1) & set(files2)
    return [(os.path.join(dir1, file), os.path.join(dir2, file)) for file in common_files]


def run_diff(file1_path, file2_path):
    file1_content = preprocess_scala_file(file1_path)
    file2_content = preprocess_scala_file(file2_path)

    # Save the preprocessed content to temporary files
    with open('/tmp/preprocessed_file1.scala', 'w') as file1:
        file1.write(file1_content)

    with open('/tmp/preprocessed_file2.scala', 'w') as file2:
        file2.write(file2_content)

    # Run the diff tool (replace 'diff' with the appropriate command for your system)
    subprocess.run(['diff', '/tmp/preprocessed_file1.scala', '/tmp/preprocessed_file2.scala'])


if __name__ == "__main__":
    dir1 = 'path_to_directory1'
    dir2 = 'path_to_directory2'

    corresponding_files = get_corresponding_files(dir1, dir2)
    for file1, file2 in corresponding_files:
        if filecmp.cmp(file1, file2):
            print(f"{file1} and {file2} are identical.")
        else:
            print(f"Differences between {file1} and {file2}:")
            run_diff(file1, file2)
