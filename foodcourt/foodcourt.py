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

def render_foodcourt_page():  # ✅ Match this name with the import in app.py
    st.set_page_config(page_title="Food Court - Diamond Mall", layout="wide")
    
    # Load CSS styles
    with open("styles/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Heading
        st.markdown("""
<div class="hero">
    <h2>🍔 Food Court</h2>
</div>
""", unsafe_allow_html=True)
    

    # Food images
    image_list = [
        ("shop9.jpg", "Coffee Zone"),
        ("shop10.jpg", "Excellent sitting arrangement"),
        ("shop11.jpg", "Fast Food")
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

    # ✔️ Add your descriptive text here (inside the function)
    st.markdown("""
        <div class="hero">
        <div class="mall-description">
            <p><strong>☕ Coffee Zone:</strong> Enjoy a range of world-famous coffees like Cappuccino, Espresso, Turkish Coffee, and Latte from top international and local brands.</p>
            <p><strong>🪑 Excellent Sitting Arrangement:</strong> Comfortable seating for families, friends, and individuals with a clean, ambient environment perfect for dining and relaxing.</p>
            <p><strong>🍔 Fast Food:</strong> From burgers and fries to pizza and wraps — indulge in a variety of fast food options for every taste and craving.</p>
        </div>
        </div>
    """, unsafe_allow_html=True)



