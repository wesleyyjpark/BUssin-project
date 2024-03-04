# DATABASE FOR LOGINS WILL BE STORED HERE.
import sqlite3
import hashlib

conn = sqlite3.connect("'./databases/userdata.db'")
cursor = conn.cursor()  

cursor.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY, 
    username TEXT NOT NULL,
    password TEXT NOT NULL    
)
""")

#REGISTER: user/pass inputted into database
def register(username, password):
    cursor.execute("SELECT username from userdata WHERE username=?", (username,))
    if len(cursor.fetchone()) != 0:
        #username already exists so return error msg <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        print() #remove this <<<<<<<<<<<<<<<<<<<
    if is_not_valid_register():
        #if username/password isnt valid let user know <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        print() #remove this <<<<<<<<<<<<<<<<<<<
    cursor.execute("INSERT INTO userdata VALUES (?, ?)", (username, password))



#LOGIN: check if user/pass in database
def login(username, password):


    cursor.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (username, password))




#invalid username/passwords
def is_not_valid_register():
    #check if "bu.edu" is at the end <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
