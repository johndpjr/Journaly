import tkinter as tk
from tkinter import ttk

from entry import Entry


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
            self.controller.entry_focus_in()
        
        def on_title_entry_focus_out(event):
            """Sets list item title and saves the journal entry
            to the database.
            """
            self.controller.entry_focus_out(self.title_entry.get())

        self.title_entry.bind('<FocusIn>', on_title_entry_focus_in)
        # Bind focus out to save journal entry
        self.title_entry.bind('<FocusOut>', on_title_entry_focus_out)

        def on_content_text_focus_out(event):
            """Saves the textbox content to the database."""
            self.controller.textbox_focus_out()
        
        self.content_text.bind('<FocusOut>', on_content_text_focus_out)
    
    def clear_entry(self):
        """Clears the current entry information."""
        # Clear title
        self.title_entry.delete(0, tk.END)
        # Clear content text
        self.content_text.delete(1.0, tk.END)
    
    def insert_entry(self, entry: Entry):
        """Inserts entry content into the frame."""
        # Insert title
        self.title_entry.insert(0, entry.title)
        # Set created date label
        self.date_created_lbl['text'] = entry.created_date
        # Insert content into text box
        self.content_text.insert(1.0, entry.content)

        # Focus on content text
        self.content_text.focus()
    
    def enable_entry_modification(self):
        """Enables the title entry and content text to be modified."""
        self.title_entry['state'] = tk.NORMAL
        self.content_text['state'] = tk.NORMAL
    
    def get_content(self):
        """Returns the content of the content_text."""
        return self.content_text.get(1.0, 'end-1c')