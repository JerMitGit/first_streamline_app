import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#pick list
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


#display
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)


streamlit.header("Fruityvice Fruit Advice!")
streamlit.text(fruityvice_response)
streamlit.text(fruityvice_response.json()) ##
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

#streamlit.stop
streamlit.header('Snowflake Connector Test')
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)



my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cnx = my_cnx.cursor()
my_cnx.execute("select * from fruit_load_list") # select * from pc_rivery_db.public.fruit_load_list
my_data_row = my_cur.fetchone()

streamlit.text("The fruit load list contains :")
streamlit.text(my_data_row)

my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load ALL list contains :")
streamlit.dataframe(my_data_rows)


add_my_fruit = streamlit.text_input('What fruit would you like to add?','Kiwi')
streamlit.write('The user entered ', add_my_fruit)
streamlit/write('Thanks for adding ', add_my_fruit)

my_cur.execute("inser into fruit_load_list values('from streamlit')")
