# To run the Streamlit app, use the 'streamlit run main.py' command in the terminal

# Import libraries
import spacy  # import spaCy for natural language processing
import streamlit as st  # import Streamlit for creating web applications
import spacy_streamlit as spt  # import spacy_streamlit for visualization

# Load the English language model provided by spaCy
nlp = spacy.load('en_core_web_sm')

# Define the main function
def main():
    # Set the title of the Streamlit application
    st.title('Name Entity Recognition (NER) APP')

    # Create a sidebar menu with options 'Home' and 'NER'
    menu = ['Home', 'NER']
    choice = st.sidebar.selectbox('menu', menu)

    # Check user's choice
    if choice == 'Home':  # if user chooses 'Home'
        # Set subheader for tokenization
        st.subheader('Word Tokenization')

        # Prompt user to enter text for tokenization
        raw_text = st.text_area('Text To Tokenize', 'Enter Text Here')

        # Process the raw text with spaCy
        doc = nlp(raw_text)

        # Check if the 'Tokenize' button is clicked
        if st.button('Tokenize'):
            # Visualize the tokenized text
            spt.visualize_tokens(doc)

    elif choice == 'NER':  # if user chooses 'NER'
        # Set subheader for Named Entity Recognition
        st.subheader('Name Entity Recognition')

        # Prompt user to enter text for NER
        raw_text = st.text_area('Text To Tokenize', 'Enter Text Here')

        # Process the raw text with spaCy
        doc = nlp(raw_text)

        # Visualize the Named Entities
        spt.visualize_ner(doc)

# Run the main function if the script is executed directly
if __name__ == '__main__':
    main()