#!/usr/bin/env python3
"""Main"""

import sys
import argparse

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
    "paths", nargs="*", help="Paths to files/directories to check"
)
cli_args = parser.parse_args()


def main(args: argparse.Namespace = cli_args):
    """Pycheckdoc entry point.

    Args:
        `args` (Namespace, optional): Arguments passed to the programme in a
            `argparse.Namespace` . Defaults to `cli_args`. `cli_args` are
            arguments provided in the command line.

    Usage
    ---

    The sample below checks the current directory recursively.

    ```Python
    from pycheckdoc_v2.main import main, parser

    args = parser.parse_args([".", "-r"])   # Provide arguments
    main(args)  # Pass the arguments to main

    ```
    """

    if len(args.paths) == 0:
        print_usage()
        sys.exit(1)

    modules = get_ast(args.paths, recursive=args.recursive)

    if modules is None:  # Files provided don't exist
        print("Files provided don't exist")
        return

    total_errors = 0
    files_with_errors = 0

    for module in modules:
        prev_count = total_errors

        module_errors = check_module_doc(module)
        func_errors = check_function_doc(module)
        class_errors, method_errors = check_class_doc(module)

        total_errors += (
            module_errors + func_errors + class_errors + method_errors
        )

        if prev_count < total_errors:
            files_with_errors += 1

    if total_errors != 0 and files_with_errors != 0:
        print_error(total_errors, files_with_errors, len(modules))
    else:
        print_success(len(modules))


if __name__ == "__main__":
    main()
