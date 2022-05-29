import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Pannenkoek spek')
streamlit.text('Pannenkoek appel')
streamlit.text('Pannenkoek naturel')
streamlit.text('Pannenkoek kip 🐔')
streamlit.text('Tosti ham/kaas 🍞')

streamlit.header('\N{flexed biceps} Menu voor sterke spieren \N{flexed biceps}')
streamlit.text('Pannenkoek advocado 🥑')
streamlit.text('Pannenkoek spinazie 🥗')

streamlit.header('🍌 Kindermenu met fruit voor Imke 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Kies wat fruit:", list(my_fruit_list.index),['Avocado','Strawberries'])
streamlit.dataframe(my_fruit_list)


