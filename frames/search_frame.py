import tkinter as tk
from tkinter import ttk


class SearchFrame(tk.Frame):
    """Models the Search Frame that contains
    a search box to search past journal entries.
    """

    def __init__(self, parent, *args, **kwargs):
        # Initialize the frame
        super().__init__(parent, *args, **kwargs)

        # Search box entry
        self.search_box_entry = ttk.Entry(self)
        # Search button
        self.search_bttn = ttk.Button(self,
                                      text='Search',
                                      command=self._on_search_bttn_click
        )
        # Pack both widgets
        self.search_box_entry.pack(side=tk.LEFT)
        self.search_bttn.pack(side=tk.LEFT)
    
    def _on_search_bttn_click(self):
        pass