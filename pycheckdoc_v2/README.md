# pycheckdoc_v2

This version of pycheckdoc uses [Abstract Syntax Trees (ASTs)](<https://docs.python.org/3/library/ast.html>)
to check the modules for documentation.

## Installation

Clone [this](<https://github.com/bryokim/pycheckdoc>) repository.

```Bash
git clone https://github.com/bryokim/pycheckdoc.git

cd pycheckdoc
```

Install required packages in requirements.txt.

```Bash
pip install -r requirements.txt
```

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

`pycheckdoc` can be called from the terminal with options as shown below.

```Bash
pycheckdoc [-h] [-r] [--no-print] [paths ...]
```

`paths` is a positional argument for paths to files / directories to
be checked.

| Option | Description | Default value |
|-- | -- | --|
| `-h`, `--help` | Show help message | |
| `-r`, `--recursive` | Recursively check directories. | `False` |
| `--no-print` | Don't print error and success messages. | `False` |

To recursively check the current directory and not print any output, though not useful, you can use the command below.

```Bash
pycheckdoc -r --no-print .
```

You can also provide several directories or files to check.

```Bash
pycheckdoc -r dir/ dir2/ ../filename
```

### Import to a file

You can import `pycheckdoc_v2` into a file and use its different
methods to check documentation.

The [main.py](main.py) file includes `check_doc` function that can be
imported and used to check files.

```Python

from pycheckdoc_v2.main import check_doc

total_errors, files_with_errors = check_doc(["."], recursive=True, print_msgs=False)

print(total_errors, files_with_errors)  # 0 0

```

Disabling error and success messages is crucial if imported, therefore `check_doc`
function sets print_msgs to `False` by default.

## More Docs

### Generating ASTs

Generation of the ASTs of modules provided is done concurrently in a `ProcessPool`
from the [Pebble](<https://pebble.readthedocs.io/en/latest/>) module. This helps
read the files faster and generate the ASTs much quicker.

```Python
# generate_ast.py

def get_module_node(path: str) -> Optional[Tuple[str, ast.Module]]:
    with open(path) as f:
        content = f.read()

    if content:
        return (path, ast.parse(content))

    return None

def get_ast(paths: List[str], recursive: bool = False) -> Optional[List[Tuple[str, ast.Module]]]:
    # Some code here ...

    with ProcessPool() as pool:
        future = pool.map(get_module_node, valid_paths)
        try:
            for module in future.result():
                if module:
                    modules.append(module)
        except Exception as e:
            print(e)

    # Some code here ...
```

:art:
