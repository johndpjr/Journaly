import tkinter as tk

import uuid


class Entry:
    """Models a journal entry."""

    def __init__(self, title=None,
                 content='', created_date=None,
                 bttn=None):
        self.id = str(uuid.uuid4()).replace('-', '')
        self.title = title
        self.content = content
        self.created_date = created_date
        self.bttn = bttn