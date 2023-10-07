#!/usr/bin/env python3
"""Check documentation on functions"""

import inspect
from types import ModuleType, FunctionType
from typing import List

from pycheckdoc.print_funcs import print_function_err, print_function_success


def get_functions(module: ModuleType) -> List[FunctionType]:
    """Get functions from the given module.

    Args:
        module (ModuleType): Module to get its functions.

    Returns:
        List[FunctionType]: List of functions in the module
    """
    functions = [
        func
        for _, func in inspect.getmembers(module, inspect.isfunction)
        if func.__module__ == module.__name__
    ]

    return functions


def check_function_doc_single(module: ModuleType) -> int:
    """Check if functions in the given module have documentation.

    Args:
        module (ModuleType): Module to check its functions.

    Returns:
        int: 0 if all functions have documentation,
            number of errors if otherwise.
    """
    funcs = get_functions(module)

    success: int = 0

    for func in funcs:
        if not func.__doc__:
            print_function_err(
                module.__name__,
                func.__name__,
                line=inspect.getsourcelines(func)[1],
            )
            success += 1
        else:
            # print_function_success(module.__name__, func.__name__)
            pass

    return success


def check_function_doc(modules: List[ModuleType]) -> int:
    """Check if functions in the given modules have documentation.

    Args:
        modules (List[ModuleType]): List of modules to check their functions.

    Returns:
        int: 0 if all functions have documentation,
            number of errors if otherwise.
    """
    mod_funcs = [(mod.__name__, get_functions(mod)) for mod in modules]

    success: int = 0

    for mod_func in mod_funcs:
        module_name = mod_func[0]
        for func in mod_func[1]:
            if not func.__doc__:
                print_function_err(
                    module_name,
                    func.__name__,
                    line=inspect.getsourcelines(func)[1],
                )
                success += 1
            else:
                # print_function_success(module_name, func.__name__)
                pass

    return success


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("Nope")
        sys.exit()

    from import_modules import import_modules

    modules = import_modules()
    module = modules[0]

    check_function_doc(modules)
    check_function_doc_single(module)
