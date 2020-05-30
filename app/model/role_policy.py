from enum import Enum

class RolePolicy(Enum):
    OWNER = 1
    ADMIN = 2
    WRITE = 3
    READ = 4
