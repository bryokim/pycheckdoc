# pycheckdoc

Check that all modules, classes, functions and methods have
documentation.

## Installation

Clone [this](<https://github.com/bryokim/pycheckdoc>) repository.

```Bash
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
