import streamlit as st
import pandas as pd


st.title("Grocery List")
st.write(
    "Click on a recipe button for information on the given recipe"
)

file_url = 'https://raw.githubusercontent.com/brinoceros484/grocery_list/refs/heads/main/RecipeGeneratorSheet1.csv'

df=pd.read_csv(file_url)

unique_meals = df['Meal Name'].unique()

# for meal in unique_meals:
#     if st.button(meal):
#         st.write(f"The ingredients for {meal} are:")
#         ingredients = df[df['Meal Name'] == meal]['Ingrediants']
#         ingredients_table = st.table(ingredients)


for meal in unique_meals:
     if st.button(meal):
         ingredients = df[df['Meal Name'] == meal]['Ingrediants']
         cookbook = df[df['Meal Name'] == meal]['Cookbook'].values[0]
         st.write(f"{meal} is in **{cookbook}** and the ingredients are:")
         ingredients_table = st.table(ingredients)        



# recipes_df = pd.read_csv(r"C:\Users\BrianMathis\Downloads\RecipeGeneratorSheet1.csv")  # Replace with your CSV file name
# recipes = recipes_df['Meal Name'].tolist()  # Replace with the correct column name

# st.write(recipes)
# st.print()


# column_left, column_right = st.columns(2)
# salmon = st.button("Salmon Teriyaki & Broccolini")
# ravioli = st.button("Ravioli en Brodo")

# column_right.ravioli




# # if st.button("Salmon Teriyaki & Broccolini"):
# #     st.write("Generate Recipe Info")

# # if st.button("Ravioli en Brodo"):
# #     st.write("Generate Recipe Info")

