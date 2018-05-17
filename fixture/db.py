import pymysql.cursors
from model.data import Group, Contact


class DbFixture:
    def __init__(self, host, db, user, password):
        self.connection = pymysql.connect(host=host, db=db, user=user, password=password, autocommit=True)
        self.connection.autocommit(True)

    def destroy(self):
        self.connection.close()

    def get_group_list(self):
        lst = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select group_id, group_name, group_header, group_footer from group_list')
            for row in cursor:
                (id, name, header, footer) = row
                lst.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return lst

    def get_contact_list(self):
        lst = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select id, firstname, lastname, nickname from addressbook where deprecated="0000-00-00 00:00:00"')
            for row in cursor:
                (id, firstname, lastname, nickname) = row
                lst.append(Contact(id=str(id), firstname=firstname, lastname=lastname, nickname=nickname))
        finally:
            cursor.close()
        return lst
