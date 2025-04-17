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

unique_chefs = df['Chef'].unique()
cols = st.columns(3)  # Adjust number of columns as needed

for i, chef in enumerate(unique_chefs):
    with cols[i % 3]:
        st.button(chef)

st.divider()


for meal in unique_meals:
    row = df[df['Meal Name'] == meal].iloc[0]
    img_path = row['Dish Picture']

    main_col1, main_col2 = st.columns(2)

    with main_col1:
        with st.container():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image(img_path, use_container_width=True)
            with col2:
                if st.button(meal):
                    st.session_state[f"{meal}_clicked"] = True

                if st.session_state.get(f"{meal}_clicked", False):
                    ingredients = df[df['Meal Name'] == meal]['Ingrediants']
                    cookbook = row['Cookbook']
                    st.write(f"{meal} is in **{cookbook}** and the ingredients are:")
                    st.table(ingredients)
                    grocery_list = st.checkbox("Add to grocery list?", key=f"grocery_{meal}")
                    if grocery_list:
                        chosen_ingredients = ingredients

    with main_col2:
            st.write(chosen_ingredients)


