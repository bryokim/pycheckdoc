#!/usr/bin/env python3
"""Main"""

import sys
import argparse
from typing import List, Tuple

# Local
from pycheckdoc_v2.generate_ast import get_ast
from pycheckdoc_v2.check_class import check_class_doc
from pycheckdoc_v2.check_function import check_function_doc
from pycheckdoc_v2.check_module import check_module_doc
from pycheckdoc_v2.print_funcs import print_error, print_success
from pycheckdoc_v2.usage import print_usage


parser = argparse.ArgumentParser(
    description="Check documentation of python source files"
)

parser.add_argument(
    "-r",
    "--recursive",
    dest="recursive",
    action="store_true",
    help="Recurse over directories.",
)

parser.add_argument(
    "--no-print",
    dest="print",
    action="store_false",
    help="Don't print error or success messages",
)

parser.add_argument(
    "paths", nargs="*", help="Paths to files/directories to check"
)
args = parser.parse_args()


def main(
    paths: List[str] = args.paths,
    recursive: bool = args.recursive,
    print_msgs: bool = args.print,
) -> Tuple[int, int]:
    """Pycheckdoc entry point.

    Arguments are read from the command line if none is provided.

    Args:
        paths (List[str], optional): List of the paths to check.
        recursive (Bool, optional): Whether to check directories recursively.
            Defaults to `False`.
        print_msgs (Bool, optional): Whether to print file errors and success
            messages. Defaults to `True`.

    Returns:
        Tuple[int, int]: Tuple of total errors and files with errors. If an
            error occurs then (-1, -1) is returned.

    Usage
    ---

    The sample below checks the current directory recursively.

    ```Python
    from pycheckdoc_v2.main import main, parser

    args = parser.parse_args([".", "-r"])   # Provide arguments
    main(args)  # Pass the arguments to main

    ```
    """

    if len(paths) == 0:
        print_usage()
        sys.exit(1)

    modules = get_ast(paths, recursive=recursive)

    if modules is None:  # Files provided don't exist
        print("Files provided don't exist")
        return (-1, -1)

    total_errors = 0
    files_with_errors = 0

    for module in modules:
        prev_count = total_errors

        module_errors = check_module_doc(module, print_msgs)
        func_errors = check_function_doc(module, print_msgs)
        class_errors, method_errors = check_class_doc(module, print_msgs)

        total_errors += (
            module_errors + func_errors + class_errors + method_errors
        )

        if prev_count < total_errors:
            files_with_errors += 1

    if print_msgs:
        if total_errors != 0 and files_with_errors != 0:
            print_error(total_errors, files_with_errors, len(modules))
        else:
            print_success(len(modules))

    return (total_errors, files_with_errors)


def check_doc(
    paths: List[str],
    recursive: bool = False,
    print_msgs: bool = False,
) -> Tuple[int, int]:
    """Check python file documentation.
    Use this in other python files instead of main.

    Args:
        paths (List[str], optional): List of the paths to check.
        recursive (Bool, optional): Whether to check directories recursively.
            Defaults to `False`.
        print_msgs (Bool, optional): Whether to print file errors and success
            messages. Defaults to `False`.

    Raises:
        ValueError: If length of paths is 0.

    Returns:
        Tuple[int, int]: Tuple of total errors and files with errors.
    """
    if len(paths) == 0:
        raise ValueError

    return main(
        paths=paths,
        recursive=recursive,
        print_msgs=print_msgs,
    )


if __name__ == "__main__":
    main()
