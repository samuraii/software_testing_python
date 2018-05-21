def test_remove_contact_from_group(app, orm):
    groups = orm.get_group_list()
    # добавляем контакт в группу, чтобы такая точно была
    app.contact.add_to_group()
    # находим группу в которой есть контакты
    for i in range(len(groups)):
        contacts_in_group = orm.get_contacts_in_group(groups[i])
        if len(contacts_in_group) > 0:
            target_group = groups[i]
            break
    # удаляем контакт из целевой группы и проверяем его отсуствие
    deleted_contact = app.contact.remove_contact_from_group(target_group)
    contacts_in_group = orm.get_contacts_in_group(target_group)
    assert deleted_contact not in contacts_in_group
