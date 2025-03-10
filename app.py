import streamlit as st
from ai import ask_ai

def main():
    st.title("Arogya Mitra")

    user_profile = st.text_area("Enter your profile:", 
                                value="30 year old male of height 180 cm and weight 70 kg")
        
    # Health-related query input
    user_input = st.text_area("Enter your health-related query:", value="I'm having fever and headache from 3 days and vomits also")

    if st.button("Submit"):
        if user_input:
            response = ask_ai(user_profile, user_input)
            st.subheader("Response:")
            st.write(response)
        else:
            st.warning("Please enter a query.")

if __name__ == "__main__":
    main()
