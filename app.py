import tkinter as tk

# Frame imports
from frames.search_frame import SearchFrame
from frames.entry_list_frame import EntryListFrame
from frames.entry_frame import EntryFrame

from controller import Controller


class App(tk.Tk):
    """Models the Journaly application."""

    def __init__(self):
        # Create window
        super().__init__()
        # Set window attributes
        self.title('Journaly')
        self.geometry('800x800')

        self.controller = Controller(self)

        # Frame creation
        self.search_frame = SearchFrame(self)
        self.entry_list_frame = EntryListFrame(self)
        self.entry_frame = EntryFrame(self)

        # TODO: think of a better fix
        self.controller.add_frames()
        self.controller.on_startup()

        # Column 0
        self.search_frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.entry_list_frame.grid(row=1, column=0, sticky=tk.NSEW)
        # Column 1
        self.entry_frame.grid(row=0, column=1, rowspan=2, sticky=tk.NSEW)

        self.grid_rowconfigure(1, weight=1)

        # Handle the window close event
        def on_closing():
            self.controller.save_entry()
            self.destroy()

        self.protocol("WM_DELETE_WINDOW", on_closing)


if __name__ == '__main__':
    app = App()
    app.mainloop()