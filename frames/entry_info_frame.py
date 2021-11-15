import tkinter as tk
from tkinter import ttk


class EntryInfoFrame(tk.Frame):
    """Models the Entry Info Frame that contains
    the journal entry information.
    """

    def __init__(self, parent, *args, **kwargs):
        # Initialize the frame
        super().__init__(parent, *args, **kwargs)

        # Title entry
        self.title_entry = ttk.Entry(self,
                                     textvariable=parent.controller.title_entry_var,
                                     state=tk.DISABLED
        )
        # Date created label
        self.date_created_lbl = tk.Label(self)

        # Pack both widgets
        self.title_entry.pack(side=tk.TOP, anchor=tk.W)
        self.date_created_lbl.pack(side=tk.TOP, anchor=tk.W)

        def on_title_entry_focus_in(event):
            parent.controller.entry_focus_in()
        
        def on_title_entry_focus_out(event):
            """Sets list item title and saves the journal entry
            to the database.
            """
            parent.controller.entry_focus_out(self.title_entry.get())

        # TODO: Bind focus in to bind tk StringVar
        self.title_entry.bind('<FocusIn>', on_title_entry_focus_in)
        # Bind focus out to save journal entry
        self.title_entry.bind('<FocusOut>', on_title_entry_focus_out)