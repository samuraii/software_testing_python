import string
import random
import os.path
import jsonpickle
import getopt
import sys
from model.data import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["num of groups", "file name"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f_name = 'data/contacts.json'

for opt, val in opts:
    if opt == '-n':
        n = int(val)
    elif opt == '-f':
        f = val


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

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f_name)

with open(file, 'w') as f:
    jsonpickle.set_encoder_options('json', indent=2)
    f.write(jsonpickle.encode(testdata))