import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("Top 100 Trending Books Analysis")

# Reads the files
df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()

max_price = st.sidebar.slider("Price Range", price_min, price_max, price_max)

# Filters the books based on the selected price range
df_books = df_top100_books[df_top100_books["book price"] <= max_price]
df_books  # Prints the filtered table

years_fig = px.bar(df_books["year of publication"].value_counts())
price_fig = px.histogram(df_books["book price"])

col1, col2 = st.columns(2) # Creates two columns for the plots

col1.plotly_chart(years_fig)
col2.plotly_chart(price_fig)
