from enum import IntEnum


class EnumRolePolicy(IntEnum):
    OWNER = 1
    ADMIN = 2
    WRITE = 3
    READ = 4
  