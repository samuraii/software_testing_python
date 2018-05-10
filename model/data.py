from sys import maxsize

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

    def __lt__(self, other):
        return self.id < other.id


class Contact:

    def __init__(
        self,
        firstname=None, 
        lastname=None,
        nickname=None,
        address=None,
        home_phone=None,
        mobile_phone=None,
        work_phone=None,
        secondary_phone=None,
        all_phones_from_home_page=None,
        email=None,
        email2=None,
        email3=None,
        all_emails_from_home_page=None,
        all_emails_from_view_page=None,
        id=None
    ):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.secondary_phone = secondary_phone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_emails_from_view_page = all_emails_from_view_page

    def __repr__(self):
        return "Contact({}, {}, {}, {}, {}, {})".format(
        self.id, 
        self.firstname, 
        self.lastname, 
        self.nickname,
        self.email, 
        self.home_phone
    )

    def __eq__(self, other):
        return self.id == other.id and self.firstname == other.firstname and self.lastname == other.lastname and self.nickname == other.nickname

    def __lt__(self, other):
        return self.id < other.id
    
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
