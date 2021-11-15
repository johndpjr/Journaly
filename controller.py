import tkinter as tk
from tkinter import ttk

from datetime import datetime

from entry import Entry


class Controller:
    """Accepts input and handles it."""
    
    def __init__(self, parent):
        self.parent = parent

        # "Global" variables
        self.title_entry_var = tk.StringVar()

        self.curr_entry = None
        self.entries = {}  # contains active Entry objects
    
    def add_frames(self):
        # Frames
        self.search_frame = self.parent.search_frame
        self.entry_list_frame = self.parent.entry_list_frame
        self.entry_info_frame = self.parent.entry_info_frame
        self.entry_content_frame = self.parent.entry_content_frame
    
    def clear_entry(self):
        """Clears the current entry information."""
        # Erase title
        self.entry_info_frame.title_entry.delete(0, tk.END)
        # Erase content text box
        self.entry_content_frame.entry_content_text.delete(1.0, tk.END)
    
    def open_entry(self, entry):
        # Save the current entry

        self.curr_entry.bttn['textvariable'] = ''
        # Clear title entry and content text box
        self.clear_entry()
        # Insert title
        self.entry_info_frame.title_entry.insert(0, entry.title)
        # Set created date label
        self.entry_info_frame.date_created_lbl['text'] = entry.created_date
        # Insert entry content to text box
        self.entry_content_frame.entry_content_text.insert(1.0, entry.content)
        # Focus on end of text box
        self.entry_content_frame.entry_content_text.focus()
        self.curr_entry = entry
    
    def new_entry(self):
        """Handles the command for a new entry."""

        # Enable modification of entry title and content
        self.entry_info_frame.title_entry['state'] = tk.NORMAL
        self.entry_content_frame.entry_content_text['state'] = tk.NORMAL
        
        # TODO: save content of previous entry

        self.clear_entry()
       
        # Set the datetime of the date created label
        created_date = datetime.now().strftime('%c')
        self.entry_info_frame.date_created_lbl['text'] = created_date
       
        # Focus on entry title
        self.entry_info_frame.title_entry.focus()
       
        # Create new list item
        bttn = ttk.Button(self.entry_list_frame,
                          textvariable=self.title_entry_var
        )
        bttn.pack(side=tk.TOP, fill=tk.X)

        # Create Entry object and add to entries dict
        self.curr_entry = Entry(created_date=created_date, bttn=bttn)
        self.entries.update({self.curr_entry.id: self.curr_entry})
        # Set the button's command to open the entry
        bttn['command'] = lambda e=self.curr_entry: self.open_entry(e)
    
    def entry_focus_in(self):
        self.curr_entry.bttn['textvariable'] = self.title_entry_var
    
    def entry_focus_out(self, title):
        # Set button text to title of entry and unlink textvariable
        self.curr_entry.title = title
        self.curr_entry.bttn.config(textvariable='', text=title)
        # TODO: write to database