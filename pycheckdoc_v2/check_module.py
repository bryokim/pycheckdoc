#!/usr/bin/env python3
"""Check module documentation"""

import ast
from typing import Tuple

# Local
from pycheckdoc_v2.print_funcs import print_module_err


def check_module_doc(module_tuple: Tuple[str, ast.Module]) -> int:
    """Check if the given module has documentation.

    Args:
        module_tuple (Tuple[str, ast.Module]): Tuple of module name and
            the modules abstract syntax tree.

    Returns:
        int: 0 if the module has documentation, else 1.
    """
    module_name, module_node = module_tuple

    if not ast.get_docstring(module_node):
        print_module_err(module_name)
        return 1

    return 0
