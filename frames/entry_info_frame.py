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
        self.title_entry = ttk.Entry(self)
        # Date created label
        self.date_created_lbl = tk.Label(self)

        # Pack both widgets
        self.title_entry.pack(side=tk.TOP, anchor=tk.W)
        self.date_created_lbl.pack(side=tk.TOP, anchor=tk.W)