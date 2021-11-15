import tkinter as tk
from tkinter import ttk

from datetime import datetime


class EntryListFrame(tk.Frame):
    """Models the Entry List Frame that contains
    a list of past journal entries.
    """

    def __init__(self, parent, *args, **kwargs):
        # Initialize the frame
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        # New entry button
        self.new_entry_bttn = ttk.Button(self,
                                         text='New entry',
                                         command=self._on_new_entry_bttn_click
        )
        self.new_entry_bttn.pack(side=tk.TOP, fill=tk.X)

        self.sel_bttn = None
    
    def _on_new_entry_bttn_click(self):
        # Enable modification of entry title and content
        self.parent.entry_info_frame.title_entry['state'] = tk.NORMAL
        self.parent.entry_content_frame.entry_content_text['state'] = tk.NORMAL
        # Set the datetime of the date created label
        self.parent.entry_info_frame.date_created_lbl['text'] = datetime.now().strftime('%c')
        # Focus on entry title
        self.parent.entry_info_frame.title_entry.focus()
        # Create new list item
        self.sel_bttn = ttk.Button(self, textvariable=self.parent.title_entry_var)
        self.sel_bttn.pack(side=tk.TOP, fill=tk.X)
        # TODO: write entry to database