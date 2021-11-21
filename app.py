import tkinter as tk

# Frame imports
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
        self.entry_list_frame = EntryListFrame(self)
        self.entry_frame = EntryFrame(self)

        # TODO: think of a better fix
        self.controller.add_frames()
        self.controller.on_startup()

        self.entry_list_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.entry_frame.pack(side=tk.LEFT, fill=tk.BOTH)

        # Handle the window close event
        def on_closing():
            self.controller.save_entry()
            self.destroy()

        self.protocol("WM_DELETE_WINDOW", on_closing)


if __name__ == '__main__':
    app = App()
    app.mainloop()