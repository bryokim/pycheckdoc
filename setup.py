from setuptools import setup, find_packages

VERSION = "2.1.0"
DESCRIPTION = (
    "Check documentation is present on module, class, function and methods."
)

# Setting up
setup(
    # the name must match the folder name 'pycheckdoc'
    name="pycheckdoc",
    version=VERSION,
    author="Brian Kimathi",
    author_email="<bryo.kim1@gmail.com>",
    description=DESCRIPTION,
    # long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=["python", "documentation"],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],

    scripts=['bin/pycheckdoc']
)
