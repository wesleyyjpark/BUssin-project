import sqlite3

#func to call the two funcs to add to both databases
def addNewRating(location: str, vendor: str, category: str, item: str, rating: float) -> None:
    #newRating(location, businessName, item, rating, comments, username)
    updateAvg(location, vendor, category, item, rating)

def removeRating(location: str, vendor: str, category: str, item: str, rating: int) -> None:
    #removeRatingFromAll(location, businessName, item, rating, comments, username)
    removeRatingFromAvg(location, vendor, category, item, rating)
    
#adds the rating to database of all ratings
'''
def newRating(location, businessName, item, rating, comments, username) -> None:
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS ratings (location TEXT, business_name TEXT, item TEXT, rating REAL, comments TEXT, username TEXT)')
    newRating = [location, businessName, item, rating, comments, username]
    cur.execute('INSERT INTO ratings (location, business_name, item, rating, comments, username) VALUES (?,?,?,?,?,?)', newRating)
    conn.commit()
    cur.close()
    conn.close()
'''
#either adds or updates the database with the new rating
def updateAvg(location, vendor, category, item, rating) -> None:
    conn = sqlite3.connect('ratings.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS ratings (location TEXT, vendor TEXT, category TEXT, item TEXT, avg_rating REAL, num_inputs INTEGER)')
    cur.execute('SELECT * FROM ratings WHERE location=? AND vendor=? AND category=? AND item=?',(location, vendor, category, item))
    if cur.fetchone() is None:
        cur.execute('INSERT INTO ratings (location, vendor, category, item, avg_rating, num_inputs) VALUES (?,?,?,?,?,?)', (location, vendor, category, item, rating, 1))
    else:
        cur.execute('SELECT avg_rating, num_inputs FROM ratings WHERE location=? AND vendor=? AND category=? AND item=?', (location, vendor, category, item))
        one = cur.fetchone()
        avg, num = one[0], one[1]
        avg = ((avg*num)+rating)/(num+1)
        num += 1
        cur.execute('UPDATE ratings SET avg_rating=?, num_inputs=? WHERE location=? AND vendor=? AND category=? AND item=?', (avg,num,location, vendor, category, item))
    conn.commit()
    cur.close()
    conn.close()
        
#removes the rating to database of all ratings <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def removeRatingFromAll(location, vendor, category, item, rating, comments, user_id) -> None:
    conn = sqlite3.connect('ratings.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM ratings WHERE location=? AND vendor=? AND category=? AND item=? AND rating=? AND comments=? AND user_id=?', (location, vendor, category, item, rating, comments, user_id))
    conn.commit()
    cur.close()
    conn.close()

def removeRatingFromAvg(location, vendor, category, item, rating) -> None:
    conn = sqlite3.connect('ratings.db')
    cur = conn.cursor()
    cur.execute('SELECT avg_rating, num_inputs FROM ratings WHERE location=? AND vendor=? AND category=? AND item=?', (location, vendor, category, item))
    one = cur.fetchone()
    avg, num = one[0], one[1]
    if num == 1:
        cur.execute('DELETE FROM ratings WHERE location=? AND VENDOR=? AND category=? AND item=?', (location, vendor, category, item))
    else:
        avg = ((avg*num)-rating)/(num-1)
        num -= 1
        cur.execute('UPDATE ratings SET avg_rating=?, num_inputs=? WHERE location=? AND vendor=? AND category=? AND item=?', (avg, num, location, vendor, category, item))
    conn.commit()
    cur.close()
    conn.close()

#given an integer, this will return the top n entries, if not given a location or business name, it will default to all, 
#if business is given location must also be given
#if not enough entries for n, all entries will be shown
def returnNTop(num: int, location=None, businessName=None) -> list:
    conn = sqlite3.connect('ratings.db')
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
