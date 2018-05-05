class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "Group({}, {}, {}, {})".format(self.id, self.name, self.header, self.footer)

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name


class Contact:

    def __init__(self, firstname=None, lastname=None, nickname=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.id = id

    def __repr__(self):
        return "Contact({}, {}, {}, {})".format(self.id, self.firstname, self.lastname, self.nickname)

    def __eq__(self, other):
        return self.id == other.id and self.firstname == other.firstname and self.lastname == other.lastname and self.nickname == other.nickname
