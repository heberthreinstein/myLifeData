import streamlit as st

# Custom imports 
from multipage import MultiPage
from pages.expense import newExpense, listExpense # import your pages here

# Create an instance of the app 
app = MultiPage()

# Add all your applications (pages) here
app.add_page("New Expense", newExpense.app)
app.add_page("List Expenses", listExpense.app)

# The main app
app.run()