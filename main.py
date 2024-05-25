import streamlit as st
from langchain_experimental.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os





# Function to set page title and configure Streamlit page
def set_page():
    st.set_page_config(
        page_title="Ask your CSV 📈",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    st.title("Ask your CSV 📈")

# Function to display file uploader and user input field
def display_input_fields():
    st.sidebar.title("Input")
    csv_file = st.sidebar.file_uploader("Upload a CSV file", type="csv")

    if csv_file is not None:
        try:
            # Display the uploaded CSV file
            st.subheader("Uploaded CSV file:")
            st.write(csv_file)

            # Get user question
            user_question = st.text_input("Ask a question about your CSV: ")

            return csv_file, user_question
        except Exception as e:
            st.error(f"An error occurred while processing the file: {e}")
            return None, None
    else:
        return None, None

# Function to run the agent and display results
def run_agent(csv_file, user_question):
    if csv_file is not None and user_question:
        try:
            # Create CSV agent
            agent = create_csv_agent(OpenAI(temperature=0), csv_file, verbose=True)

            # Run the agent with user question
            with st.spinner("Analyzing..."):
                result = agent.run(user_question)
            
            # Display results
            st.subheader("Results")
            st.write(result)

        except Exception as e:
            st.error(f"An error occurred while processing your question: {e}")

def main():
    set_page()

    # Load environment variables from .env file
    load_dotenv()

    # Load the OpenAI API key from the environment variable
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        st.error("OPENAI_API_KEY is not set. Please set it in your environment.")
        st.stop()

    csv_file, user_question = display_input_fields()
    run_agent(csv_file, user_question)

if __name__ == "__main__":
    main()
