import csv
import sqlite3

class FoodRating:
    def __init__(self, location, businessName, item, rating, comments):
        self.location = location
        self.businessName = businessName
        self.item = item
        self.rating = rating
        self.comments = comments
        self.addNewRating()
        self.updateAvg()

    def addNewRating(self):
        file = open('./databases/ratings.csv', 'a', newline='')
        writer = csv.writer(file)
        newInput = [self.location, self.businessName, self.item, self.rating, self.comments]
        writer.writerow(newInput)
        file.close()
    
    def updateAvg(self):
        conn = sqlite3.connect('./databases/avgFoodRating.db')
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS ratings (location TEXT, business_name TEXT, item TEXT, avg_rating REAL, num_inputs INTEGER)')
        cur.execute('SELECT * FROM ratings WHERE location=? AND business_name=? AND item=?',(self.location, self.businessName, self.item))
        selection = cur.fetchone()
        if selection is None:
            cur.execute('INSERT INTO ratings (location, business_name, item, avg_rating, num_inputs) VALUES (?,?,?,?,?)', (self.location, self.businessName, self.item, self.rating, 1))
        else:
            cur.execute('SELECT avg_rating FROM ratings WHERE location=? AND business_name=? AND item=?', (self.location, self.businessName, self.item))
            avg = cur.fetchone()[0]
            cur.execute('SELECT num_inputs FROM ratings WHERE location=? AND business_name=? AND item=?', (self.location, self.businessName, self.item))
            num = cur.fetchone()[0]
            avg = ((avg*num)+self.rating)/(num+1)
            num += 1
            cur.execute('UPDATE ratings SET avg_rating=?, num_inputs=? WHERE location=? AND business_name=? AND item=?', (avg,num,self.location, self.businessName, self.item))
        conn.commit()
        cur.close()
        conn.close()
        
input = FoodRating('GSU', 'Basho', 'sushi', 5, 'it is good')

conn = sqlite3.connect('./databases/avgFoodRating.db')
cur = conn.cursor()
cur.execute('SELECT * FROM ratings')
print(cur.fetchall())
""" #This clears out the db entries for testing
cur.execute('DELETE FROM ratings')
conn.commit()
"""
cur.close()
conn.close()
        
