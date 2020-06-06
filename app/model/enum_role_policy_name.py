from enum import Enum


class EnumRolePolicyName(Enum):
    OWNER = 'owner'
    ADMIN = 'admin'
    WRITE = 'write'
    READ = 'read'
