import random
import string
from model.data import Contact


def random_string(prefix, max_len, spaces=5):
    symbols = string.ascii_letters + string.digits + " " * spaces
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(max_len))])


def random_phone(max_len):
    return '+' + ''.join([random.choice(string.digits) for i in range(random.randrange(6, max_len))])


testdata = [Contact(firstname='', lastname='')] + [
    Contact(
        firstname=random_string('firstname', 10),
        lastname=random_string('lastname', 15),
        nickname=random_string('nickname', 15),
        email=random_string('e', 10, 0) + '@mail.ru',
        home_phone=random_phone(8),
        mobile_phone=random_phone(8),
        secondary_phone=random_phone(8),
        work_phone=random_phone(8)
    )
    for i in range(5)
]