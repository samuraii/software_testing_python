import pytest
from model.data import Contact
from data.add_contact import testdata

@pytest.mark.parametrize('contact', testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    before = app.contact.get_contact_list()
    app.contact.create(contact)
    assert app.contact.count() - 1 == len(before)
    after = app.contact.get_contact_list()
    assert sorted(before, key=Contact.id_or_max) != sorted(after, key=Contact.id_or_max)
