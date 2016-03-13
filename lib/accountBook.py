#! /usr/bin/python3
# -*- coding:utf-8 -*-

import sqlite3
from lib.transaction import *

class accountBook():

    def __init__(self):
        pass

    def __enter__(self):
        # Init the connexion with the database
        self.db_con = sqlite3.connect('picsou.db')

        # Get a cursor
        self.c = self.db_con.cursor()

        # Create tables if necessary
        if self.createTables():
            print("The account book is created.")

        return self

    def __exit__(self, type, value, traceback):
        """Close peacefuly the connexion with the database.
        """

        # Close the cursor
        self.c.close()
        # Close the connexion with the database
        self.db_con.close()

    # -----------------

    def add(self, t):
        """Add a transaction in the account book.
        """

        self.c.execute("""
            INSERT INTO book
            (sum, timestamp, payee, desc)
            VALUES (?, ?, ?, ?);
            """,
            (t.sum, t.timestamp, t.payee, t.desc) )

    def get(self, request, *args):
        """Return transactions given a request.
        """

        self.c.execute("""
            SELECT sum, timestamp, payee, desc
            FROM book
            %s
            """ % request,
            *args)

        return [t for t in map(transaction._make, self.c.fetchall())]

    def getSince(self, timestamp):
        """Return transactions since a given timestamp.
        """

        return self.get("""
            WHERE timestamp >= ?
            ORDER BY timestamp DESC;
            """, (timestamp,))

    def getFromTo(self, timestamp1, timestamp2):
        """Return transactions between timestamp1 and timestamp2.
        """

        return self.get("""
            WHERE timestamp >= ?
            AND   timestamp <= ?
            ORDER BY timestamp DESC;
            """, (timestamp1, timestamp2))

    def getPayee(self, payee):
        """Return transaction given a payee.
        """

        return self.get("""
            WHERE payee = ?
            ORDER BY timestamp DESC;
            """, (payee,))

    def commit(self):
        """Commit modifications in the database.
        """
        self.db_con.commit()

    def createTables(self):
        """Create tables if necessary.
        """
        try:
            self.c.execute('''CREATE TABLE book (
                id INTEGER PRIMARY KEY,
                sum REAL,
                timestamp TEXT,
                payee TEXT,
                desc TEXT);
                ''')

            self.db_con.commit()
            return True

        except:
            return False

if __name__ == "__main__":
    pass
