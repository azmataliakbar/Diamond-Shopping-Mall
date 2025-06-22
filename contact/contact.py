#  contact.py

import streamlit as st

def render_contact_page():  # ✅ This must match the app.py router
    st.set_page_config(page_title="Contact - Diamond Mall", layout="wide")

    # Load CSS
    with open("styles/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Full Hero-like block
    st.markdown("""
    <div class="hero">
        <h2>📞 Contact Us</h2>
        <p>We'd love to hear from you! Whether it's a question, feedback, or business inquiry, feel free to reach out.</p>
        <div class="mall-description">
            <p><strong>📍 Address:</strong> Diamond Shopping Mall, Main Boulevard, City Center</p>
            <p><strong>📞 Phone:</strong> <a href="tel:+923332236799" style="color:#c084fc;">+92 333 2236799</a></p>
            <p><strong>✉️ Email:</strong> <a href="mailto:info@diamondmall.com" style="color:#c084fc;">info@diamondmall.com</a></p>
            <p><strong>🕒 Hours:</strong> Mon–Sun: 10:00 AM – 10:00 PM</p>
        </div>
    </div>
    """, unsafe_allow_html=True)




