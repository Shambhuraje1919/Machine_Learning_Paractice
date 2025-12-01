import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
st.title("Hello Software Engineer")
st.write("How much will your LPA be in 5 years?")
Salary_with_compnay = st.selectbox("Select your company and package", ["google 30LPA", "amazon 25LPA", "microsoft 28LPA", "apple 35LPA"])
st.write("Congratulations for ", Salary_with_compnay)
st.success( Salary_with_compnay,icon="✅")
st.balloons()
st.write("Thank you for using our app!")
st.snow()
st.text("Code is like humor. When you have to explain it,")
###st.page_config(page_title="LPA Predictor", page_icon=":computer:", layout="centered")
name = st.text_input("Enter your name")

st.button("Submit")
st.write("Your name is:", name , "the great software engineer At!", Salary_with_compnay)

df = pd.DataFrame({
    'Year': [1, 2, 3, 4, 5],
    'LPA': [10, 25, 20, 40, 30]
})
st.line_chart(df.set_index('Year'))
st.area_chart(df.set_index('Year'))
st.bar_chart(df.set_index('Year'))
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

age = st.slider("Select your age", 18, 60, 25)
st.write("Your age is:", age)

st.write("to a 5-year-old.")
st.write("to a 5-year-old.")
#import streamlit as st
import random
import time

st.write("Streamlit loves LLMs! 🤖 [Build your own chat app](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps) in minutes, then make it powerful by adding images, dataframes, or even input widgets to the chat.")

st.caption("Note that this demo app isn't actually connected to any LLMs. Those are expensive ;)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Let's start chatting! 👇"}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        assistant_response = random.choice(
            [
                "Hello there! How can I assist you today?",
                "Hi, human! Is there anything I can help you with?",
                "Do you need help?",
            ]
        )
        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})


