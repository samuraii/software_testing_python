import random
from model.data import Group

def test_edit_group_data(app):
    app.session.login('admin', 'secret')
    name  = random.randint(1, 100)
    app.group.edit_data(Group(name=name, header='New', footer='FooterNew'))
    app.session.logout()