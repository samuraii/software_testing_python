import string
import random
from model.data import Group


testdata = [
    Group(name='groupname1', header='groupheader1', footer='groupfooter1'),
    Group(name='groupname2', header='groupheader2', footer='groupfooter2')
]


# def random_string(prefix, max_len):
#     symbols = string.ascii_letters + string.digits + " " * 10
#     return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(max_len))])
#
#
# testdata = [Group('', '', '')] + [
#     Group(name=random_string('name', 10), header=random_string('header', 10), footer=random_string('footer', 10))
#     for i in range(5)
# ]
