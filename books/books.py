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

def render_books_page():

    st.markdown("""
<div class="hero">
    <h2>📚 Bookstore</h2>
</div>
""", unsafe_allow_html=True)


    # Use only images that actually exist in your 'assets' folder
    image_list = [
        ("shop1.jpg", "Best-Selling Novels"),
        ("shop5.jpg", "Children's Picture Books")
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
        <p><strong>1- International & Local Books:</strong> A curated selection of bestsellers, classic literature, and contemporary titles from around the world and Pakistan.</p>
        <p><strong>2- Kids’ Picture Books:</strong> Colorful and educational picture books perfect for children, designed to inspire imagination and early learning.</p>
        <p><strong>3- Academic & Leisure Reading:</strong> Explore a full range of textbooks, motivational reads, novels, biographies, and self-help books in a calm reading-friendly environment.</p>
    </div>
    </div>
    """, unsafe_allow_html=True)



