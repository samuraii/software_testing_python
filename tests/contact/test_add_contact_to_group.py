from model.data import Group
from model.data import Contact
import random


def test_add_contact_to_group(app, orm):
    # Получаем первичную информацию
    group_list = app.orm.get_group_list()
    contact_list = app.orm.get_contact_list()
    # Предусловия
    if len(group_list) == 0:
        app.group.create(Group(name='GroupToAddContqct', footer='Frooter', header='Header'))
        group_list = app.orm.get_group_list()
    if len(contact_list) == 0:
        app.contact.create_random_contact()
        contact_list = app.orm.get_contact_list()
    # Добавляем случайный контакт в случайную группу
    random_contact_index = random.randint(0, len(contact_list))
    random_group = group_list[random.randint(0, group_list)]
    app.contact.add_to_group(random_contact_index, random_group)
    # Проверяем наличие контакта в группе куда мы его добавляли
    contacts_in_group = orm.get_contacts_in_group(random_group)
    assert contact_list[random_contact_index] in contacts_in_group
