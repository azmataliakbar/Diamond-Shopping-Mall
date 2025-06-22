# about/about.py
import streamlit as st
import base64
import os

def get_base64_image(image_path):
    if not os.path.exists(image_path):
        st.error(f"Image file not found: {image_path}")
        return ""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


def render_about_page():

    st.markdown("""
<div class="hero">
    <h2>🏢 About Diamond Shopping Mall</h2>
</div>
""", unsafe_allow_html=True)


    image_list = [
        ("shop.jpg", "Best Shopping Store"),
        ("shop1.jpg", "Elegant Shops & Boutique")
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

    st.markdown("""
    <div class="hero">
    <div class="mall-description">
        <p>
            Welcome to <strong>Diamond Shopping Mall</strong>, a premier destination for shopping, dining, and entertainment.
            We offer a diverse range of experiences to cater to all your needs.
        </p>
        <h3>Our Diverse Offerings:</h3>
        <ul>
            <li><strong>🛍️ Shops:</strong> Explore a wide array of retail outlets featuring local and international brands, from fashion to electronics.</li>
            <li><strong>💎 Jewelry:</strong> Discover exquisite jewelry collections for every occasion.</li>
            <li><strong>📚 Books:</strong> Immerse yourself in the world of literature at our comprehensive bookstores.</li>
            <li><strong>🛒 Grocery:</strong> Find all your daily essentials and gourmet treats at our well-stocked grocery store.</li>
            <li><strong>🍔 Food Court:</strong> Indulge in a culinary journey with a variety of cuisines available at our vibrant food court.</li>
        </ul>
        <p>
            Diamond Shopping Mall is committed to providing a comfortable, enjoyable, and memorable experience for all our visitors.
            We look forward to welcoming you!
        </p>
    </div>
    </div>

""", unsafe_allow_html=True)

