import os
from file_crawler import generate_directory_tree

def generate_project_overview(project_dir):
    overview = f"Project Directory: {project_dir}\n\n"
    overview += "Directory Structure:\n"
    overview += generate_directory_tree(project_dir)
    return overview

def generate_table_of_contents(file_list):
    toc = "Table of Contents\n\n"
    for i, file in enumerate(file_list, 1):
        toc += f"{i}. {file['name']} (p. {i})\n"
    return toc