import string
import random
import os.path
import jsonpickle
import getopt
import sys
from model.data import Group

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["num of groups", "file name"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f_name = 'data/groups.json'

for opt, val in opts:
    if opt == '-n':
        n = int(val)
    elif opt == '-f':
        f = val


def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(max_len))])


testdata = [Group('', '', '')] + [
    Group(name=random_string('name', 10), header=random_string('header', 10), footer=random_string('footer', 10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f_name)

with open(file, 'w') as f:
    jsonpickle.set_encoder_options('json', indent=2)
    f.write(jsonpickle.encode(testdata))
