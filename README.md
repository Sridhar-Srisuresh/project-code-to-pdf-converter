# Project Code to PDF/Text Converter

This Python project converts the contents of a project directory into either a PDF or a text file, making it easy to document and share your code projects. It is particularly useful for overcoming file attachment limitations encountered while working with chat-based Language Model (LLM) systems. This tool allows you to submit entire projects as context, provided they fall within the LLM's context length constraints.

## Features

- Scans a specified project directory
- Generates a project overview and table of contents
- Extracts docstrings and comments from Python files
- Allows user to choose between PDF and text file output

## Limitations

- File size and type restrictions may apply based on the capabilities of the underlying conversion libraries.

## Requirements

- Python 3.x
- ReportLab
- Pygments

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/project-code-to-pdf-converter.git
   ```
2. Navigate to the project directory:
   ```
   cd project-code-to-pdf-converter
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the main.py script:
   ```
   python main.py
   ```
2. Enter the path to your project folder when prompted.
3. Choose the output format:
   - Enter '1' for PDF output
   - Enter '2' for text file output
4. The generated file will be saved in the `Project_output_files` directory.

## Project Structure

- `main.py`: The main script that orchestrates the conversion process
- `file_crawler.py`: Handles directory traversal and file metadata extraction
- `file_reader.py`: Reads the content of files
- `code_parser.py`: Extracts docstrings and comments from Python files
- `project_analyzer.py`: Generates project overview and table of contents
- `pdf_generator.py`: Creates the PDF output
- `text_generator.py`: Creates the text file output
- `pdf_styler.py`: Defines styles for PDF generation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Project Roadmap

- Support for syntax highlighting for code content
- Line numbering in the code section

## License

This project is open source and available under the [MIT License](LICENSE).
