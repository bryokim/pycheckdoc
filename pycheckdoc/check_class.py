#!/usr/bin/env python3
"""Check documentation on classes and their methods"""

import inspect
from types import ModuleType, FunctionType
from typing import Any, Type, List, Tuple

from pycheckdoc.print_funcs import print_class_err, print_method_err


def get_classes(module: ModuleType) -> List[Any]:
    """Get classes from the given module.

    Args:
        module (ModuleType): Module to get its classes.

    Returns:
        list[Any]: A list of classes from the module.
    """
    classes = [
        _class
        for _, _class in inspect.getmembers(module, inspect.isclass)
        if _class.__module__ == module.__name__
    ]

    return classes


def get_methods(_class: Type) -> List[FunctionType]:
    """Geth methods in the given class.

    Args:
        _class (Type): Class to get its methods.

    Returns:
        list[FunctionType]: A list of methods from the class.
    """
    methods = [
        method
        for _, method in inspect.getmembers(_class, inspect.isfunction)
        if method.__module__ == _class.__module__
    ]

    return methods


def check_method_doc(_class: Type) -> int:
    """Check if methods in the given class have documentation.

    Args:
        _class (Type): Class to check its methods.

    Returns:
        int: 0 if all the methods have documentation else,
            number of methods without documentation.
    """
    methods = get_methods(_class)

    success: int = 0

    for method in methods:
        if not method.__doc__:
            print_method_err(
                method.__module__,
                _class.__name__,
                method.__name__,
                line=(inspect.getsourcelines(method)[1]),
            )
            success += 1

    return success


def check_class_doc(module: ModuleType) -> Tuple[int, int]:
    """Check if classes in the given module have documentation.
    Args:
        module (ModuleType): Module to check its classes.

    Returns:
        tuple: A tuple of the number of classes and methods
            without documentation.
    """
    classes = get_classes(module)

    class_success: int = 0
    method_success: int = 0

    for _class in classes:
        if not _class.__doc__:
            print_class_err(
                module.__name__,
                _class.__name__,
                line=inspect.getsourcelines(_class)[1],
            )
            class_success += 1

        method_success += check_method_doc(_class)

    return (class_success, method_success)


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("Nope")
        sys.exit()

    from import_modules import import_modules

    module = import_modules()[0]

    print(get_classes(module))
    print(check_class_doc(module))
