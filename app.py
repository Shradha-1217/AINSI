import streamlit as st
import google.generativeai as genai
import os
from datetime import datetime

# Configure page settings
st.set_page_config(
    page_title="AI Fictional Interview Generator",
    page_icon="🎭",
    layout="wide"
)

# Function to setup the Google Gemini Pro model
def setup_model(api_key):
    if not api_key:
        st.error("⚠️ Please enter your Google API Key in the sidebar.")
        st.stop()
    
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-1.5-pro')

# Function to generate interview
def generate_interview(character1, character2, topic, tone, api_key):
    model = setup_model(api_key)
    
    # Create a prompt for the model
    prompt = f"""
    Generate a creative dialogue interview between {character1} and {character2}.
    
    Guidelines:
    - The interview should be about {topic if topic else "any relevant topic that would be interesting for these characters"}.
    - The tone should be {tone}.
    - Include 8-10 exchanges between the characters.
    - Each character should have distinct personality traits and speaking styles that reflect who they are.
    - Format the output as a dialogue script with clear speaker indicators.
    - Make it entertaining, insightful, and reflect the known characteristics/knowledge of these figures.
    
    Output format example:
    {character1}: [First line of dialogue]
    {character2}: [Response]
    {character1}: [Reply]
    ...and so on.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating interview: {str(e)}"

# Sidebar for API Key
with st.sidebar:
    st.title("⚙️ Settings")
    api_key = st.text_input("Enter Google API Key", type="password", help="Get your API key from Google AI Studio (https://makersuite.google.com/)")
    st.markdown("---")
    st.markdown("### About")
    st.markdown("This app uses Google's Gemini 1.5 Pro model to generate creative interviews between any two characters.")
    st.markdown("You need a valid Google API key to use this application.")

# Main app interface
st.title("🎭 AI Fictional Interview Generator")
st.subheader("Generate creative dialogue interviews between any two characters using Google's Gemini 1.5 Pro AI model")

# Example character pairs
st.subheader("Try these example character combinations:")
example_col1, example_col2, example_col3 = st.columns(3)

example_pairs = [
    ("Socrates", "Steve Jobs", "Innovation and Ethics"),
    ("Nikola Tesla", "Tony Stark", "Future of Technology"),
    ("Marie Curie", "Wonder Woman", "Female Empowerment")
]

# Store the current selected character pair
if 'char1' not in st.session_state:
    st.session_state.char1 = ""
if 'char2' not in st.session_state:
    st.session_state.char2 = ""
if 'topic' not in st.session_state:
    st.session_state.topic = ""

# Functions for button clicks to update state
def set_example(char1, char2, topic):
    st.session_state.char1 = char1
    st.session_state.char2 = char2
    st.session_state.topic = topic

# Display example buttons in a more straightforward way
with example_col1:
    if st.button(f"{example_pairs[0][0]} & {example_pairs[0][1]}", key=f"btn1"):
        set_example(*example_pairs[0])

with example_col2:
    if st.button(f"{example_pairs[1][0]} & {example_pairs[1][1]}", key=f"btn2"):
        set_example(*example_pairs[1])

with example_col3:
    if st.button(f"{example_pairs[2][0]} & {example_pairs[2][1]}", key=f"btn3"):
        set_example(*example_pairs[2])

# More examples
example_col4, example_col5, example_col6 = st.columns(3)

more_example_pairs = [
    ("Shakespeare", "Taylor Swift", "Modern Songwriting"),
    ("Albert Einstein", "Yoda", "Space-Time Philosophy"),
    ("Leonardo da Vinci", "Elon Musk", "Future of Art and Technology")
]

with example_col4:
    if st.button(f"{more_example_pairs[0][0]} & {more_example_pairs[0][1]}", key=f"btn4"):
        set_example(*more_example_pairs[0])

with example_col5:
    if st.button(f"{more_example_pairs[1][0]} & {more_example_pairs[1][1]}", key=f"btn5"):
        set_example(*more_example_pairs[1])

with example_col6:
    if st.button(f"{more_example_pairs[2][0]} & {more_example_pairs[2][1]}", key=f"btn6"):
        set_example(*more_example_pairs[2])

st.markdown("---")
st.subheader("Create Your Interview")

# Two-column layout for inputs
col1, col2 = st.columns(2)

with col1:
    character1 = st.text_input("Character 1", value=st.session_state.char1, placeholder="e.g., Albert Einstein")

with col2:
    character2 = st.text_input("Character 2", value=st.session_state.char2, placeholder="e.g., Cleopatra")

# Topic and tone
topic = st.text_input("Topic (Optional)", value=st.session_state.topic, placeholder="e.g., Power & Leadership")
tone = st.selectbox("Tone", options=["Funny", "Dramatic", "Philosophical", "Creative"], index=0)

# Generate button
if st.button("Generate Interview", type="primary"):
    if not character1 or not character2:
        st.error("Please provide both character names.")
    elif not api_key:
        st.error("Please enter your Google API Key in the sidebar.")
    else:
        with st.spinner("Generating interview..."):
            interview = generate_interview(character1, character2, topic, tone, api_key)
        
        st.subheader(f"Interview between {character1} and {character2}")
        
        # Display interview in a box with a clean format
        st.text_area("Interview", interview, height=400)
        
        # Create download button for the interview
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"interview_{character1}_{character2}_{current_time}.txt"
        
        st.download_button(
            label="Download Interview Script",
            data=interview,
            file_name=filename,
            mime="text/plain"
        )

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit and Google's Gemini 1.5 Pro")