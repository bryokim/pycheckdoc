from pycheckdoc.check_function import (
    check_function_doc,
    check_function_doc_single,
)


from . import no_doc, with_doc


def test_check_function_doc_with_doc():
    """
    GIVEN an imported module object with functions that all
        have documentation
    WHEN check_function_doc_single is called with the module as argument
    THEN 0 is returned from the function call.
    """
    status = check_function_doc_single(with_doc)

    assert status == 0


def test_check_function_doc_no_doc():
    """
    GIVEN an imported module object with functions missing documentation
    WHEN check_function_doc_single is called with the module as argument
    THEN number of functions missing documentation is returned.
    """
    status = check_function_doc_single(no_doc)

    assert status == 1


def test_check_function_doc_multiple():
    """
    GIVEN a list of imported module objects
    WHEN check_function_doc is called with the module as argument
    THEN 0 is returned if all functions in all modules have documentation
        else number of functions missing documentation is returned.
    """
    status = check_function_doc([with_doc, no_doc])

    assert status == 1
