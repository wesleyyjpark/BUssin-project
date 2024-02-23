# DATABASE FOR LOGINS WILL BE STORED HERE.
import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")