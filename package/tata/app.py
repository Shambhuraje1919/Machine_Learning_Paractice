import streamlit as st

st.title("First web page using Streamlit")
st.subheader("This is the sub-header")
st.text("This is the text")

st.markdown("### $E = MC^2$")
st.button("Click Me")
st.checkbox("I agree to the terms and conditions")
st.text_input("Enter your name", "Type here...")
st.slider("Select a value", 0, 100, 25)

find_your_LPA = st.selectbox(
    "Software Engineer",
    ["Amazon 22 LPA", "Google 30 LPA", "Microsoft 25 LPA"]
)

st.write("You selected:", find_your_LPA)