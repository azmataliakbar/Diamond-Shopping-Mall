# jewelry/jewelry.py
import streamlit as st
import base64
import os

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.warning(f"Image not found: {image_path}")
        return ""

def render_jewelry_page():

    st.markdown("""
<div class="hero">
    <h2>💎 Jewelry Section</h2>
</div>
""", unsafe_allow_html=True)


    image_list = [
        ("shop2.jpg", "Jewelry Set 1"),
        ("shop4.jpg", "Jewelry Set 2")
    ]

    for img_name, caption in image_list:
        img_path = os.path.join("assets", img_name)
        img_data = get_base64_image(img_path)

        if img_data:
            st.markdown(f"""
                <div class="hero">
                <div style="text-align:center; margin: 30px 0;">
                    <img src="data:image/jpg;base64,{img_data}" class="shop-img"/>
                    <p style="font-weight:bold; margin-top:10px;">{caption}</p>
                </div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero">
    <div class="mall-description">
        <p><strong>1- Gold Jewelry:</strong> Elegant and timeless gold sets, bangles, and rings crafted with the finest quality and intricate designs.</p>
        <p><strong>2- Diamond & Artificial Jewelry:</strong> Sparkling diamond pieces and beautifully designed artificial jewelry for every budget and occasion.</p>
        <p><strong>3- Pearls & Diamond Sets:</strong> A graceful collection of pearl and diamond combinations, perfect for weddings, gifts, and luxury events.</p>
    </div>
    </div>
    """, unsafe_allow_html=True)



