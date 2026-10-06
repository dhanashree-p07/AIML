import streamlit as st

# -----------------------------
# PAGE SETTINGS
# -----------------------------
st.set_page_config(
    page_title="Login Page",
    page_icon="🔐",
    layout="centered"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

/* Background */
.stApp {
    background-color: #f5f5f5;
}

/* Login box */
.login-box {
    background-color: white;
    padding: 40px;
    border-radius: 15px;
    box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.15);
    margin-top: 60px;
}

/* Title */
.title {
    text-align: center;
    color: #333333;
    font-size: 32px;
    font-weight: bold;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #777777;
    font-size: 16px;
    margin-bottom: 25px;
}

/* Input labels */
label {
    color: #333333 !important;
    font-weight: bold !important;
}

/* Login button */
.stButton > button {
    width: 100%;
    background-color: #4a4a4a;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 12px;
    font-size: 16px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #333333;
    color: white;
}

/* Sign up text */
.signup {
    text-align: center;
    color: #666666;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# LOGIN BOX
# -----------------------------
st.markdown('<div class="login-box">', unsafe_allow_html=True)

# Title
st.markdown(
    '<div class="title">Welcome Back!</div>',
    unsafe_allow_html=True
)

# Subtitle
st.markdown(
    '<div class="subtitle">Login to your account</div>',
    unsafe_allow_html=True
)


# -----------------------------
# EMAIL
# -----------------------------
email = st.text_input(
    "Email",
    placeholder="Enter your email"
)


# -----------------------------
# PASSWORD
# -----------------------------
password = st.text_input(
    "Password",
    type="password",
    placeholder="Enter your password"
)


# -----------------------------
# REMEMBER ME
# -----------------------------
remember = st.checkbox("Remember me")


# -----------------------------
# LOGIN BUTTON
# -----------------------------
if st.button("Login"):

    # Demo login details
    if email == "admin@gmail.com" and password == "12345":

        st.success("Login Successful! 🎉")

    else:

        st.error("Invalid email or password!")


# -----------------------------
# SIGN UP
# -----------------------------
st.markdown(
    '<div class="signup">'
    "Don't have an account? "
    "<b>Sign Up</b>"
    "</div>",
    unsafe_allow_html=True
)

# Close login box
st.markdown("</div>", unsafe_allow_html=True)
