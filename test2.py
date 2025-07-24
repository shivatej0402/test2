# Revamped Streamlit Cafe Menu App with Pro-Grade UI/UX and SEO Enhancements

import streamlit as st
import time

# --- Page Config ---
st.set_page_config(page_title="Brew & Bite Café | Delicious Menu", layout="wide")

# --- Injected CSS for Premium UI/UX ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
    
    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
        scroll-behavior: smooth;
    }

    .stApp {
        background-color: #fff9f5;
    }

    h1, h2, h3 {
        color: #3e2f1c;
    }

    .menu-card {
        background: #ffffff;
        padding: 1rem;
        margin-bottom: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        transition: transform 0.2s ease;
    }

    .menu-card:hover {
        transform: scale(1.02);
    }

    .floating-cart {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: #3e2f1c;
        color: white;
        padding: 15px 20px;
        border-radius: 30px;
        box-shadow: 2px 2px 15px rgba(0,0,0,0.2);
        z-index: 9999;
        font-weight: bold;
        font-size: 16px;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s;
    }

    .floating-cart:hover {
        background-color: #5c4332;
    }

    .category-button {
        font-size: 1.1rem;
        padding: 0.5rem 1rem;
        background-color: #fff0e0;
        border-radius: 10px;
        margin-bottom: 0.5rem;
        font-weight: 600;
        border: none;
        cursor: pointer;
    }

    .category-button:hover {
        background-color: #ffe5cc;
    }
</style>
""", unsafe_allow_html=True)

# --- Metadata (SEO) ---
st.markdown("""
<meta name="description" content="Explore Brew & Bite Café’s curated menu with starters, mains, smoothies, and desserts. Order with ease. Fresh. Delicious. Affordable."/>
<meta property="og:title" content="Brew & Bite Café" />
<meta property="og:description" content="Serving delicious moments since 2020. View our full menu and place your order." />
<meta property="og:image" content="https://www.cafeflorista.com/_next/image?url=%2Fimages%2Fcafe%2FIMG-20240922-WA0015.jpg&w=640&q=75" />
<meta name="twitter:card" content="summary_large_image">
""", unsafe_allow_html=True)

# --- Initialize Session State ---
def init_session():
    for key, val in {
        "page": "home",
        "cart": [],
        "selected_category": None,
        "customer_info": {"name": "", "mobile": ""},
        "order_placed": False,
    }.items():
        if key not in st.session_state:
            st.session_state[key] = val

init_session()

# Placeholder menu data
menu_data = {
    "Starters": [
        {"name": "Paneer Tikka", "price": 150, "image": "https://carveyourcraving.com/wp-content/uploads/2021/10/paneer-tikka-skewers.jpg"},
        {"name": "Chicken Lollipop", "price": 160, "image": "https://www.bradleysmoker.com/cdn/shop/files/Screen-Shot-2021-08-19-at-11_26_55-AM.png?v=6727898055398431908"},
    ],
    "Smoothies": [
        {"name": "Mango Smoothie", "price": 80, "image": "https://vaya.in/recipes/wp-content/uploads/2017/09/Mango-Smoothie_1-1.jpg"},
        {"name": "Chocolate Banana", "price": 90, "image": "https://www.ambitiouskitchen.com/wp-content/uploads/fly-images/52949/Chocolate-Peanut-Butter-Banana-Smoothie-5-500x375-c.jpg"},
    ],
}

# --- Home Page ---
if st.session_state.page == "home":
    st.image("https://www.cafeflorista.com/_next/image?url=%2Fimages%2Fcafe%2FIMG-20240922-WA0015.jpg&w=640&q=75", use_container_width=True)
    st.title("☕ Welcome to Brew & Bite Café")
    st.subheader("Serving delicious food since 2020 🍽️")
    st.write("Explore our wide variety of dishes, from starters to desserts. Fresh, tasty, and crafted with love.")
    if st.button("View Menu", use_container_width=True):
        st.session_state.page = "menu"
        st.rerun()

# --- Menu Page ---
elif st.session_state.page == "menu":
    st.sidebar.title("🛒 Your Cart")
    total = 0
    for item in st.session_state.cart:
        subtotal = item['price'] * item['qty']
        total += subtotal
        st.sidebar.write(f"{item['qty']} x {item['name']} = ₹{subtotal}")

    st.sidebar.markdown(f"**Total: ₹{total}**")
    name = st.sidebar.text_input("👤 Name", value=st.session_state.customer_info["name"])
    mobile = st.sidebar.text_input("📱 Mobile", value=st.session_state.customer_info["mobile"])
    if st.sidebar.button("Proceed to Checkout"):
        st.session_state.customer_info["name"] = name
        st.session_state.customer_info["mobile"] = mobile
        st.session_state.page = "checkout"
        st.rerun()

    st.header("📂 Select a Category")
    for category in menu_data:
        if st.button(f"🍽️ {category}", use_container_width=True, key=f"cat_{category}"):
            st.session_state.selected_category = category

    selected = st.session_state.selected_category
    if selected:
        st.subheader(f"🍴 {selected}")
        for item in menu_data[selected]:
            with st.container():
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.image(item['image'], width=150)
                with col2:
                    st.markdown(f"<div class='menu-card'><strong>{item['name']}</strong><br>💰 ₹{item['price']}</div>", unsafe_allow_html=True)
                    qty = st.number_input(f"Qty - {item['name']}", 1, 10, 1, key=f"qty_{item['name']}")
                    if st.button(f"Add {item['name']} to Cart", key=f"add_{item['name']}"):
                        st.session_state.cart.append({**item, "qty": qty})
                        st.success(f"✅ {item['name']} added to cart")

    if st.button("⬅️ Back to Home"):
        st.session_state.page = "home"
        st.rerun()

    # Floating Cart Button
    total_items = sum(i['qty'] for i in st.session_state.cart)
    if total_items > 0:
        st.markdown(f"""
            <div class="floating-cart" onclick="document.getElementById('goto_checkout').click();">
                🛒 {total_items} item(s) | ₹{total}
            </div>
        """, unsafe_allow_html=True)
        if st.button("", key="goto_checkout"):
            st.session_state.page = "checkout"
            st.rerun()

# --- Checkout Page ---
elif st.session_state.page == "checkout":
    st.title("🧾 Order Summary")
    st.markdown(f"👤 **{st.session_state.customer_info['name']}**")
    st.markdown(f"📱 **{st.session_state.customer_info['mobile']}**")
    st.markdown("---")
    total = 0
    for item in st.session_state.cart:
        subtotal = item['price'] * item['qty']
        total += subtotal
        st.write(f"{item['qty']} x {item['name']} = ₹{subtotal}")
    st.markdown(f"### Total: ₹{total}")

    if st.button("✅ Confirm Order"):
        st.success("🎉 Order placed successfully!")
        st.session_state.cart.clear()
        st.session_state.page = "home"
        time.sleep(2)
        st.rerun()

    if st.button("⬅️ Modify Cart"):
        st.session_state.page = "menu"
        st.rerun()
