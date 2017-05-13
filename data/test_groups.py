import random
import string
from models.group import Group

utf_symbols = ''.join([chr(l) for l in range(1, 0x10ffff) if chr(l).isprintable()])
cyr_symbol = ''.join([chr(l) for l in range(0x0400, 0x04FF) if chr(l).isprintable()])
cyr_symbol_ru_uk = ''.join([chr(l) for l in range(0x0410, 0x0457) if chr(l).isprintable()])

def random_string(maxlen):
    lenght = random.randrange(maxlen)
    symbols = string.ascii_letters + string.digits + " "*10 # + string.punctuation
    return ''.join([random.choice(symbols) for _ in range(lenght)])

names = ['', 'fdd', '123']
headers = ['', 'fdd', '123']
footers = ['', 'fdd', '123']

test_groups = [
    Group(name_group=name, header_group=header, footer_group=footer)
    for name in names
    for header in headers
    for footer in footers
] + [
    Group(name_group=random_string(14), header_group=random_string(20), footer_group=random_string(50))
    for _ in range(5)
]
