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

        # Add the transaction
        self.c.execute("""
            INSERT INTO book
            (sum, timestamp, payee, desc, method)
            VALUES (?, ?, ?, ?, ?);
            """,
            (t.sum, t.timestamp, t.payee, t.desc, t.method) )

        # Get back the id of the added transaction
        id_transaction = self.c.lastrowid

        # Save tags
        for tag in t.tags:
            self.linkToTag(id_transaction, tag)



    def get(self, request, *args):
        """Return transactions given a request.
        """

        self.c.execute("""
            SELECT sum, timestamp, payee, desc, method
            FROM book
            %s
            """ % request,
            *args)

        return [transaction._make(list(t) + [''])
                for t in self.c.fetchall()]

    def getSince(self, timestamp):
        """Return transactions since a given timestamp.
        """

        return self.get("""
            WHERE timestamp >= ?
            ORDER BY timestamp;
            """, (timestamp,))

    def getFromTo(self, timestamp1, timestamp2):
        """Return transactions between timestamp1 and timestamp2.
        """

        return self.get("""
            WHERE timestamp >= ?
            AND   timestamp <= ?
            ORDER BY timestamp;
            """, (timestamp1, timestamp2))

    def getFromPayee(self, payee):
        """Return transaction given a payee.
        """

        return self.get("""
            WHERE payee = ?
            ORDER BY timestamp;
            """, (payee,))

    def getPayees(self):
        """Return a list of all payees.
        """

        self.c.execute("""
            SELECT payee
            FROM book
            GROUP BY payee;
            """)

        return [p[0] for p in self.c.fetchall()]

    def getTags(self):
        """Return a list of all tags.
        """

        self.c.execute("""
            SELECT name
            FROM tags
            GROUP BY name;
            """)

        return [t[0] for t in self.c.fetchall()]

    # -------------

    def getTagId(self, name):
        """Return the id of a tag given its name.
        """
        
        self.c.execute("""
            SELECT id_tag
            FROM tags
            WHERE name = ?;
            """, (name,))

        tag = self.c.fetchone()

        if tag:
            return tag[0]
        else:
            return None

    def linkToTag(self, id_transaction, tag):
        """Add a tag to a transaction.
        """

        # Get the id of the tag
        id_tag = self.getTagId(tag)

        if not id_tag:
            # The tag doesn't exist...
            # ... so create it
            self.c.execute("""
                INSERT INTO tags
                (name)
                VALUES (?);
                """, (tag,))

            id_tag = self.c.lastrowid

            # ... and link it with the transaction
            self.c.execute("""
                INSERT INTO tag_links
                (id_transaction, id_tag)
                VALUES (?, ?);
                """, (id_transaction, id_tag))
        else:
            # The tag already exist...
            # ... check if the transaction is already linked to this tag
            self.c.execute("""
                SELECT *
                FROM tag_links
                WHERE id_transaction = ? AND id_tag = ?;
                """, (id_transaction, id_tag))

            if not self.c.fetchone():
                # ... link the tag with the transaction if necessary
                self.c.execute("""
                    INSERT INTO tag_links
                    (id_transaction, id_tag)
                    VALUES (?, ?);
                    """, (id_transaction, id_tag))

        self.commit()

    # -------------

    def commit(self):
        """Commit modifications in the database.
        """
        self.db_con.commit()

    def createTables(self):
        """Create tables if necessary.
        """
        try:
            self.c.execute('''CREATE TABLE book (
                id_transaction INTEGER PRIMARY KEY,
                sum REAL,
                timestamp TEXT,
                payee TEXT,
                desc TEXT,
                method TEXT);
                ''')

            self.c.execute('''CREATE TABLE tags (
                id_tag INTEGER PRIMARY KEY,
                name TEXT);
                ''')

            self.c.execute('''CREATE TABLE tag_links (
                id_transaction INTEGER,
                id_tag INTEGER);
                ''')

            self.db_con.commit()
            return True

        except:
            return False

if __name__ == "__main__":
    with accountBook() as a:
        print(a.getPayees())
