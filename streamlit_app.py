import streamlit as st
import pandas as pd


st.title("Grocery List App")
st.write(
    "Click on a recipe button for information on the given recipe"
)

st.write(
    "Are there any Chefs you want to filter for?"
)

file_url = 'https://raw.githubusercontent.com/brinoceros484/grocery_list/refs/heads/main/RecipeGeneratorSheet1.csv'

df=pd.read_csv(file_url)

unique_meals = df['Meal Name'].unique()      

for meal in unique_meals:
    row = df[df['Meal Name'] == meal].iloc[0]
    img_path = row['Dish Picture']

    with st.container():
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(img_path, use_container_width=True)
        with col2:
            if st.button(meal):
                ingredients = df[df['Meal Name'] == meal]['Ingrediants']
                cookbook = row['Cookbook']
                st.write(f"{meal} is in **{cookbook}** and the ingredients are:")
                st.table(ingredients)
