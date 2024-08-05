import os
from pathlib import Path
from file_crawler import crawl_directory
from file_reader import read_file_content
from pdf_generator import create_pdf
from text_generator import create_text_file
from project_analyzer import generate_project_overview, generate_table_of_contents
from code_parser import extract_docstrings_and_comments, syntax_highlight


def main():
    # Ask for input project folder
    while True:
        input_dir = input("Enter the path to your project folder: ").strip()
        input_dir = Path(input_dir)
        if input_dir.is_dir():
            break
        else:
            print(
                f"Error: {input_dir} is not a valid directory. Please try again.")

    # Ask for output format using numeric input
    while True:
        print("Choose output format:")
        print("1. PDF")
        print("2. Text")
        choice = input("Enter your choice (1 or 2): ").strip()
        if choice in ['1', '2']:
            output_format = 'pdf' if choice == '1' else 'text'
            break
        else:
            print("Invalid choice. Please enter 1 for PDF or 2 for Text.")

    # Get the directory of the current script
    current_script_dir = Path(__file__).resolve().parent

    # Construct the output directory path relative to the project directory
    output_dir = current_script_dir / "Project_output_files"

    # Create the output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)

    # Generate a unique filename for the output
    base_name = input_dir.name
    output_extension = '.pdf' if output_format == 'pdf' else '.txt'
    output_name = f"{base_name}_code{output_extension}"
    counter = 1
    while (output_dir / output_name).exists():
        output_name = f"{base_name}_code_{counter}{output_extension}"
        counter += 1
    output_file = output_dir / output_name

    print(f"Scanning directory: {input_dir}")
    files = crawl_directory(input_dir)
    print("Generating project overview...")
    project_overview = generate_project_overview(input_dir)
    print("Generating table of contents...")
    toc = generate_table_of_contents(files)

    file_contents = []
    for file in files:
        print(f"Processing file: {file['path']}")
        content = read_file_content(file['path'])
        docstrings, comments = extract_docstrings_and_comments(file['path'])
        highlighted_content = syntax_highlight(file['path'], content)

        # Add docstrings and comments to the content if they exist
        if docstrings:
            highlighted_content = f"Docstrings:\n{docstrings}\n\n" + \
                highlighted_content
        if comments:
            highlighted_content = f"Comments:\n{''.join(comments)}\n\n" + \
                highlighted_content

        file_contents.append((file, highlighted_content))

    print(f"Generating {output_format.upper()} file: {output_file}")
    if output_format == 'pdf':
        create_pdf(project_overview, toc, file_contents, output_file)
    else:
        create_text_file(project_overview, toc, file_contents, output_file)

    print(f"{output_format.upper()} generation complete!")
    print(f"File saved as: {output_file}")


if __name__ == "__main__":
    main()
