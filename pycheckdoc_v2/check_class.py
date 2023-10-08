#!/usr/bin/env python3
"""Check class and method documentation """

import ast
from typing import Tuple


from pycheckdoc_v2.print_funcs import print_class_err, print_method_err


def check_class_doc(module_tuple: Tuple[str, ast.Module]) -> Tuple[int, int]:
    """Check if classes in the given module have documentation.
    Class methods are also checked in the process.

    Args:
        module_tuple (Tuple[str, ast.Module]): Tuple of module name and
            the modules abstract syntax tree.

    Returns:
        Tuple[int, int]: Tuple of number if classes and methods without
            documentation.
    """
    module_name, module_node = module_tuple

    class_nodes = [
        node for node in module_node.body if type(node) is ast.ClassDef
    ]

    no_doc_num_class = 0
    no_doc_num_method = 0

    for class_node in class_nodes:
        if not ast.get_docstring(class_node):
            print_class_err(
                module_name, class_node.name, line=class_node.lineno
            )
            no_doc_num_class += 1

        no_doc_num_method += check_method_doc(class_node, module_name)

    return (no_doc_num_class, no_doc_num_method)


def check_method_doc(class_node: ast.ClassDef, module_name: str) -> int:
    """Check if methods in the given class have documentation.

    Args:
        class_node (ast.ClassDef): Class node to check its methods.
        module_name (str): Name of the module containing the class.

    Returns:
        int: Number of methods without documentation.
    """
    method_nodes = [
        node for node in class_node.body if type(node) is ast.FunctionDef
    ]

    no_doc_num = 0

    for method_node in method_nodes:
        if not ast.get_docstring(method_node):
            print_method_err(
                module_name,
                class_node.name,
                method_node.name,
                line=method_node.lineno,
            )
            no_doc_num += 1

    return no_doc_num
