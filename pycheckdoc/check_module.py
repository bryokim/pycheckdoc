#!/usr/bin/env python3
"""Check documentation of a module"""

import inspect
from types import ModuleType

from pycheckdoc.print_funcs import print_module_err, print_module_success


def check_module_doc(module: ModuleType) -> int:
    """Check if the given module has documentation.
    If source file is empty, then it is skipped.

    Args:
        `module` (ModuleType): Module to check for its
            documentation.

    Returns:
        int: 0 if the module has documentation,
            1 if it doesn't have documentation.
    """
    val = 0
    if not module.__doc__:
        try:
            print_module_err(
                module.__name__, line=inspect.getsourcelines(module)[1]
            )
            val = 1
        except OSError:
            pass

    return val


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("Nope")
        sys.exit()

    from import_modules import import_modules

    module = import_modules()[0]

    check_module_doc(module)
