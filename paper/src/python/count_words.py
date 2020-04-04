"""This Python script counts words in a Markdown / LaTeX document(s).

Usage:
    python3 count_words.py <filename or directory>

It will ignore ATX headers, LaTeX & Markdown comments, and LaTeX markup tags.

"""
import sys
import os
import re


def is_md(filename: str,
    _ignored_files: set={'README.md', 'build.md'},
    _legal_extensions: set={'.md', '.markdown', '.tex'},
) -> bool:
    """
    Return a boolean determining if the filename is a markdown file.

    Args:
        filename: the filename to validate

        _legal_extensions: specific extensions to recognize as Markdown

    Returns:
        true if the filename is a markdown file, false otherwise

    """
    # if the filename is in the Markdown black list, ignore it
    if filename in _ignored_files:
        return False
    # iterate over the extensions in the accepted extensions
    for markdown_extension in _legal_extensions:
        if markdown_extension == filename[-len(markdown_extension):]:
            return True
    # the filename doesn't have a valid extension, return False
    return False


def markdown_filenames(directory: str) -> list:
    """
    Return a list of the filenames in the input directory.

    Args:
        directory: the input directory

    Returns:
        a list of the markdown files in the input directory.

    """
    try:
        # return a sorted list of the files in the given directory if they
        # are legal markdown files
        return sorted([file for file in os.listdir(directory) if is_md(file)])
    except FileNotFoundError:
        # catch a file not found error if the directory doesn't exist
        print('{} does not exist!'.format(directory))
        exit(1)


def clean_line(line: str) -> str:
    """
    Clean a single line and return it.

    Args:
        line: the line of Markdown / LaTeX to clean

    Returns:
        a cleaned line of text

    """
    # ignore latex comments, and markdown headers
    if '%' in line[:1] or '#' in line[:1]:
        # ignore LaTeX comment lines and Markdown header lines
        return ''
    # strip the line of all whitespace and new lines and append a single space
    return line.rstrip() + ' '


def clean_contents(contents: str) -> str:
    """
    Clean and return the contents of a LaTeX / Markdown file.

    Args:
        contents: the contents of the file to clean

    Returns:
        a file with all markup nonsense removed

    """
    # remove the LaTeX comment blocks
    contents = re.sub(r'\\begin{comment}.+?\\end{comment}', '', contents)
    # remove the general LaTeX markup
    contents = re.sub(r'\\.+?{.+?}(\[.+?\])?', '', contents)
    # remove the markdown comments from the text
    contents = re.sub(r'<!--.+?-->', '', contents)
    # remove markdown links and figures
    contents = re.sub(r'!?\[.*\](\(.+?\))?(:\s+?.+)?', '', contents)
    # remove markdown standard tables
    contents = re.sub(r'\|.*\|', '', contents)
    # return the clean text
    return contents


def read_file(filename: str) -> str:
    """
    Read the contents of a single file.

    Args:
        filename: the name of the file to read

    Returns:
        the string contents of the file

    """
    if not is_md(filename):
        raise ValueError('filename must have a valid markdown extension')
    # initialize the contents to store from the file
    contents = ''
    # open the file into the contents one line at a time
    with open(filename) as md_file:
        # iterate over each line in the file and write it to the output
        for line in md_file:
            contents += clean_line(line)
    # clean the entire contents of the file
    contents = clean_contents(contents)

    return contents


def read_dir(directory: str) -> str:
    """
    Read the contents of every Markdown / LaTeX file in a directory.

    Args:
        directory: the name of the directory to read files from

    Returns:
        the concatenated contents of the files in the directory

    """
    # initialize the contents to store from the files
    contents = ''
    # iterate over the files and collect their contents
    for filename in markdown_filenames(directory):
        contents += read_file('{}/{}'.format(directory, filename))

    return contents


def read_contents(filename: str) -> str:
    """
    Read the contents of a file or directory.

    Args:
        filename: the filename or directory to read

    Returns:
        the concatenated text from the file(s)

    """
    # if it's a directory, enter it and read the files
    if os.path.isdir(filename):
        return read_dir(filename)
    # otherwise read the file
    return read_file(filename)


def words(contents: str) -> list:
    """
    Return the list of words in a file's contents.

    Args:
        contents: the text to get the words in

    Returns:
        a list of all the words in the string

    """
    return re.findall(r'\w+', contents)


def get_filename() -> str:
    """
    Get the filename from the command line.

    Returns:
        the first positional argument (the filename)

    """
    try:
        # try to get the filename
        return sys.argv[1]
    except IndexError:
        # pass the exception along to the next level
        raise ValueError('no filename position argument!')


def _main():
    """Execute the code in this module as a standalone script."""
    try:
        # get the filename from the command line
        filename = get_filename()
    except ValueError:
        # print the usage information and exit
        print(__doc__)
        sys.exit(1)
    # read the contents of the file
    contents = read_contents(filename)
    # split the contents into words and count them
    word_count = len(words(contents))
    # print the word count to the console
    print('{} words in {}'.format(word_count, filename))


if __name__ == '__main__':
    _main()
