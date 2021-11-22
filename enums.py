from enum import Enum


class DateFormat(Enum):
    """Models the date format for the database and user view."""
    DB = '%Y%m%d%H%M%S'
    USER = '%A %B %d, %Y (%I:%M:%S %p)'