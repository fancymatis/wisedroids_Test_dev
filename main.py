import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def set_openai_api_key(api_key):
    """Set the OpenAI API key as an environment variable for the current session."""
    os.environ["OPENAI_API_KEY"] = api_key
    return api_key != ""

def main():
    st.set_page_config(page_title="Test Agent App", layout="wide")
    
    # Sidebar for API key input
    st.sidebar.title("Authentication")
    api_key = st.sidebar.text_input(
        "Enter your OpenAI API key:",
        type="password",
        help="Your API key is not stored and is only used for the current session."
    )
    
    if api_key:
        if set_openai_api_key(api_key):
            st.sidebar.success("API key set successfully!")
            
            # Main application content
            st.title("Test Agent Application")
            st.write("This is a test agent application.")
            
            # Original functionality
            if st.button("Run Test Agent"):
                try:
                    st.write("test agent")
                    st.success("Test agent executed successfully!")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        else:
            st.sidebar.error("Please enter a valid API key.")
    else:
        # Instructions when no API key is provided
        st.title("Welcome to the Test Agent Application")
        st.write("Please enter your OpenAI API key in the sidebar to get started.")
        st.info("Your API key is required to use this application. It will only be used for the current session and will not be stored.")

if __name__ == "__main__":
    main()
