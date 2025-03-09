import streamlit as st
from ai import ask_ai

def main():
    st.title("Arogya Mitra")

    user_input = st.text_area("Enter your health-related query:")

    if st.button("Submit"):
        if user_input:
            response = ask_ai(user_input)
            st.subheader("Response:")
            st.write(response)
        else:
            st.warning("Please enter a query.")

if __name__ == "__main__":
    main()
