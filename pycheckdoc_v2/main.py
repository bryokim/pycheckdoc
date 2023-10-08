#!/usr/bin/env python3
"""Main"""

import sys

# Local
from pycheckdoc_v2.generate_ast import get_ast
from pycheckdoc_v2.check_class import check_class_doc
from pycheckdoc_v2.check_function import check_function_doc
from pycheckdoc_v2.check_module import check_module_doc
from pycheckdoc_v2.print_funcs import print_error, print_success
from pycheckdoc_v2.usage import print_usage


def main():
    """Entry point"""

    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    modules = get_ast()

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
