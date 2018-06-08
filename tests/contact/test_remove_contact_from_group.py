from model.data import Group
import random


def test_remove_contact_from_group(app, orm):
    group_list = orm.get_group_list()
    # Предусловие
    if len(group_list) == 0:
        app.group.create(Group(name='GroupToRmContqct', footer='Frooter', header='Header'))
        group_list = app.orm.get_group_list()
    # Ищем группу в которой есть контакты, либо делаем такую
    for i in range(len(group_list)):
        contacts_in_group = orm.get_contacts_in_group(group_list[i])
        if len(contacts_in_group) > 0:
            target_group = group_list[i]
            break
        else:
            # Нужно добавить в группу контакт
            contact_list_raw = orm.get_contact_list()
            contact_list = orm.convert_contacts_to_model(contact_list_raw)
            # Проверяем что есть контакт для добавления иначе создаем
            if len(contact_list) == 0:
                app.contact.create_random_contact()
                contact_list = orm.get_contact_list()
            # Добавляем случайный контакт в случайную группу
            random_contact_index = random.randint(0, len(contact_list))
            random_group = group_list[random.randint(0, group_list)]
            app.contact.add_to_group(random_contact_index, random_group)
    random_group = random.choice(group_list)
    removed_contact = app.contact.remove_contact_from_group(random_group)
    assert removed_contact in orm.get_contacts_not_in_group(random_group)
