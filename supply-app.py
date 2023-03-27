# Import necessary packages
import streamlit as st

# Create the main function for the web app
def main():
    # Set title of the web app
    st.title("My Streamlit Web App")

    # Add some text to the web app
    st.write("Welcome to my first Streamlit web app!")

    # Add a slider widget to the web app
    age = st.slider("What's your age?", 0, 100, 25)

    # Add a selectbox widget to the web app
    gender = st.selectbox("What's your gender?", ["Male", "Female"])

    # Add a button to the web app
    if st.button("Submit"):
        # Display the user's input
        st.write("Your age:", age)
        st.write("Your gender:", gender)

# Call the main function to run the web app
if __name__ == "__main__":
    main()
