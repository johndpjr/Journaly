import tkinter as tk


class Entry:
    """Models a journal entry."""

    def __init__(self, uid=None, title=None,
                 content='', created_date=None,
                 bttn=None, del_bttn=None,
                 persistent=False):
        self.uid = uid
        self.title = title
        self.content = content
        self.created_date = created_date
        self.bttn = bttn
        self.del_bttn = del_bttn
        self.persistent = persistent