#!/usr/bin/env python3
"""Entry point"""

import sys

from pycheckdoc.usage import print_usage

if len(sys.argv) == 1:
    print_usage()
    sys.exit()


from pycheckdoc.check_function import check_function_doc_single
from pycheckdoc.check_module import check_module_doc
from pycheckdoc.check_class import check_class_doc

from pycheckdoc.print_funcs import print_error, print_success

from pycheckdoc.import_modules import import_modules


def main():
    """Check module, class, function and class methods documentation.
    Prints the status, either success or errors found to stdout.
    """

    modules = import_modules()

    error_count: int = 0
    error_files: int = 0

    for module in modules:
        prev_count = error_count

        mod_status = check_module_doc(module)
        func_status = check_function_doc_single(module)
        class_status = check_class_doc(module)

        error_count += (
            mod_status + func_status + class_status[0] + class_status[1]
        )

        if prev_count < error_count:
            error_files += 1

    if error_files != 0 and error_count != 0:
        print_error(error_count, error_files, len(modules))
    else:
        print_success(len(modules))


if __name__ == "__main__":
    main()
