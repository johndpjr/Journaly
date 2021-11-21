import tkinter as tk


class Entry:
    """Models a journal entry."""

    def __init__(self, controller, uid=None, title=None,
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

        self.bttn['command'] = lambda e=self: controller.open_entry(e)
        self.del_bttn['command'] = lambda e=self: controller.delete_entry(e)
    
    def remove_from_view(self):
        self.bttn.destroy()
        self.del_bttn.destroy()