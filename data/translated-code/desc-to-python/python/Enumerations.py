from enum import Enum

class Contact(Enum):
    FIRST_NAME = 1
    LAST_NAME = 2
    PHONE = 3

Contact2 = Enum('Contact2', 'FIRST_NAME LAST_NAME PHONE')

print(Contact.__members__)
print(Contact2.__members__)