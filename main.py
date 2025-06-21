import streamlit as st
import base64

# Set page config
st.set_page_config(page_title="My Website", layout="wide")

# Custom CSS (optional)
with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load image and convert to base64
def get_base64_logo(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Path to image
logo_base64 = get_base64_logo("assets/logo.png")
# Second image (phone icon) at right side
phone_icon_base64 = get_base64_logo("assets/callme.png") # or any icon you have

# 1. NAVBAR

st.markdown(f"""
<div class="navbar">
    <div class="logo-container">
        <img src="data:image/png;base64,{logo_base64}" class="logo">
    </div>
    <div class="nav-links">
        <a href="#">Home</a>
        <a href="#">Link1</a>
        <a href="#">Link2</a>
        <a href="#">Link3</a>
        <a href="#">Link4</a>
        <a href="#">Link5</a>
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


# 2. HERO SECTION
st.markdown("""
<div class="hero">
    <h1>Welcome to My Website</h1>
    <p>This is where we talk about AI, Images, and Video.</p>
    <a href="#">Explore More</a>
</div>
""", unsafe_allow_html=True)

# 3. FOOTER
st.markdown("""

<div class="footer">
    <p>© 2025 My Website | Author: Azmat Ali Akbar</p>
</div>
""", unsafe_allow_html=True)