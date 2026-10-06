import streamlit as st

# Page settings
st.set_page_config(
    page_title="Login Page",
    page_icon="🔐",
    layout="centered"
)

# CSS
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #667eea, #764ba2);
}

.login-box {
    background-color: white;
    padding: 40px;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.25);
    margin-top: 80px;
}

.title {
    text-align: center;
    color: #333333;
    font-size: 32px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #777777;
    margin-bottom: 25px;
}

</style>
""", unsafe_allow_html=True)


# Login box
st.markdown('<div class="login-box">', unsafe_allow_html=True)

st.markdown(
    '<div class="title">Welcome Back!</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Login to your account</div>',
    unsafe_allow_html=True
)


# Input fields
email = st.text_input(
    "Email",
    placeholder="Enter your email"
)

password = st.text_input(
    "Password",
    type="password",
    placeholder="Enter your password"
)

remember = st.checkbox("Remember me")


# Login button
if st.button("Login", use_container_width=True):

    if email == "admin@gmail.com" and password == "12345":
        st.success("Login Successful! 🎉")

    else:
        st.error("Invalid email or password!")


st.markdown(
    '<p style="text-align:center;color:#666;">'
    "Don't have an account? Sign Up"
    "</p>",
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)
