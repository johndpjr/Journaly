from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from datetime import datetime

from database.database import Database
from entry import Entry
from enums import DateFormat

import typing
if typing.TYPE_CHECKING:
    from app import App


class Controller:
    """Accepts user input and converts it to a relevant command."""
    
    def __init__(self, parent: App):
        self.parent = parent

        self.db = Database()

        # "Global" variables
        self.title_entry_var = tk.StringVar()

        self.curr_entry = None
        self.entries = {}  # contains cached Entry objects
        self._curr_grid_row = 2
    
    def add_frames(self):
        self.entry_list_frame = self.parent.entry_list_frame
        self.entry_frame = self.parent.entry_frame
    
    def delete_entry(self, entry: Entry):
        """Removes the entry from the view and the database."""
        entry.remove_from_view()

        self.db.delete_entry(entry)
        del self.entries[entry.uid]  # free entry from cache

        # Clear the entry_frame if currently selected entry is deleted.
        if self.curr_entry is not None and entry.uid == self.curr_entry.uid:
            self.entry_frame.clear_entry()
            # TODO: auto-select the next entry
            self.entry_frame.set_entry_modification_state(tk.DISABLED)
    
    def get_date_format_view(self, date_str: str, target_format: DateFormat):
        """Returns the appropriate format for the date storage and view."""
        if target_format is DateFormat.DB:
            return datetime.strptime(date_str, DateFormat.USER.value).strftime(DateFormat.DB.value)
        elif target_format is DateFormat.USER:
            return datetime.strptime(date_str, DateFormat.DB.value).strftime(DateFormat.USER.value)
    
    def _add_new_entry_list_item(self, **kwargs) -> Entry:
        """Adds a new entry list item to the entry list.
        Returns the newly created entry.
        """
        bttn = ttk.Button(self.entry_list_frame)
        bttn.grid(row=self._curr_grid_row, column=0, sticky=tk.EW)

        del_bttn = ttk.Button(self.entry_list_frame, text='X')
        del_bttn.grid(row=self._curr_grid_row, column=1)
        self._curr_grid_row += 1

        entry = Entry(self, bttn=bttn, del_bttn=del_bttn, **kwargs)
        
        return entry
    
    def on_startup(self):
        """Executes the startup flow for the application.
        Retrieves all entries from the database and
        displays them as buttons.
        """
        for db_entry in self.db.getall_entries():
            # Create entry object
            entry = self._add_new_entry_list_item(uid=db_entry[0], title=db_entry[1],
                                                  created_date=db_entry[2], content=db_entry[3],
                                                  persistent=True
            )
            # Update the dictionary
            self.entries.update({entry.uid: entry})
    
    def open_entry(self, entry):
        # Save the current entry
        if self.curr_entry is None:
            self.entry_frame.set_entry_modification_state(tk.NORMAL)
            self.curr_entry = entry
        else:
            self.curr_entry.content = self.entry_frame.get_content()
        
        self.entry_frame.clear_entry()
        self.entry_frame.insert_entry(entry)
        self.curr_entry = entry
    
    def save_entry(self):
        """Saves the current entry to the database."""
        if self.curr_entry is not None:
            self.curr_entry.title = self.entry_frame.title_entry.get()
            self.curr_entry.content = self.entry_frame.get_content()
            self.db.update_entry(self.curr_entry)
    
    def new_entry(self):
        """Handles the command for a new entry."""

        self.entry_frame.clear_entry()
       
        # Set the datetime of the date created label
        created_date = datetime.now()
        self.entry_frame.date_created_label['text'] = created_date.strftime(DateFormat.USER.value)
       
        # Focus on entry title
        self.entry_frame.title_entry.focus()

        # Create Entry object and add to entries dict
        self.curr_entry = self._add_new_entry_list_item(uid=self.db.get_uid(),
                                                        created_date=created_date.strftime(DateFormat.DB.value)
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