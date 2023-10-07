#!/usr/bin/env python3


from pycheckdoc.check_module import check_module_doc

from . import no_doc, with_doc


def test_check_module_doc_with_doc():
    """
    GIVEN an imported module object with documentation
    WHEN check_module_doc is called with the module as argument
    THEN 0 is returned from the function call.
    """
    status = check_module_doc(with_doc)

    assert status == 0


def test_check_module_doc_no_doc():
    """
    GIVEN an imported module object without documentation
    WHEN check_module_doc is called with the module as argument
    THEN 1 is returned from the function call.
    """
    status = check_module_doc(no_doc)

    assert status == 1


def test_check_module_doc_string_arg():
    """
    GIVEN a string object
    WHEN check_module_doc is called with the string as argument
    THEN 0 is returned from the function call.
    """
    status = check_module_doc("module")

    assert status == 0


def test_check_module_doc_int_arg():
    """
    GIVEN an integer object
    WHEN check_module_doc is called with the integer as argument
    THEN 0 is returned from the function call.
    """
    status = check_module_doc(2)

    assert status == 0


def test_check_module_doc_class_arg():
    """
    GIVEN a class object
    WHEN check_module_doc is called with the class as argument
    THEN 0 is returned from the function call if the class has
        documentation and 1 if it doesn't.
    """

    WithDoc_status = check_module_doc(with_doc.WithDoc)
    assert WithDoc_status == 0

    NoDoc_status = check_module_doc(no_doc.NoDoc)
    assert NoDoc_status == 1
