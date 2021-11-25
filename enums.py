from enum import Enum, auto


class DateFormat(Enum):
    """Models the date format for the database and user view."""
    DB = '%Y%m%d%H%M%S'
    USER = '%A %B %d, %Y (%I:%M:%S %p)'

class UpdateType(Enum):
    """Models the kind of database update that is used."""
    ALL = auto()
    TITLE = auto()
    CONTENT = auto()