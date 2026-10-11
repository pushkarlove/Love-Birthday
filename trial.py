import streamlit as st
import time

# Page Configuration
st.set_page_config(
    page_title="Happy Birthday Sneh ❤️",
    page_icon="🎂",
    layout="centered"
)

# Custom Styling, Modern Loading Screen, Password Box & Spiral Animations
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@300;400;600;700&display=swap');

        /* Background Styling */
        .stApp {
            background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
            font-family: 'Poppins', sans-serif;
            color: #ffffff;
        }

        h1, h2, h3 {
            font-family: 'Pacifico', cursive;
            color: #ff758c;
            text-align: center;
        }

        /* Modern Glassmorphism Card */
        .glass-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            text-align: center;
            max-width: 480px;
            margin: 50px auto;
        }

        /* Love Note / Message Box */
        .love-message-box {
            background: rgba(255, 117, 140, 0.15);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 117, 140, 0.4);
            border-radius: 20px;
            padding: 25px;
            margin: 30px auto;
            text-align: center;
            box-shadow: 0 10px 30px rgba(255, 117, 140, 0.25);
        }

        .love-message-box p {
            font-size: 16px;
            line-height: 1.8;
            color: #fce4ec;
            font-weight: 400;
        }

        /* Shatter & Spiral Animation for Photos */
        @keyframes shatterSpiral {
            0% {
                opacity: 0;
                transform: scale(0.1) rotate(720deg) translate(300px, -300px);
                filter: blur(10px);
            }
            50% {
                opacity: 0.5;
                transform: scale(0.8) rotate(360deg) translate(-50px, 50px);
                filter: blur(2px);
            }
            100% {
                opacity: 1;
                transform: scale(1) rotate(0deg) translate(0, 0);
                filter: blur(0px);
            }
        }

        /* Animated Photo Cards Container */
        .spiral-card {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            padding: 12px;
            border-radius: 18px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 10px 25px rgba(255, 117, 140, 0.3);
            animation: shatterSpiral 1.8s cubic-bezier(0.25, 1, 0.5, 1) forwards;
            margin-bottom: 25px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .spiral-card:hover {
            transform: scale(1.04);
            box-shadow: 0 15px 35px rgba(255, 117, 140, 0.5);
        }

        /* Glowing Text */
        .glow-text {
            text-shadow: 0 0 10px #ff758c, 0 0 20px #ff758c;
        }
    </style>
""", unsafe_allow_html=True)

# Session States
if "loaded" not in st.session_state:
    st.session_state.loaded = False

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# STEP 1: Trending Loader Screen
if not st.session_state.loaded:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("<h2 class='glow-text'>✨ Initializing Magical Universe...</h2>", unsafe_allow_html=True)

    progress_text = st.empty()
    progress_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.01)
        progress_bar.progress(percent_complete + 1)
        progress_text.markdown(
            f"<p style='text-align:center; font-weight:600;'>Loading Pure Love... {percent_complete + 1}%</p>",
            unsafe_allow_html=True)

    st.session_state.loaded = True
    time.sleep(0.2)
    st.rerun()


# STEP 2: Password Gate Screen
elif not st.session_state.authenticated:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("<h2 class='glow-text'>🔒 Special Access</h2>", unsafe_allow_html=True)
    st.markdown(
        "<p style='color: #e0e0e0;'>Yeh khoobsurat safar sirf meri Sneh ke liye hai. Apna secret passcode enter karo:</p>",
        unsafe_allow_html=True)

    password = st.text_input("Passcode Required", type="password", key="pass_input")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Unlock My Heart ✨", use_container_width=True):
            if password == "081126":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Access Denied! Galat passcode 💔")
    st.markdown('</div>', unsafe_allow_html=True)


# STEP 3: Main Birthday Celebration (After Password Unlock)
else:
    st.markdown("<h1 class='glow-text'>🎉 Happy Birthday, My Kareja Sneh! 🎂</h1>", unsafe_allow_html=True)
    st.markdown(
        "<h3 style='text-align: center; color: #ffb199;'>✨ 8th November - The most special day of my life ✨</h3>",
        unsafe_allow_html=True)
    st.write("")

    # Heartfelt Love & Birthday Message Section
    st.markdown("""
        <div class="love-message-box">
            <h3 style="color: #ff758c; margin-bottom: 10px; font-family: 'Pacifico', cursive;">To My Everything, Sneh ❤️</h3>
            <p>
                Tum meri zindagi ka woh sabse haseen hissa ho jise paane ke baad mujhe kuch aur nahi chahiye. 
                Tumhari yeh muskurahat, tumhara yeh gussa, tumhara har ek andaz mere dil ke sabse kareeb hai.<br><br>
                Main tumse behad pyar karta hoon, aur yeh sirf ek lafz nahi, meri rooh ka ehsaas hai. 
                Aaj tumhara birthday hai, aur main chahta hoon ki tumhe yeh mehsoos ho ki duniya ka chahe koi bhi kona ho, 
                yeh dil hamesha sirf aur sirf tumhare liye dhadakta hai. Tum meri jaan ho, meri duniya ho!<br><br>
                Hamesha aise hi muskurati raho, aur meri zindagi ko roshan karti raho. Happy Birthday, my love! 💖
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.markdown("<h3 style='text-align: center; color: #ff758c;'>✨ Kuch Yaadein Jo Humari Duniya Hain ✨</h3>",
                unsafe_allow_html=True)
    st.write("")

    # List of images inside the 'Kareja/' folder
    image_paths = [
        "Kareja/jpg 01.jpg",
        "Kareja/jpg 02.jpg",
        "Kareja/jpg 03.jpg",
        "Kareja/jpg 04.jpg",
        "Kareja/jpg 05.jpg",
        "Kareja/jpg 06.jpg"
    ]

    # Display images in 2-column layout with Shatter-to-Spiral Animation
    col1, col2 = st.columns(2)

    for index, img_path in enumerate(image_paths):
        target_column = col1 if index % 2 == 0 else col2
        with target_column:
            st.markdown('<div class="spiral-card">', unsafe_allow_html=True)
            try:
                st.image(img_path, use_column_width=True)
            except Exception:
                st.warning(f"Image load hone mein dikkat hai: {img_path}")
            st.markdown('</div>', unsafe_allow_html=True)

    st.write("")
    st.markdown(
        "<h3 style='text-align: center; color: #ff758c; margin-top: 40px;' class='glow-text'> You mean the absolute world to me! Forever yours 💖</h3>",
        unsafe_allow_html=True)