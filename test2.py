# Final streamlined Streamlit cafe menu web app with UI/UX and SEO enhancements

import streamlit as st
import time

# --- Page config with favicon ---
st.set_page_config(
    page_title="Brew & Bite Cafe",
    page_icon="🍵",
    layout="wide"
)

# --- Inject global custom CSS ---
st.markdown("""
    <style>
        html, body, [class*="css"]  {
            font-family: 'Segoe UI', sans-serif;
            background-color: #fff8f2;
        }
        h1, h2, h3 {
            color: #3e2723;
        }
        .stButton>button {
            background-color: #ff7043;
            color: white;
            border-radius: 12px;
            padding: 0.5em 1em;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #ff5722;
        }
        footer {
            visibility: hidden;
        }
        .footer-container {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            text-align: center;
            padding: 10px;
            background-color: #ffe0b2;
            color: #4e342e;
            font-size: 14px;
            z-index: 100;
        }
    </style>
""", unsafe_allow_html=True)

# --- Logo and Navigation ---
col1, col2 = st.columns([1, 9])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/2965/2965567.png", width=60)  # cafe logo
with col2:
    st.title("Brew & Bite Cafe")
    st.caption("Fresh. Fun. Flavorful.")

# --- Simple navigation ---
menu_options = ["Home", "Menu", "About"]
choice = st.selectbox("Navigate", menu_options, index=0, key="nav")

# --- Home Page ---
if choice == "Home":
    st.header("Welcome to Brew & Bite Cafe! 🍽️")
    st.image("https://www.cafeflorista.com/_next/image?url=%2Fimages%2Fcafe%2FIMG-20240922-WA0015.jpg&w=640&q=75", use_container_width=True)
    st.write("""
        Enjoy a delightful experience with mouth-watering dishes, healthy smoothies, and indulgent desserts.
        Our cafe brings flavors from around the world right to your plate!
    """)

# --- About Page ---
elif choice == "About":
    st.header("About Us")
    st.image("https://cdn.pixabay.com/photo/2015/10/30/20/13/coffee-1014535_1280.jpg", width=600)
    st.write("""
        At **Brew & Bite**, we believe food should be fun, fresh, and unforgettable.

        Since 2020, we’ve been serving everything from sizzling starters to hearty mains, fresh smoothies, and sweet endings.

        Our team of chefs pours passion into every bite and blend. Come join us for an experience that tastes as good as it feels.
    """)
    st.subheader("Connect with us")
    st.markdown("""
        <p>
            <a href='https://instagram.com' target='_blank'>🤍 Instagram</a> |
            <a href='https://facebook.com' target='_blank'>💙 Facebook</a> |
            <a href='mailto:contact@brewbite.com'>📧 Email</a>
        </p>
    """, unsafe_allow_html=True)

# --- Menu Page Placeholder ---
elif choice == "Menu":
    st.header("Our Delicious Menu")
    st.info("Menu functionality coming here. Use your previous menu logic or integrate database logic.")

# --- Footer ---
st.markdown("""
    <div class='footer-container'>
        © 2025 Brew & Bite Cafe | Designed with ❤️ by [You]
    </div>
""", unsafe_allow_html=True)
