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
                                     textvariable=parent.title_entry_var,
                                     state=tk.DISABLED
        )
        # Date created label
        self.date_created_lbl = tk.Label(self)

        # Pack both widgets
        self.title_entry.pack(side=tk.TOP, anchor=tk.W)
        self.date_created_lbl.pack(side=tk.TOP, anchor=tk.W)

        def on_title_entry_focus_out(event):
            """Saves the journal entry to the database."""
            print('Saving entry...')
            # Set button text to title_entry content
            parent.entry_list_frame.sel_bttn['textvariable'] = ''
            parent.entry_list_frame.sel_bttn['text'] = self.title_entry.get()
            # Write to database

        # TODO: Bind focus in to bind tk StringVar

        # Bind focus out to save journal entry
        self.title_entry.bind('<FocusOut>', on_title_entry_focus_out)