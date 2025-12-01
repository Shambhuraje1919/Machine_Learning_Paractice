
import streamlit as st

st.title("First web page using Streamlit")
st.subheader("This is the sub-header")
st.text("This is the text")

st.markdown("### $E = MC^2$")
st.button("Click Me")

find_your_LPA = st.selectbox(
    "Software Engineer",
    ["Amazon 22 LPA", "Google 30 LPA", "Microsoft 25 LPA"]
)

st.write("You selected:", find_your_LPA)
