import streamlit as st
from streamlit_option_menu import option_menu
from utils.auth import login
from utils.tone_detect import detect_skin_tone
from utils.product_api import fetch_products_by_tone
from utils.chat_assistant import assistant_reply
import streamlit_folium as stf
import folium
from PIL import Image

# Load custom CSS

# Authenticator
authenticator = login()
name, auth_status, username = authenticator.login("Login", "main")

if not auth_status:
    st.warning("Please log in to continue.")
    st.stop()
authenticator.logout("Logout", "sidebar")

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        menu_title="Makeup App",
        options=["Home", "Skin Tone & Products", "Store Locator", "Chat Assistant", "Profile"],
        icons=["house", "palette", "geo-alt", "chat", "person"],
        menu_icon="heart",
        default_index=0,
    )

if selected == "Home":
    st.image("assets/logo.png", width=120)
    st.title("Welcome to GlamorMate 💄")
    st.write("Get personalized makeup recommendations just for you. Start by scanning your skin tone!")

elif selected == "Skin Tone & Products":
    st.title("📸 Detect Skin Tone & Get Product Suggestions")
    img_file = st.camera_input("Take a selfie")
    if img_file:
        image = Image.open(img_file)
        tone = detect_skin_tone(image)
        st.success(f"Detected Skin Tone: **{tone}**")

        st.subheader("Recommended Products:")
        products = fetch_products_by_tone(tone)
        for p in products:
            with st.container():
                st.markdown(f"**{p.get('name', 'No Name')}**")
                st.image(p.get("image_link", "https://via.placeholder.com/150"), width=100)
                st.markdown(f"{p.get('description', 'No description available.')}")
                st.markdown(f"[View Product]({p.get('product_link', '#')})")

elif selected == "Store Locator":
    st.title("🗺️ Find Stores Near You")
    m = folium.Map(location=[12.9716, 77.5946], zoom_start=13)
    folium.Marker([12.975, 77.595], popup="Nykaa Store").add_to(m)
    folium.Marker([12.968, 77.591], popup="Lakmé Salon").add_to(m)
    stf.folium_static(m)

elif selected == "Chat Assistant":
    st.title("💬 Ask Your Makeup Assistant")
    st.markdown("Ask for help with makeup tips, skincare routines, or product suggestions!")
    user_input = st.text_input("Your question:")
    if user_input:
        response = assistant_reply(user_input)
        st.markdown(f"**Assistant:** {response}")

elif selected == "Profile":
    st.title("👤 Your Profile")
    st.markdown(f"**Name:** {name}")
    st.markdown(f"**Username:** {username}")
    st.markdown("More profile features coming soon!")

st.markdown("---")
st.markdown("<center>© 2025 GlamorMate. All rights reserved.</center>", unsafe_allow_html=True)
