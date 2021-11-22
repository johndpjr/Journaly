from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from entry import Entry

import typing
if typing.TYPE_CHECKING:
    from app import App


class EntryFrame(tk.Frame):
    """Models the Entry Frame that contains
    the journal entry information.
    """

    def __init__(self, parent, *args, **kwargs):
        # Initialize the frame
        super().__init__(parent, *args, **kwargs)
        self.controller = parent.controller

        # Define widgets
        # Title entry
        self.title_entry = ttk.Entry(self,
                                     textvariable=self.controller.title_entry_var,
                                     font='Courier 14 bold',
                                     state=tk.DISABLED
        )
        # Date created label
        self.date_created_label = tk.Label(self, font='Courier 12')
        # Entry content text box
        self.content_text = tk.Text(self, wrap=tk.WORD,
                                    state=tk.DISABLED
        )

        # Pack all widgets
        self.title_entry.pack(side=tk.TOP, fill=tk.X, anchor=tk.NW)
        self.date_created_label.pack(side=tk.TOP, anchor=tk.NW)
        self.content_text.pack(side=tk.TOP, fill=tk.BOTH, anchor=tk.NW, expand=True)

        # Sets title_entry events and bindings.
        def on_title_entry_focus_in(event):
            """Sets the textvariable of the corresponding entry list item
            to what is currently in the title_entry entry box.
            """
            self.controller.entry_focus_in()
        
        def on_title_entry_focus_out(event):
            """Sets the entry's list item title and saves or updates
            the entry to the database.
            """
            self.controller.entry_focus_out(self.title_entry.get())

        self.title_entry.bind('<FocusIn>', on_title_entry_focus_in)
        self.title_entry.bind('<FocusOut>', on_title_entry_focus_out)

        # Sets content_text events and bindings.
        def on_content_text_focus_out(event):
            """Saves the content_text content to the database
            for the current entry.
            """
            self.controller.textbox_focus_out()
        
        self.content_text.bind('<FocusOut>', on_content_text_focus_out)
    
    def clear_entry(self):
        """Clears the title_entry and the content_text."""
        self.set_entry_modification_state(tk.NORMAL)
        self.title_entry.delete(0, tk.END)
        self.date_created_label['text'] = ''
        self.content_text.delete(1.0, tk.END)
    
    def insert_entry(self, entry: Entry):
        """Inserts entry content into the title_entry and content_text
        and sets the date_created_label to the entry's creation date."""
        # Insert title
        self.title_entry.insert(0, entry.title)
        # Set created date label
        self.date_created_label['text'] = entry.created_date
        # Insert content into text box
        self.content_text.insert(1.0, entry.content)

        # Focus on content text
        self.content_text.focus()
    
    def set_entry_modification_state(self, state):
        """Sets the state of the title_entry and content_text widgets."""
        self.title_entry['state'] = state
        self.content_text['state'] = state
    
    def get_content(self):
        """Returns the content of the content_text."""
        return self.content_text.get(1.0, 'end-1c')