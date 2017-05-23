#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('MangaLife.db')
print "Opened database successfully";

conn.execute('''CREATE TABLE MangaList
       (NAME           TEXT    NOT NULL,
       ADDRESS        CHAR(1000));''')
print "Table created successfully";

conn.close()