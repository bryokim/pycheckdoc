#!/usr/bin/env python3
"""Check module documentation"""

import ast
from typing import Tuple

# Local
from pycheckdoc_v2.print_funcs import print_module_err


def check_module_doc(
    module_tuple: Tuple[str, ast.Module], print_msgs: bool = True
) -> int:
    """Check if the given module has documentation.

    Args:
        module_tuple (Tuple[str, ast.Module]): Tuple of module path and
            the modules abstract syntax tree.
        print_msgs (bool, optional): Whether to print the error/success
            messages. Defaults to `True`.

    Returns:
        int: 0 if the module has documentation, else 1.
    """
    module_path, module_node = module_tuple

    if not ast.get_docstring(module_node):
        if print_msgs:
            print_module_err(module_path)
        return 1

    return 0
