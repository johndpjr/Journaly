import tkinter as tk
from tkinter import ttk

from datetime import datetime

from database.database import Database
from entry import Entry


class Controller:
    """Accepts input and handles it."""
    
    def __init__(self, parent):
        self.parent = parent

        # "Global" variables
        self.title_entry_var = tk.StringVar()

        self.db = Database()
        self.curr_entry = None
        self.entries = {}  # contains active Entry objects
    
    def add_frames(self):
        # Frames
        self.search_frame = self.parent.search_frame
        self.entry_list_frame = self.parent.entry_list_frame
        self.entry_frame = self.parent.entry_frame
    
    def on_startup(self):
        """Executes the startup flow for the application."""
        for entry in self.db.getall_entries():
            # Create new list item
            bttn = ttk.Button(self.entry_list_frame)
            bttn.pack(side=tk.TOP, fill=tk.X)
            # Create entry object and update the dictionary
            e = Entry(uid=entry[0], title=entry[1], created_date=entry[2], content=entry[3], bttn=bttn)
            self.entries.update({e.uid: e})
            bttn['text'] = e.title
            # Set the button's command to open the entry
            bttn['command'] = lambda e=e: self.open_entry(e)
            print(entry)
    
    def clear_entry(self):
        """Clears the current entry information."""
        # Erase title
        self.entry_frame.title_entry.delete(0, tk.END)
        # Erase content text box
        self.entry_frame.content_text.delete(1.0, tk.END)
    
    def open_entry(self, entry):
        # Save the current entry
        if self.curr_entry is None:
            self._enable_content_modification()
            self.curr_entry = entry

        self.curr_entry.bttn['textvariable'] = ''
        self.curr_entry.content = self.entry_frame.content_text.get(1.0, 'end-1c')
        # Clear title entry and content text box
        self.clear_entry()
        # Insert title
        self.entry_frame.title_entry.insert(0, entry.title)
        # Set created date label
        self.entry_frame.date_created_lbl['text'] = entry.created_date
        # Insert entry content to text box
        self.entry_frame.content_text.insert(1.0, entry.content)
        # Focus on end of text box
        self.entry_frame.content_text.focus()
        self.curr_entry = entry
    
    def new_entry(self):
        """Handles the command for a new entry."""

        self._enable_content_modification()
        
        if self.curr_entry is not None:
            self.curr_entry.content = self.entry_frame.content_text.get(1.0, 'end-1c')

        self.clear_entry()
       
        # Set the datetime of the date created label
        created_date = datetime.now().strftime('%c')
        self.entry_frame.date_created_lbl['text'] = created_date
       
        # Focus on entry title
        self.entry_frame.title_entry.focus()
       
        # Create new list item
        bttn = ttk.Button(self.entry_list_frame,
                          textvariable=self.title_entry_var
        )
        bttn.pack(side=tk.TOP, fill=tk.X)

        # Create Entry object and add to entries dict
        self.curr_entry = Entry(uid=self.db.get_uid(), created_date=created_date, bttn=bttn)
        self.entries.update({self.curr_entry.uid: self.curr_entry})
        # Set the button's command to open the entry
        bttn['command'] = lambda e=self.curr_entry: self.open_entry(e)
    
    def entry_focus_in(self):
        self.curr_entry.bttn['textvariable'] = self.title_entry_var
    
    def entry_focus_out(self, title):
        # Set button text to title of entry and unlink textvariable
        self.curr_entry.title = title
        self.curr_entry.bttn.config(textvariable='', text=title)
        
        # Write to database
        self.db.add_entry(self.curr_entry)

    def _enable_content_modification(self):
        """Enables the title entry and content content_text to be modified."""
        self.entry_frame.title_entry['state'] = tk.NORMAL
        self.entry_frame.content_text['state'] = tk.NORMAL