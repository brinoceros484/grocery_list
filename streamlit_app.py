import streamlit as st
import pandas as pd

col_1header, col2_header, col3_header = st.columns(3)
col2_header.title("Grocery List App")
st.write(
    "Click on a recipe button for information on the given recipe"
)

st.write(
    "Are there any Chefs you want to filter for?"
)

if 'grocery_list' not in st.session_state:
    st.session_state.grocery_list = []

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
    ingredients = df[df['Meal Name'] == meal]['Ingrediants'].tolist()
    cookbook = row['Cookbook']

    with st.container():
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(img_path, use_container_width=True)
        with col2:
            expand = st.expander(meal)  # CHANGED from button to expander
            with expand:
                st.write(f"{meal} is in **{cookbook}** and the ingredients are:")
                st.table(ingredients)
                
                # NEW: Checkbox to add ingredients
                if st.checkbox(f"Add {meal} to grocery list?", key=meal):
                    for ingredient in ingredients:
                        if ingredient not in st.session_state.grocery_list:
                            st.session_state.grocery_list.append(ingredient)

# NEW: Show grocery list
st.divider()
st.subheader("Your Grocery List:")
if st.session_state.grocery_list:
    #st.write(st.session_state.grocery_list)
    st.table(st.session_state.grocery_list)
else:
    st.write("No items yet. Select recipes above!")