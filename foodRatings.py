import sqlite3

#func to call the two funcs to add to both databases
def addNewRating(location: str, businessName: str, item: str, rating: float, comments: str, username: str) -> None:
    newRating(location, businessName, item, rating, comments, username)
    updateAvg(location, businessName, item, rating)
    
#adds the rating to database of all ratings
def newRating(location, businessName, item, rating, comments, username):
    conn = sqlite3.connect('./databases/allRatings.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS ratings (location TEXT, business_name TEXT, item TEXT, rating REAL, comments TEXT, username TEXT)')
    newRating = [location, businessName, item, rating, comments, username]
    cur.execute('INSERT INTO ratings (location, business_name, item, rating, comments, username) VALUES (?,?,?,?,?,?)', newRating)
    conn.commit()
    cur.close()
    conn.close()

#removes the rating to database of all ratings <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def removeRating():

#either adds or updates the database with the new rating
def updateAvg(location, businessName, item, rating) -> None:
    conn = sqlite3.connect('./databases/avgFoodRating.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS ratings (location TEXT, business_name TEXT, item TEXT, avg_rating REAL, num_inputs INTEGER)')
    cur.execute('SELECT * FROM ratings WHERE location=? AND business_name=? AND item=?',(location, businessName, item))
    if cur.fetchone() is None:
        cur.execute('INSERT INTO ratings (location, business_name, item, avg_rating, num_inputs) VALUES (?,?,?,?,?)', (location, businessName, item, rating, 1))
    else:
        cur.execute('SELECT avg_rating FROM ratings WHERE location=? AND business_name=? AND item=?', (location, businessName, item))
        avg = cur.fetchone()[0]
        cur.execute('SELECT num_inputs FROM ratings WHERE location=? AND business_name=? AND item=?', (location, businessName, item))
        num = cur.fetchone()[0]
        avg = ((avg*num)+rating)/(num+1)
        num += 1
        cur.execute('UPDATE ratings SET avg_rating=?, num_inputs=? WHERE location=? AND business_name=? AND item=?', (avg,num,location, businessName, item))
    conn.commit()
    cur.close()
    conn.close()
        
#given an integer, this will return the top n entries, if not given a location or business name, it will default to all, 
#if business is given location must also be given
#if not enough entries for n, all entries will be shown
def returnNTop(num: int, location=None, businessName=None) -> list:
    conn = sqlite3.connect('./databases/avgFoodRating.db')
    cur = conn.cursor()
    if location is not None and businessName is not None:
        cur.execute('SELECT * FROM ratings WHERE location=? AND business_name=? ORDER BY avg_rating DESC', (location, businessName))
    elif location is not None and businessName is None:
        cur.execute('SELECT * FROM ratings WHERE location=? ORDER BY avg_rating DESC', (location,))
    else:
        cur.execute('SELECT * FROM ratings ORDER BY avg_rating DESC')
    nTop = cur.fetchmany(num)
    cur.close()
    conn.close()
    return nTop
         
#To add new ratings call the func:
#addNewRating(location:String, business_name:String, item:String, rating:Float, comments:String, username:String)

#testInput = addNewRating('West', 'Grill_Station', 'fries', 5, 'it is good', 'Andrew Ting')

"""
for i in returnNTop(5, 'GSU', 'Basho'):
    print(i)
"""
conn_avg = sqlite3.connect('./databases/avgFoodRating.db')
conn_all = sqlite3.connect('./databases/allRatings.db')
cur_avg = conn_avg.cursor()
cur_all = conn_all.cursor()
#prints out the database in rows
"""
cur_avg.execute('SELECT * FROM ratings')
data = cur_avg.fetchall()
for i in data:
    print(i)
#"""
"""
cur_all.execute('SELECT * FROM ratings')
data = cur_all.fetchall()
for i in data:
    print(i)
#"""
#This clears out the db entries for testing
"""
cur_avg.execute('DELETE FROM ratings')
cur_all.execute('DELETE FROM ratings')
conn_avg.commit()
conn_all.commit()
#"""
cur_avg.close()
cur_all.close()
conn_avg.close()
conn_all.close()
