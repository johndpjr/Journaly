import tkinter as tk
from tkinter import ttk


class EntryFrame(tk.Frame):
    """Models the Entry Frame that contains
    the journal entry information.
    """

    def __init__(self, parent, *args, **kwargs):
        # Initialize the frame
        super().__init__(parent, *args, **kwargs)
        self.controller = parent.controller

        # Title entry
        self.title_entry = ttk.Entry(self,
                                     textvariable=self.controller.title_entry_var,
                                     state=tk.DISABLED
        )
        # Date created label
        self.date_created_lbl = tk.Label(self)
        # Entry content text box
        self.content_text = tk.Text(self, state=tk.DISABLED)

        # Pack all widgets
        self.title_entry.pack(side=tk.TOP, anchor=tk.W)
        self.date_created_lbl.pack(side=tk.TOP, anchor=tk.W)
        self.content_text.pack(fill=tk.BOTH, anchor=tk.W, expand=True)

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