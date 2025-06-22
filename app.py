import streamlit as st
from navbar.navbar import render_navbar
from hero.hero import render_hero
from footer.footer import render_footer

from shops.shops import render_shops_page
from jewelry.jewelry import render_jewelry_page
from books.books import render_books_page
from grocery.grocery import render_grocery_page
from foodcourt.foodcourt import render_foodcourt_page
from about.about import render_about_page
from contact.contact import render_contact_page


# Navigation router
PAGES = {
    "Home": "home",
    "Shops": render_shops_page,
    "Jewelry": render_jewelry_page,
    "Books": render_books_page,
    "Grocery": render_grocery_page,
    "Food Court": render_foodcourt_page,
    "About": render_about_page,
    "Contact": render_contact_page,
}

# Set page config
st.set_page_config(page_title="Diamond Shopping Mall", layout="wide")
with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Render navbar
render_navbar()

# Page selection
page = st.query_params.get("page", "Home")

if page == "Home":
    render_hero()
else:
    PAGES[page]()  # Call the page function

# Footer
render_footer()


