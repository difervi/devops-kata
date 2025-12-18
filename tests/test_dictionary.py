from src.dictionary import Dictionary


def test_dictionary_found():
    d = Dictionary()
    d.newentry("Apple", "A fruit")
    assert d.look("Apple") == "A fruit"


def test_dictionary_not_found():
    d = Dictionary()
    assert d.look("Banana") == "Can't find entry for Banana"
