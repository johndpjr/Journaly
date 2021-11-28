import tkinter as tk
from tkinter import ttk

import os
import pickle

from crypto import Crypto
from app import App


class InitFlowApp(tk.Tk):
    """Models the toplevel window that allows access to the
    main Journaly application.
    """

    def __init__(self):
        # Initialize the top window
        super().__init__()
        # Set window attributes
        self.geometry('400x400')

        if not os.path.exists('info.pickle'):
            # Start new password flow
            self.title('Journaly - create journal password')
            tk.Label(self,
                     text='No password found... please create one below.'
            ).grid(row=0, column=0, columnspan=2, sticky=tk.W)
            self.user_notify_label = tk.Label(self, fg='red')
            self.user_notify_label.grid(row=1, column=0, columnspan=2, sticky=tk.W)

            self.pw_init_entry = ttk.Entry(self)
            self.pw_confirm_entry = ttk.Entry(self)
            self.pw_init_entry.grid(row=2, column=0)
            self.pw_confirm_entry.grid(row=3, column=0)

            ttk.Button(self,
                       text='Create password',
                       command=self._on_create_pw_bttn_click
            ).grid(row=2, column=1, rowspan=2)
        else:
            # A password was created: ask user to enter password
            self.encrypted_pw = pickle.load(open('info.pickle', 'rb'))['encrypted_pw']
            self.title('Journaly - enter journal password')
            tk.Label(self, text='Enter password...').grid(row=0, column=0, columnspan=2, sticky=tk.W)
            self.pw_entry = ttk.Entry(self)
            self.pw_entry.grid(row=1, column=0, sticky=tk.W)
            ttk.Button(self,
                       text='Unlock journal',
                       command=self._on_unlock_journal_bttn_click
            ).grid(row=1, column=1, sticky=tk.W)
    
    def _on_create_pw_bttn_click(self):
        # Check if init and confirm passwords match
        password = self.pw_init_entry.get()

        if password or self.pw_confirm_entry.get():
            if password == self.pw_confirm_entry.get():
                # Create Crypto object
                self.crypto = Crypto(password)
                info_dict = {
                    'encrypted_pw': self.crypto.encrypt(password)
                }
                pickle.dump(info_dict, open('info.pickle', 'wb'))
            else:  # passwords don't match - notify user
                self.user_notify_label['text'] = "*Passwords don't match - try again"
        else:
            self.user_notify_label['text'] = "*Fill and match both password fields"

    def _on_unlock_journal_bttn_click(self):
        entered_pw = self.pw_entry.get()
        self.crypto = Crypto(entered_pw)
        print(self.encrypted_pw)
        print(self.crypto.encrypt(entered_pw))
        if self.crypto.encrypt(entered_pw) == self.encrypted_pw:  # password is correct
            self.destroy()
            app = App()
            app.mainloop()


if __name__ == '__main__':
    init_flow_app = InitFlowApp()
    init_flow_app.mainloop()