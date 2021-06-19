import streamlit as st
import pandas as pd
import datetime
from models.Expense import Expense 

def app():
    st.write("""
    # New expense
    """)

    with st.form("expense"):
            
        date = st.date_input('Date', datetime.datetime.now())
        
        category = st.selectbox('Category',['Entretaining','Food','Fun Food','Bills','Investment','Gifts','Important','Higene','Health','Emergency' 'Fund','Transportation'])

        description = st.text_input("Description")

        price = st.number_input("Price")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            Expense(date, category, description, price).save()
