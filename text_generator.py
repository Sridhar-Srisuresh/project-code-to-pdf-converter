def create_text_file(project_overview, toc, file_contents, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("Project Overview\n")
        f.write("================\n\n")
        f.write(project_overview)
        f.write("\n\n")

        f.write("Table of Contents\n")
        f.write("=================\n\n")
        f.write(toc)
        f.write("\n\n")

        for file_info, content in file_contents:
            f.write(f"File: {file_info['path']}\n")
            f.write("=" * (len(file_info['path']) + 6) + "\n\n")
            f.write(f"Size: {file_info['size']} bytes\n")
            f.write(f"Created: {file_info['created']}\n")
            f.write(f"Modified: {file_info['modified']}\n\n")
            f.write("Content:\n")
            f.write(content)
            f.write("\n\n")
