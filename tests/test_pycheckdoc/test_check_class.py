from pycheckdoc.check_class import check_class_doc, check_method_doc

from . import no_doc, with_doc


def test_check_class_doc_with_doc():
    class_status, method_status = check_class_doc(with_doc)

    assert class_status == 0
    assert method_status == 0


def test_check_class_doc_no_doc():
    class_status, method_status = check_class_doc(no_doc)

    assert class_status == 1
    assert method_status == 2


def test_check_method_doc_with_doc():
    status = check_method_doc(with_doc.WithDoc)

    assert status == 0


def test_check_method_doc_no_doc():
    status = check_method_doc(no_doc.NoDoc)

    assert status == 2
