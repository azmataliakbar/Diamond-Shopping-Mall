# shops/shops.py
import streamlit as st
import base64
import os

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def render_shops_page():

    st.markdown("""
<div class="hero">
    <h2>🛍️ Shops Section</h2>
</div>
""", unsafe_allow_html=True)


    # Images and descriptions
    image_list = [
        ("shop.jpg", "Men's Clothing Store"),
        ("shop1.jpg", "Elegant Women's Boutique")
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

    # ✅ This must be inside the function
    st.markdown("""
    <div class="hero">
    <div class="mall-description">
        <p><strong>1- Clothing, Shoes & Sports Stores:</strong> A wide range of branded clothing, trendy footwear, and sportswear — perfect for every age and lifestyle.</p>
        <p><strong>2- Electronics & Mobile Shops:</strong> Explore the latest gadgets, home electronics, and mobile phone accessories from top brands.</p>
        <p><strong>3- Grocery, Books & Services:</strong> One-stop access to grocery stores, book shops, food courts, help desks, and 24/7 security support for a complete mall experience.</p>
    </div>
    </div>
    """, unsafe_allow_html=True)



