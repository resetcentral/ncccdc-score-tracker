#!/usr/bin/env python3
import sqlite3

conn = sqlite3.connect('scores.db')
c = conn.cursor()
c.execute('DROP TABLE IF EXISTS scores')
c.execute('CREATE TABLE scores (frame integer, team integer, service integer, result integer)')
conn.commit()
conn.close()
