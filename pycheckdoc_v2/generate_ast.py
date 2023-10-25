#!/usr/bin/env python3
"""Generate ASTs for the modules to be checked"""

import ast
import sys
from pathlib import Path
from pebble import ProcessPool  # type: ignore
from typing import List, Optional, Set, Tuple


def get_module_node(path: str) -> Optional[Tuple[str, ast.Module]]:
    """Read file at path and convert its source code
    into an ast. Generate the ast as a module node.

    Args:
        path (str): Path to the file to read.

    Returns:
        Tuple[str, ast.Module] | None: Tuple of the path and the
            ast module node if the file has content,
            else None if file is empty.
    """

    with open(path) as f:
        content = f.read()

    if content:
        return (path, ast.parse(content))

    return None


def validate_paths(paths: List[str], recursive: bool = False) -> Set[str]:
    """Validate given paths by checking if they exist.
    Also iterate over directories given so as to include .py files
    in them.

    All returned paths are absolute. This helps in removing
    duplicates and also help avoid any FileNotFoundError when reading
    the files.

    Args:
        paths (List[str]): List of paths to validate.

        recursive (Bool): Check directories recursively. Defaults to `False`.

    Returns:
        Set[str]: Set of valid paths. This includes the files
            from directories given.
    """
    valid_paths = []

    for path in paths:
        file_path = Path(path)

        if file_path.exists():
            if file_path.is_file() and file_path.suffix == ".py":
                valid_paths.append(str(file_path.absolute()))
            elif file_path.is_dir():
                if recursive:  # Get all .py files in all child directories.
                    files = file_path.glob("**/*.py")
                else:  # Get .py files in this directory only.
                    files = file_path.glob("*.py")

                # Add absolute paths of the files to avoid later inconveniences
                # when reading from the file.
                valid_paths.extend(
                    list(map(lambda x: str(x.absolute()), list(files)))
                )

    return set(valid_paths)  # Remove duplicates


def get_ast(
    paths: List[str], recursive: bool = False
) -> Optional[List[Tuple[str, ast.Module]]]:
    """Get the Abstract Syntax Trees(AST) of the modules pointed to
    by paths.

    Args:
        paths (List[str]): A list of file paths to get their ASTs.
            Relative paths are relative to the current working directory.
            Absolute paths can also be used.
            This list can include directories. If .py files are
            found in the directory they are checked instead.

        recursive (Bool): Check directories recursively. Defaults to `False`.

    Raises:
        TypeError: If paths is not a list this error is raised.

    Returns:
        List[Tuple[str, Module]] | None: List of tuples with format
            (path, ast.Module) if paths are provided and at least one is
            exists, else None is returned.
    """

    if type(paths) is not list:
        raise TypeError("Paths must be a list of strings")

    if len(paths) == 0:
        return None

    valid_paths = validate_paths(paths, recursive)

    if len(valid_paths) == 0:
        return None

    modules = []

    # Read the files and parse them concurrently.
    with ProcessPool() as pool:
        future = pool.map(get_module_node, valid_paths)
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

    modules = get_ast(sys.argv[1:])

    if modules:
        print(ast.dump(modules[0][1], indent=4))
