import streamlit as st
import base64
import os

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def render_hero():
    image_names = [
        "shop2.jpg", "shop4.jpg", "shop5.jpg",
        "shop6.jpg"
    ]

    image_html = ""
    for name in image_names:
        img_path = os.path.join("assets", name)
        img_data = get_base64_image(img_path)
        image_html += f'<img src="data:image/jpg;base64,{img_data}" class="shop-img" loading="lazy"/>'


    st.markdown(f"""
    <div class="hero">
        <h1>Diamond Shopping Mall</h1>
        <p>Explore the latest products below.Visit soon for special discount.</p>
        <div class="image-grid">
            {image_html}
    </div>
        <div class="video-section">
            <h2>Watch Shop in our Mall</h2>
            <iframe class="promo-video" src="https://www.youtube.com/embed/sUj9UkZxzpM?si=hJHC2ocltXhkPSwo"
                    title="Promo Video" frameborder="0" allowfullscreen>
            </iframe>
        </div>
    </div>
    """, unsafe_allow_html=True)

