# pycheckdoc (v1)

This version of pycheckdoc imports modules to be checked and uses
[inspect](<https://docs.python.org/3/library/inspect.html>) to get different members and check for their documentation.

The members checked are functions, classes and methods. The module
documentation is also checked.

## Installation

Clone [this](<https://github.com/bryokim/pycheckdoc>) repository.

```Bash
cd pycheckdoc
```

Install required packages in requirements.txt.

```Bash
pip install -r requirements.txt
```

Change [pycheckdoc](../bin/pycheckdoc) binary to load this module instead of v2. It's supposed to look as below.

```Python
#!/usr/bin/env python3

# Uncomment this
from pycheckdoc.check_doc import main

# Comment this
# from pycheckdoc_v2.main import main

main()
```

> You can checkout [pycheckdoc_v2](../pycheckdoc_v2/).

Edit the `setup.py` file as you see fit. You can use it as is
and will build the package accordingly.

Build the package.

```Bash
python setup.py sdist bdist_wheel
```

Install the `pycheckdoc` package that has been built.

```Bash
pip install .
```

An executable, `pycheckdoc`, is installed in the path so that the
module can be called from the terminal.

## Usage

### From the terminal

`pycheckdoc` can be called from the terminal as shown below.

```Bash
pycheckdoc [filename]
```

### Import to a file

You can import `pycheckdoc` into a file and use its different
methods to check documentation.

```Python
import pycheckdoc

import math

pycheckdoc.check_module_doc(math) # Print error if module isn't documented, otherwise nothing happens
```

## More Docs

### Getting members

Example of how members are gotten. This is a snippet from [check_class.py](check_class.py).

```Python
# check_class.py

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
        if _class.__module__ == module.__name__ # Ensure it's not an imported class.
    ]

    return classes
```

### Importing modules

Since modules being checked are imported, they need to contain `if __name__ == "__main__":`
guard to prevent them from being executed.

To prevent any module without the guard from being executed for long, a check is done
on every import to ensure that the importation does not last for more than a second.

```Python
# import_modules.py

@concurrent.process(timeout=1)
def validate_import(basename: str) -> Optional[bool]:
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
```

Any modules that exceed this threshold are not
imported and therefore not checked and an error message is printed with the filename and
reason.

```Python
# import_modules.py

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
```
