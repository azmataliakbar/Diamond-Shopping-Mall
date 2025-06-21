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
            <img src="data:image/png;base64,{logo_base64}" class="logo">
        </div>
        <div class="nav-links">
            <a href="#">Home</a>
            <a href="#">Shops</a>
            <a href="#">Jewelry</a>
            <a href="#">Books</a>
            <a href="#">Grocery</a>
            <a href="#"> Food Court</a>
            <a href="#">About</a>
            <a href="#">Contact</a>
        </div>
        <div class="contact-icon">
            <a href="tel:+923332236799">
                <img src="data:image/png;base64,{phone_icon_base64}" class="contact">
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
