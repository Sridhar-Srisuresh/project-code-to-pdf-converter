import os
from pathlib import Path
from datetime import datetime


def get_file_metadata(file_path):
    stats = os.stat(file_path)
    return {
        'path': str(file_path),
        'name': file_path.name,
        'extension': file_path.suffix,
        'size': stats.st_size,
        'created': datetime.fromtimestamp(stats.st_ctime),
        'modified': datetime.fromtimestamp(stats.st_mtime)
    }


def generate_directory_tree(directory):
    directory = Path(directory)  # Ensure directory is a Path object
    tree = []
    for root, dirs, files in os.walk(directory):
        root_path = Path(root)
        level = len(root_path.relative_to(directory).parts)
        indent = '  ' * level
        tree.append(f"{indent}{root_path.name}/")
        for file in files:
            tree.append(f"{indent}  {file}")
    return '\n'.join(tree)


def crawl_directory(directory):
    directory = Path(directory)  # Ensure directory is a Path object
    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = Path(root) / file
            file_list.append(get_file_metadata(file_path))
    return file_list
