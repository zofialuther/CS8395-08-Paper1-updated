from enum import Enum

class Contact(Enum):
    FIRST_NAME = 1
    LAST_NAME = 2
    PHONE = 3

print(Contact.__members__)  # mappingproxy(OrderedDict([('FIRST_NAME', <Contact.FIRST_NAME: 1>), ('LAST_NAME', <Contact.LAST_NAME: 2>), ('PHONE', <Contact.PHONE: 3>)]))