import models.db.mongodbConnection as conn
import streamlit as st

class Expense():
    
    def __init__(self, date, category, description, price):
        self.date = date
        self.category = category
        self.description = description
        self.price = price
    
    def save(self):
        db = conn.getDbConnection(self)
              
        doc = {"date": self.date.strftime("%d/%m/%Y"),
               "category": self.category,
               "descrption": self.description,
               "price": self.price}
        
        collection = db.Expense
        id = collection.insert_one(doc).inserted_id
        if id:
            st.success("Saved")
        
        