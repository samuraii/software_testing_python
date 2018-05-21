def test_add_contact_to_group(app, orm):
    add_data = app.contact.add_to_group()
    contacts_in_group = orm.get_contacts_in_group(add_data['group_to_add'])
    assert add_data['added_contact'] in contacts_in_group
