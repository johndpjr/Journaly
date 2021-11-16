import tkinter as tk
from tkinter import ttk

from entry import Entry


class EntryListFrame(tk.Frame):
    """Models the Entry List Frame that contains
    a list of past journal entries.
    """

    def __init__(self, parent, *args, **kwargs):
        # Initialize the frame
        super().__init__(parent, *args, **kwargs)
        self.controller = parent.controller

        # New entry button
        self.new_entry_bttn = ttk.Button(self,
                                         text='New entry',
                                         command=self._on_new_entry_bttn_click
        )
        self.new_entry_bttn.pack(side=tk.TOP, fill=tk.X)
    
    def _on_new_entry_bttn_click(self):
        """Handles the 'New entry' button click."""
        # Start controller reaction to command
        self.controller.new_entry()