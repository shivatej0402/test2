import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Cafe Delight",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="auto"
)

# --- Inject Custom CSS for Enhanced Visuals ---
st.markdown("""
<style>
/* Global styles */
body {
    font-family: 'Segoe UI', sans-serif;
    background-color: #fffdf8;
}

/* Header */
.header {
    text-align: center;
    font-size: 3em;
    color: #4B2E83;
    margin-top: 0.2em;
    margin-bottom: 0.2em;
}

/* Navigation */
.navbar {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin-bottom: 2rem;
    font-size: 1.2em;
    background-color: #fdebd0;
    padding: 1rem;
    border-radius: 1rem;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}
.navbar a {
    color: #4B2E83;
    text-decoration: none;
    font-weight: bold;
    transition: color 0.3s;
}
.navbar a:hover {
    color: #d35400;
}

/* Footer */
footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #fdebd0;
    color: #4B2E83;
    text-align: center;
    padding: 1rem;
    font-size: 0.9em;
    border-top: 1px solid #ccc;
}

/* Image styling */
img {
    border-radius: 1rem;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}
</style>
""", unsafe_allow_html=True)

# --- Logo and Title ---
col1, col2 = st.columns([1, 6])
with col1:
    st.image("logo.png", width=80)
with col2:
    st.markdown("<div class='header'>Cafe Delight ☕</div>", unsafe_allow_html=True)

# --- Navigation Bar ---
st.markdown("""
<div class='navbar'>
    <a href='/?page=home'>Home</a>
    <a href='/?page=menu'>Menu</a>
    <a href='/?page=about'>About</a>
</div>
""", unsafe_allow_html=True)

# --- Routing Logic ---
query_params = st.experimental_get_query_params()
page = query_params.get("page", ["home"])[0]

if page == "home":
    st.image("hero.jpg", use_column_width=True)
    st.markdown("""
    ### Welcome to Cafe Delight 🍰
    Explore a delicious world of snacks, coffee, and good vibes!
    
    - 🍕 Freshly baked pizzas
    - 🥤 Smoothies & Milkshakes
    - 🥗 Healthy bowls & wraps
    - 🍰 Homemade desserts
    """)

    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("smoothie.jpg", caption="Fresh Smoothies")
    with col2:
        st.image("wraps.jpg", caption="Healthy Wraps")
    with col3:
        st.image("dessert.jpg", caption="Delicious Desserts")

elif page == "menu":
    st.markdown("""
    ### Our Menu 📋
    Discover our handcrafted items!
    (This section can be made dynamic with database integration)
    """)

    menu_items = {
        "Starters": ["Garlic Bread", "Cheesy Nachos"],
        "Beverages": ["Lemon Iced Tea", "Caramel Frappe"],
        "Desserts": ["Choco Lava Cake", "Strawberry Tart"]
    }

    for category, items in menu_items.items():
        st.subheader(category)
        for item in items:
            st.markdown(f"- {item} 🍽️")

elif page == "about":
    st.markdown("""
    ### About Us ✨
    Welcome to Cafe Delight – your cozy space to chill, munch, and sip! 😋
    
    Founded in 2024, our cafe blends modern vibes with classic flavors.

    ### Our Team 👨‍🍳
    Passionate foodies, award-winning chefs, and coffee lovers.

    ### Follow us 💬
    [Instagram](https://instagram.com) | [Facebook](https://facebook.com) | [Twitter](https://twitter.com)
    """)

# --- Footer ---
st.markdown("""
<footer>
    Made with ❤️ by Cafe Delight | Connect with us @cafedelight | © 2025
</footer>
""", unsafe_allow_html=True)
