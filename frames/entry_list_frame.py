from __future__ import annotations

import tkinter as tk
from tkinter import ttk

import typing
if typing.TYPE_CHECKING:
    from app import App


class EntryListFrame(tk.Frame):
    """Models the Entry List Frame that contains
    a list of past journal entries.
    """

    def __init__(self, parent: App, *args, **kwargs):
        # Initialize the frame
        super().__init__(parent, *args, **kwargs)
        self.controller = parent.controller

        # Search box entry
        self.search_box_entry = ttk.Entry(self)
        # Search button
        self.search_bttn = ttk.Button(self,
                                      text='Search',
                                      command=self._on_search_bttn_click
        )
        # Pack both widgets
        self.search_box_entry.grid(row=0, column=0, sticky=tk.EW)
        self.search_bttn.grid(row=0, column=1, sticky=tk.EW)
    

        # New entry button
        self.new_entry_bttn = ttk.Button(self,
                                         text='New entry',
                                         command=self._on_new_entry_bttn_click
        )
        self.new_entry_bttn.grid(row=1, column=0, columnspan=2,
                                 pady=(10, 5), sticky=tk.EW
        )

        self.grid_columnconfigure(0, weight=1)
    
    def _on_search_bttn_click(self):
        """Handles the 'Search' button click."""
        pass

    def _on_new_entry_bttn_click(self):
        """Handles the 'New entry' button click."""
        # Start controller reaction to command
        self.controller.new_entry()