"""Functions for printing results of the checks"""

import sys
from typing import Optional


def print_module_success(module_name: str, msg: Optional[str] = None) -> None:
    """Print success from the module checks.

    Args:
        module_name (str): Name of the module.
        msg (str | None, optional): Message to print. Defaults to None.
    """

    if msg:
        ending = " "
    else:
        ending = "\n"

    print("\t", end="")
    print("\033[1;32;40m module_suc \033[0m ->", end=" ")
    print(f"\033[5;32m{module_name}.py \033[0m", end=ending)

    if msg:
        print(f"\033[0;32m : {msg}\033[0m")


def print_module_err(
    module_name: str, err: Optional[str] = None, line: int = 0
) -> None:
    """Print error from the module checks.

    Args:
        module_name (str): Name of the module where there's an error.
        err (str | None, optional): Error that occurred. Defaults to `None`.
        line (int | None, optional): Line number of the module. Defaults to 0.
    """

    if err:
        ending = ""
    else:
        ending = "\n"

    print(
        f"\033[1;33m{module_name}.py:",
        end="",
        file=sys.stderr,
    )

    if line == 0:
        print(f" {line}:", end="", file=sys.stderr)

    print(
        "\033[1;31m module_err \033[0m",
        end=ending,
        file=sys.stderr,
    )

    if err:
        print(
            f"\033[1;31m: {err}\033[0m",
            file=sys.stderr,
        )


def print_function_success(
    module_name: str, func_name: str, msg: Optional[str] = None
) -> None:
    """Print success from the function checks.

    Args:
        module_name (str): Name of the module.
        func_name (str): Name of the function.
        msg (str | None, optional): Message to print. Defaults to None.
    """

    if msg:
        ending = " "
    else:
        ending = "\n"

    print("\t", end="")
    print("\033[1;32;40m func_suc \033[0m ->", end=" ")
    print(f"\033[5;32m{module_name}.py : {func_name} \033[0m", end=ending)

    if msg:
        print(f"\033[0;32m : {msg}\033[0m")


def print_function_err(
    module_name: str, func_name: str, err: Optional[str] = None, line: int = 0
) -> None:
    """Print error from the function checks.

    Args:
        module_name (str): Name of the module where function exists.
        func_name (str): Name of the function with the error.
        err (str | None, optional): Error that occurred. Defaults to `None`.
        line (int | None, optional): Line number where the function has been
            declared in the source file. Defaults to 0.
    """

    if err:
        ending = ""
    else:
        ending = "\n"

    print(
        f"\033[1;33m{module_name}.py:",
        end="",
        file=sys.stderr,
    )

    if line != 0:
        print(f" {line}:", end="", file=sys.stderr)

    print(
        f"\033[1;31m func_err: \033[1;37m{func_name}\033[0m",
        end=ending,
        file=sys.stderr,
    )

    if err:
        print(
            f"\033[1;31m: {err}\033[0m",
            file=sys.stderr,
        )


def print_class_err(
    module_name: str, class_name: str, err: Optional[str] = None, line: int = 0
) -> None:
    """Print error from the class checks.

    Args:
        module_name (str): Name of the module where the class exists.
        class_name (str): Name of the class being checked.
        err (str | None, optional): Error message to print. Defaults to None.
        line (int, optional): Line number where the class has been declared
            in the source file. Defaults to 0.
    """
    if err:
        ending = ""
    else:
        ending = "\n"

    print(
        f"\033[1;33m{module_name}.py:",
        end="",
        file=sys.stderr,
    )

    if line != 0:
        print(f" {line}:", end="", file=sys.stderr)

    print(
        f"\033[1;31m class_err: \033[1;37m{class_name}\033[0m",
        end=ending,
        file=sys.stderr,
    )

    if err:
        print(
            f"\033[1;31m: {err}\033[0m",
            file=sys.stderr,
        )


def print_method_err(
    module_name: str,
    class_name: str,
    method_name: str,
    err: Optional[str] = None,
    line: int = 0,
) -> None:
    """Print error from the method checks.

    Args:
        module_name (str): Name of the module where the method exists.
        class_name (str): Name of the class where method exists.
        method_name (str): Name of the method being checked.
        err (str | None, optional): Error message to print. Defaults to None.
        line (int, optional): Line number where the method is found in the
            source file. Defaults to 0.
    """
    if err:
        ending = ""
    else:
        ending = "\n"

    print(
        f"\033[1;33m{module_name}.py:",
        end="",
        file=sys.stderr,
    )

    if line != 0:
        print(f" {line}:", end="", file=sys.stderr)

    print(
        f"\033[1;31m method_err: \033[1;37m{class_name}: {method_name}\033[0m",
        end=ending,
        file=sys.stderr,
    )

    if err:
        print(
            f"\033[1;31m: {err}\033[0m",
            file=sys.stderr,
        )


def print_error(error_count: int, error_files: int, num_modules: int) -> None:
    """Print error message if some documentation is missing.

    Args:
        error_count (int): Number of errors that were found.
        error_files (int): Number of files that have errors.
        num_modules (int): Number of modules checked.
    """

    error_str = (
        f"Found {error_count} error in {error_files} source file "
        + f"(checked {num_modules} source file)"
    )

    if error_count > 1:
        error_str = (
            error_str[: error_str.find("error") + 5]
            + "s"
            + error_str[error_str.find("error") + 5:]
        )

    if error_files > 1:
        error_str = (
            error_str[: error_str.find("file") + 4]
            + "s"
            + error_str[error_str.find("file") + 4:]
        )

    if num_modules > 1:
        error_str = (
            error_str[: error_str.rfind("file") + 4]
            + "s"
            + error_str[error_str.rfind("file") + 4:]
        )

    print(f"\033[1;31m{error_str}", file=sys.stderr)


def print_success(num_modules: int) -> None:
    """Print success message when all documentation
    is present.

    Args:
        num_modules (int): Number of modules checked.
    """

    print(
        f"\033[1;32mSuccess: no issues found in {num_modules} source file",
        end="",
    )

    if num_modules > 1:
        print("s\033[0m")
    else:
        print("\033[0m")
