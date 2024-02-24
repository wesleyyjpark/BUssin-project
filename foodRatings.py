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
        cursor = conn.cursor()
        query = ''
        
        

input = FoodRating('GSU', 'Halal_Shack', 'rice_bowl', 5, 'it is good')
        
