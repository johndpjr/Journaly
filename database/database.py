import sqlite3
import uuid
from pathlib import Path

from entry import Entry
from enums import UpdateType


class Database:
    """Models a SQLite Database for Journaly"""

    def __init__(self):
        # Create connection to database
        self.conn = sqlite3.connect(Path('database/journal.db'))
        self.c = self.conn.cursor()

        # Initial table creation sequence
        with self.conn:
            # Create Entries table
            self.c.execute("""CREATE TABLE IF NOT EXISTS Entries (
                uid TEXT,
                title TEXT DEFAULT '',
                createdDate TEXT,
                content TEXT DEFAULT ''
            )""")
    
    def get_uid(self):
        """Returns a valid uuid4."""
        return str(uuid.uuid4()).replace('-', '')
    
    def add_entry(self, entry: Entry):
        """Adds an entry to Entries."""
        with self.conn:
            self.c.execute("INSERT INTO Entries (uid, title, createdDate) VALUES (?, ?, ?)",
                           (entry.uid, entry.title, entry.created_date)
            )
    
    def delete_entry(self, entry: Entry):
        """Deletes the entry from Entries."""
        with self.conn:
            self.c.execute("DELETE FROM Entries WHERE uid=?", (entry.uid,))

    def update_entry(self, entry: Entry, update_type: UpdateType=UpdateType.ALL):
        """Updates an entry."""

        if update_type is UpdateType.TITLE:
            with self.conn:
                self.c.execute("""UPDATE Entries
                               SET title=?
                               WHERE uid=?""",
                               (entry.title, entry.uid)
                )
        elif update_type is UpdateType.CONTENT:
            with self.conn:
                self.c.execute("""UPDATE Entries
                               SET content=?
                               WHERE uid=?""",
                               (entry.content, entry.uid)
                )
        else:  # update_type is UpdateType.ALL
            with self.conn:
                self.c.execute("""UPDATE Entries
                               SET title=?,
                               content=?
                               WHERE uid=?""",
                               (entry.title, entry.content, entry.uid)
                )
    
    def getall_entry_titles(self):
        """Returns a list of entry titles from Entries."""
        with self.conn:
            self.c.execute("SELECT uid, title FROM Entries")
        return self.c.fetchall()
    
    def get_cache(self, entry: Entry):
        """Returns the cache for an entry (content and createdDate)."""
        with self.conn:
            self.c.execute("SELECT createdDate, content FROM Entries WHERE uid=?", (entry.uid,))
        return self.c.fetchone()