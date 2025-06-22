import streamlit as st
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def render_navbar():
    logo_base64 = get_base64_image("assets/logo.png")
    phone_icon_base64 = get_base64_image("assets/callme.png")

    st.markdown(f"""
    <div class="navbar">
        <div class="logo-container">
            <a href="?page=Home" target="_self">
                <img src="data:image/png;base64,{logo_base64}" class="logo">
            </a>
        </div>
        <div class="nav-links">
            <a href="?page=Home" target="_self">Home</a>
            <a href="?page=Shops" target="_self">Shops</a>
            <a href="?page=Jewelry" target="_self">Jewelry</a>
            <a href="?page=Books" target="_self">Books</a>
            <a href="?page=Grocery" target="_self">Grocery</a>
            <a href="?page=Food Court" target="_self">Food Court</a>
            <a href="?page=About" target="_self">About</a>
            <a href="?page=Contact" target="_self">Contact</a>
        </div>
        <div class="contact-icon">
            <a href="tel:+923332236799">
                <img src="data:image/png;base64,{phone_icon_base64}" class="contact">
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)


