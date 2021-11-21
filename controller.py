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
        self._row = 1  # "New entry" button is above
    
    def add_frames(self):
        self.search_frame = self.parent.search_frame
        self.entry_list_frame = self.parent.entry_list_frame
        self.entry_frame = self.parent.entry_frame
    
    def delete_entry(self, entry: Entry):
        # Remove widgets from view
        entry.remove_from_view()
        # Remove from database
        self.db.delete_entry(entry.uid)
        del self.entries[entry.uid]
    
    def _new_entry_list_item(self):
        """Adds a new entry list item to the entry list.
        Returns the created button and delete button.
        """
        bttn = ttk.Button(self.entry_list_frame)
        bttn.grid(row=self._row, column=0, sticky=tk.EW)

        del_bttn = ttk.Button(self.entry_list_frame, text='X')
        del_bttn.grid(row=self._row, column=1)
        self._row += 1

        return bttn, del_bttn
    
    def on_startup(self):
        """Executes the startup flow for the application."""
        for entry in self.db.getall_entries():
            # Create entry object
            bttn, del_bttn = self._new_entry_list_item()
            e = Entry(self, uid=entry[0], title=entry[1],
                      created_date=entry[2], content=entry[3],
                      bttn=bttn, del_bttn=del_bttn,
                      persistent=True)
            # Update the dictionary
            self.entries.update({e.uid: e})
            bttn['text'] = e.title
    
    def open_entry(self, entry):
        # Save the current entry
        if self.curr_entry is None:
            self.entry_frame.enable_entry_modification()
            self.curr_entry = entry
        else:
            self.curr_entry.bttn['textvariable'] = ''
            self.curr_entry.content = self.entry_frame.get_content()
        
        self.entry_frame.clear_entry()
        self.entry_frame.insert_entry(entry)
        self.curr_entry = entry
    
    def new_entry(self):
        """Handles the command for a new entry."""

        self.entry_frame.enable_entry_modification()
        
        # if self.curr_entry is not None:
        #     self.curr_entry.content = self.entry_frame.get_content()

        self.entry_frame.clear_entry()
       
        # Set the datetime of the date created label
        created_date = datetime.now().strftime('%c')
        self.entry_frame.date_created_lbl['text'] = created_date
       
        # Focus on entry title
        self.entry_frame.title_entry.focus()
       
        bttn, del_bttn = self._new_entry_list_item()

        # Create Entry object and add to entries dict
        self.curr_entry = Entry(self, uid=self.db.get_uid(),
                                created_date=created_date,
                                bttn=bttn, del_bttn=del_bttn
        )
        self.entries.update({self.curr_entry.uid: self.curr_entry})
    
    def entry_focus_in(self):
        self.curr_entry.bttn['textvariable'] = self.title_entry_var
    
    def entry_focus_out(self, title: str):
        # Set button text to title of entry.
        self.curr_entry.title = title
        # Unlink the textvaraible of the current entry.
        self.curr_entry.bttn.config(textvariable='', text=title)
        
        # Add to database if entry is not persistent.
        if not self.curr_entry.persistent:
            self.db.add_entry(self.curr_entry)
            self.curr_entry.persistent = True
        else:  # update content if persistent
            self.db.update_entry(self.curr_entry)
    
    def textbox_focus_out(self):
        self.curr_entry.content = self.entry_frame.get_content()
        if self.curr_entry.persistent:
            self.db.update_entry(self.curr_entry)
        else:
            self.db.add_entry(self.curr_entry)