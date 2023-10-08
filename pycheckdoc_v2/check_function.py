#!/usr/bin/env python3
"""Check function documentation"""

import ast
from typing import Tuple

# Local
from pycheckdoc_v2.print_funcs import print_function_err


def check_function_doc(module_tuple: Tuple[str, ast.Module]) -> int:
    """Check if the functions in the given module have documentation.

    Args:
        module_tuple (Tuple[str, ast.Module]): Tuple of module path and
            the modules abstract syntax tree.
    Returns:
        int: Number of functions without documentation.
    """
    module_path, module_node = module_tuple

    function_nodes = [
        node for node in module_node.body if type(node) is ast.FunctionDef
    ]

    no_doc_num = 0

    for func_node in function_nodes:
        if not ast.get_docstring(func_node):
            print_function_err(
                module_path, func_node.name, line=func_node.lineno
            )
            no_doc_num += 1

    return no_doc_num
