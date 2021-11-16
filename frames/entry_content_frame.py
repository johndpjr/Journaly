import tkinter as tk


class EntryContentFrame(tk.Frame):
    """Models the Entry Content Frame that contains
    a text box for the journal text content.
    """

    def __init__(self, parent, *args, **kwargs):
        # Initialize the frame
        super().__init__(parent, *args, **kwargs)

        # Entry content text box
        self.textbox = tk.Text(self, state=tk.DISABLED)
        self.textbox.pack(fill=tk.BOTH, expand=True)