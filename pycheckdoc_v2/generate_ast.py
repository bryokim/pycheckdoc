#!/usr/bin/env python3
"""Generate ASTs for the modules to be checked"""

import ast
import sys
from pebble import ProcessPool  # type: ignore
from typing import List, Optional, Tuple


def get_module_node(filename: str) -> Optional[Tuple[str, ast.Module]]:
    """Read file with name filename and convert its source code
    into an ast. Generate the ast as a module node.

    Args:
        filename (str): Name of the file to read.

    Returns:
        Tuple[str, ast.Module] | None: Tuple of the filename and the
            ast module node if the file has content,
            else None if file is empty.
    """

    with open(filename) as f:
        content = f.read()

    if content:
        return (filename, ast.parse(content))

    return None


def get_ast() -> List[Tuple]:
    """Get the Abstract Syntax Trees(AST) of the modules given as
    arguments.

    Returns:
        List[Tuple]: List of tuples with format (filename, ast.Module)
    """

    modules = []

    # Read the files and parse them concurrently.
    with ProcessPool() as pool:
        future = pool.map(get_module_node, sys.argv[1:])

        try:
            for module in future.result():
                if module:
                    modules.append(module)
        except Exception as e:
            print(e)

    return modules


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No arg")
        sys.exit(1)

    modules = get_ast()
    print(ast.dump(modules[0][1], indent=4))
