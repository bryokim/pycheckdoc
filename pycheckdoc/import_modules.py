#!/usr/bin/env python3
"""Imports all the modules to be checked"""

import os
import sys

from concurrent.futures import TimeoutError
from pathlib import Path
from pebble import concurrent, common
from typing import List, TextIO
from types import ModuleType


# Add path where script is being run to path
# so as to enable importation of modules.
sys.path.append(str(Path.cwd()))
sys.path.append(str(Path.cwd().parent))
sys.path.append(str(Path.cwd().parent.parent))


@concurrent.process(timeout=1)
def validate_import(basename: str) -> bool | None:
    """Validate that the import can be done within
    a second. If not, then the file is being executed
    during importation and takes too long.

    This is just a check for whether the module being
    imported has `if __name__ == "__main__"` directive
    that prevents its execution when imported.

    Args:
        basename (str): Name of the file being imported
            without the .py suffix.

    Raises:
        TimeoutError: If the importation takes more than 1 second,
            this error is raised.

    Returns:
        bool|None: Return True if import can be done in under 1
            second, else a timeout occurs and `TimeoutError` is raised.
    """
    __import__(basename)

    return True


def get_modules(stderr: TextIO) -> list[ModuleType]:
    """Import valid modules.

    Args:
        stderr (TextIO): Stream to write errors.

    Returns:
        List[ModuleType]: List of imported modules.
    """
    modules = []

    for file in sys.argv[1:]:
        basename = Path(file).stem

        future = validate_import(basename)

        try:
            if future.result():
                modules.append(__import__(basename))
        except TimeoutError:
            print(
                f"\033[1;31m ERROR: \033[1;37m{basename}.py: \033[0m"
                + "Took long to import. Check if file has "
                + "\033[1;37m`if __name__ == '__main__':`\033[0m guard set.",
                file=stderr,
            )
        except common.ProcessExpired as error:
            # print("%s. Exit code: %d" % (error, error.exitcode), file=stderr)
            pass
        except Exception as e:
            print(f"\033[1;37m{basename}.py: \033[0m{e}", file=stderr)

    return modules


def import_modules() -> List[ModuleType]:
    """Import passed modules that need to be checked.

    Returns:
        List[ModuleType]: List of imported modules.
    """

    # Save initial stdout and stderr.
    stdout_sv = sys.stdout
    stderr_sv = sys.stderr

    # Create file stream to use in place of stdout and stderr
    # during importation.
    fout = open("import_output.now", "w")
    sys.stdout = fout
    sys.stderr = fout

    modules = get_modules(stderr=stderr_sv)

    # Restore default stdout and stderr
    sys.stdout = stdout_sv
    sys.stderr = stderr_sv

    # Close the file stream and delete the file if it is created.
    fout.close()
    if Path.exists(Path("import_output.now")):
        os.remove("import_output.now")

    return modules


# Import modules
# modules = import_modules()
# print(modules)
