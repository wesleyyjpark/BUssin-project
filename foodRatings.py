import sqlite3

#func to call the two funcs to add to both databases
def addNewRating(location: str, businessName: str, item: str, rating: float, comments: str, username: str):
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
    
#either adds or updates the database with the new rating
def updateAvg(location, businessName, item, rating):
    conn = sqlite3.connect('./databases/avgFoodRating.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS ratings (location TEXT, business_name TEXT, item TEXT, avg_rating REAL, num_inputs INTEGER)')
    cur.execute('SELECT * FROM ratings WHERE location=? AND business_name=? AND item=?',(location, businessName, item))
    selection = cur.fetchone()
    if selection is None:
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
        
#To add new ratings call the func:
#addNewRating(location:String, business_name:String, item:String, rating:Float, comments:String, username:String)

#testInput = addNewRating('GSU', 'Basho', 'sushi', 5.0, 'it is good', 'Andrew Ting')

conn_avg = sqlite3.connect('./databases/avgFoodRating.db')
conn_all = sqlite3.connect('./databases/allRatings.db')
cur_avg = conn_avg.cursor()
cur_all = conn_all.cursor()
#prints out the database in rows
cur_avg.execute('SELECT * FROM ratings')
data = cur_avg.fetchall()
for i in data:
    print(i)
cur_all.execute('SELECT * FROM ratings')
data = cur_all.fetchall()
for i in data:
    print(i)

#This clears out the db entries for testing
cur_avg.execute('DELETE FROM ratings')
cur_all.execute('DELETE FROM ratings')
conn_avg.commit()
conn_all.commit()

cur_avg.close()
cur_all.close()
conn_avg.close()
conn_all.close()
