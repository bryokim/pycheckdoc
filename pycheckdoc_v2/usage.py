"""pycheckdoc_v2 usage"""


USAGE = """
Check documentation of python source files

Path to the file/directory to check can either be relative
or absolute.

Path is relative if it's a direct child of the cwd.

If path to a directory is provided, any .py files existing
in the directory are checked.

Both relative and absolute paths can be passed as arguments
for the same call.
    pycheckdoc file.py /home/user/dev/main.py

Examples:
    Check file.py that is in the cwd:
        pycheckdoc file.py

    Check file.py in the src directory in the cwd:
        pycheckdoc src/file.py

    Check all .py files in the src directory in the cwd:
        pycheckdoc src
        pycheckdoc src/*.py

    Check a file or directory not in the cwd:
        pycheckdoc /home/user/dev/file.py   -> File
        pycheckdoc /home/user/dev   -> Directory

    Check directories recursively:
        pycheckdoc -r dir
"""


def print_usage():
    """Print usage"""
    print("USAGE: pycheckdoc [-h] [-r] [paths ...]")

    print(USAGE)
