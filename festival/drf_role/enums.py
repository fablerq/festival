from enum import Enum


class PermissionEnum(Enum):
    READ = 0
    WRITE = 1
    NO_ACCESS = 2


class RoleEnum(Enum):
    Unknown = 0
    Admin = 1
    Moderator = 2
    Shipowner = 3
    Captain = 4
    Sailor = 5
    Organizer = 6
    Assistant = 7
