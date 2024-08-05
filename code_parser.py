import ast
import tokenize
import io
from pathlib import Path
from pygments import highlight
from pygments.lexers import get_lexer_for_filename, TextLexer
from pygments.formatters import RawTokenFormatter


def is_python_file(file_path):
    return Path(file_path).suffix.lower() in ['.py', '.pyw']


def extract_docstrings_and_comments(file_path):
    if not is_python_file(file_path):
        return None, []  # Return None for docstrings and empty list for comments for non-Python files

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    try:
        tree = ast.parse(content)
        docstrings = ast.get_docstring(tree)
    except SyntaxError:
        # If there's a syntax error, we can't parse docstrings
        docstrings = None

    comments = []
    try:
        for token in tokenize.generate_tokens(io.StringIO(content).readline):
            if token.type == tokenize.COMMENT:
                comments.append(token.string)
    except tokenize.TokenError:
        # If there's a token error, we'll just return whatever comments we've collected so far
        pass

    return docstrings, comments


def syntax_highlight(file_path, content):
    # Simply return the content without any highlighting
    return content
