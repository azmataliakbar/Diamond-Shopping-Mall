import streamlit as st
import base64
import os

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.warning(f"⚠️ Image not found: {image_path}")
        return ""

def render_grocery_page():  # ✅ Must match what you're importing in app.py
    st.set_page_config(page_title="Grocery - Diamond Mall", layout="wide")

    # Load styles
    with open("styles/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.markdown("""
<div class="hero">
    <h2>🛒 Grocery Section</h2>
</div>
""", unsafe_allow_html=True)


    # Images and captions
    image_list = [
        ("shop6.jpg", "Fresh Fruits"),
        ("shop8.jpg", "Fresh Vegetables"),
        ("shop7.jpg", "Daily Essentials")
    ]

    for img_name, caption in image_list:
        img_path = os.path.join("assets", img_name)
        img_data = get_base64_image(img_path)
        st.markdown(f"""
            <div class="hero">
            <div style="text-align:center; margin: 30px 0;">
                <img src="data:image/jpg;base64,{img_data}" class="shop-img"/>
                <p style="font-weight:bold; margin-top:10px;">{caption}</p>
            </div>
            </div>
        """, unsafe_allow_html=True)

    # 🔄 Replace st.write() with styled markdown
    st.markdown("""
    <div class="hero">
    <div class="mall-description">
        <p><strong>1- Fresh Fruits:</strong> Handpicked seasonal fruits delivered daily — juicy, ripe, and full of flavor for a healthy lifestyle.</p>
        <p><strong>2- Fresh Vegetables:</strong> Locally sourced greens and vegetables, washed and packed with care to ensure freshness and nutrition.</p>
        <p><strong>3- Grocery & Dairy Products:</strong> A complete range of essentials including pulses, rice, snacks, milk, butter, yogurt, and other fresh dairy products under one roof.</p>
    </div>
    </div>
    """, unsafe_allow_html=True)


