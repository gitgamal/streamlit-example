import streamlit as st
import requests
import openai
# Define API endpoint

# Define conversation history file name
conv_file = "conversation_history.txt"

# Check if conversation history file exists or not
try:
    with open(conv_file, mode="r") as f:
        conversation_history = f.read()
except FileNotFoundError:
    conversation_history = ""

# Define Streamlit app
def app():
    st.title("GPT Chat App")
    user_input = st.text_input("Enter your message")

    if st.button("Send"):
        # Send user message to API
        response = requests.post(api_endpoint, json={"message": user_input})

        if response.status_code != 200:
            st.error("Error occurred while processing message")
        else:
            # Get bot response from API
            bot_response = response.json().get("response")
            st.write("Bot says: ", bot_response)

            # Store conversation history
            with open(conv_file, mode="a") as f:
                f.write("User: " + user_input + "\n")
                f.write("Bot: " + bot_response + "\n")

    # Display conversation history
    st.write("---Conversation History---")
    st.write(conversation_history)

if __name__ == "__main__":
    app()
