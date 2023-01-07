import plotly.express as px
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import streamlit as st

book=pd.read_csv("Data/book.csv")

tab1, tab2 = st.tabs(["Price", "Rating & Quantity"])

with tab1:
   st.header("Price Vs Book_category")
   fig = px.bar(book, x="Book_category", y="Price")
   st.plotly_chart(fig,theme="streamlit", use_container_width=True)
    
   

with tab2:
   st.header("Quantity Vs Book_category based on Star_rating")
   fig1 = px.bar(book, x="Book_category",y="Quantity",color="Star_rating")
   st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

   