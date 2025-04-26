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

# Custom CSS for better styling
st.markdown("""
<style>
    .main {
        background-color: #f9f9f9;
    }
    h1 {
        color: #1E3A8A;
        font-size: 42px !important;
        text-align: center;
        margin-bottom: 10px !important;
    }
    h2 {
        color: #2563EB;
    }
    h3 {
        color: #3B82F6;
    }
    .stButton>button {
        background-color: #3B82F6;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 500;
        border: none;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #2563EB;
        transform: translateY(-2px);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .example-card {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-bottom: 15px;
        transition: all 0.3s;
        border: 1px solid #e5e7eb;
    }
    .example-card:hover {
        box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
        transform: translateY(-5px);
    }
    .stTextInput>div>div>input {
        border-radius: 8px;
        border: 1px solid #d1d5db;
        padding: 10px;
    }
    .generated-interview {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-top: 20px;
        border: 1px solid #e5e7eb;
    }
    .interview-header {
        background-color: #EFF6FF;
        padding: 10px 15px;
        border-radius: 8px;
        margin-bottom: 15px;
        color: #1E40AF;
        font-weight: 600;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #EFF6FF;
        border-radius: 8px;
        padding: 10px 20px;
        color: #3B82F6;
    }
    .stTabs [aria-selected="true"] {
        background-color: #3B82F6;
        color: white;
    }
    .sidebar .css-6qob1r {
        background-color: #F3F4F6;
    }
    .css-1d391kg {
        background-color: #F3F4F6;
    }
    .stTextArea > div > div > textarea {
        background-color: #f8fafc;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
    }
    .css-1cypcdb {
        background-color: #2563EB;
        color: white;
    }
    .divider {
        border-top: 1px solid #e5e7eb;
        margin: 20px 0;
    }
    .primary-button {
        background-color: #2563EB;
        color: white;
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
        font-weight: 500;
        width: 100%;
    }
    .download-button {
        background-color: #10B981;
        color: white;
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
        font-weight: 500;
        width: 100%;
    }
    .tone-option {
        background-color: white;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 10px;
        cursor: pointer;
        border: 1px solid #e5e7eb;
        transition: all 0.2s;
    }
    .tone-option:hover {
        border-color: #3B82F6;
        transform: translateY(-2px);
    }
    .tone-option.selected {
        border-color: #3B82F6;
        background-color: #EFF6FF;
    }
    .tone-icon {
        font-size: 24px;
        margin-bottom: 5px;
    }
</style>
""", unsafe_allow_html=True)

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

# Sidebar for API Key with enhanced styling
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <h2 style="color: #1E40AF;">⚙️ Settings</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # API Key input with improved styling
    st.markdown("""
    <div style="background-color: #EFF6FF; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
        <h4 style="color: #1E40AF; margin-top: 0;">API Credentials</h4>
        <p style="font-size: 0.9rem; color: #4B5563; margin-bottom: 10px;">
            Enter your Google API key to use the Gemini 1.5 Pro model
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    api_key = st.text_input(
        "Google API Key", 
        type="password", 
        help="Get your API key from Google AI Studio (https://makersuite.google.com/)"
    )
    
    # Show status based on whether API key is provided
    if api_key:
        st.success("✅ API Key provided")
    else:
        st.warning("⚠️ API Key required to generate interviews")
    
    st.markdown("<hr style='margin: 30px 0; border-color: #E5E7EB;'>", unsafe_allow_html=True)
    
    # About section with improved styling
    st.markdown("""
    <div style="background-color: #EFF6FF; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
        <h4 style="color: #1E40AF; margin-top: 0;">About This App</h4>
        <p style="font-size: 0.9rem; color: #4B5563; margin-bottom: 10px;">
            This creative tool uses Google's Gemini 1.5 Pro model to generate fictional interviews between any two characters you can imagine!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Instructions
    st.markdown("""
    <div style="background-color: #EFF6FF; padding: 15px; border-radius: 10px;">
        <h4 style="color: #1E40AF; margin-top: 0;">How To Use</h4>
        <ol style="font-size: 0.9rem; color: #4B5563; padding-left: 20px; margin-bottom: 0;">
            <li>Enter your Google API key above</li>
            <li>Select a pre-made character pair or create your own</li>
            <li>Choose a tone for the conversation</li>
            <li>Click Generate to create your interview!</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

# Main app interface with enhanced header
st.markdown("""
<div style="text-align: center; padding: 20px 0;">
    <h1>🎭 AI Fictional Interview Generator</h1>
    <p style="font-size: 1.2rem; color: #4B5563; margin-bottom: 30px;">
        Create imaginative dialogues between any characters using Google's Gemini 1.5 Pro AI
    </p>
</div>
""", unsafe_allow_html=True)

# Store the current selected character pair
if 'char1' not in st.session_state:
    st.session_state.char1 = ""
if 'char2' not in st.session_state:
    st.session_state.char2 = ""
if 'topic' not in st.session_state:
    st.session_state.topic = ""
if 'tone' not in st.session_state:
    st.session_state.tone = "Funny"

# Functions for button clicks to update state
def set_example(char1, char2, topic):
    st.session_state.char1 = char1
    st.session_state.char2 = char2
    st.session_state.topic = topic
    st.rerun()

# Container for character pair examples
st.markdown("""
<h3 style="margin-bottom: 20px; color: #3B82F6; text-align: center;">
    Select from popular character combinations
</h3>
<p style="text-align: center; color: #6B7280; margin-bottom: 20px;">
    Featuring combinations from world history, pop culture, and Indian mythology
</p>
""", unsafe_allow_html=True)

# First row of examples
example_pairs = [
    ("Socrates", "Steve Jobs", "Innovation and Ethics"),
    ("Nikola Tesla", "Tony Stark", "Future of Technology"),
    ("Marie Curie", "Wonder Woman", "Female Empowerment")
]

example_col1, example_col2, example_col3 = st.columns(3)

# Display example cards with enhanced styling
with example_col1:
    st.markdown(f"""
    <div class="example-card">
        <h4 style="color: #2563EB; margin-bottom: 5px;">{example_pairs[0][0]} & {example_pairs[0][1]}</h4>
        <p style="color: #6B7280; font-size: 0.9rem; margin-bottom: 10px;">Topic: {example_pairs[0][2]}</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button(f"Select Pair", key=f"btn1"):
        set_example(*example_pairs[0])

with example_col2:
    st.markdown(f"""
    <div class="example-card">
        <h4 style="color: #2563EB; margin-bottom: 5px;">{example_pairs[1][0]} & {example_pairs[1][1]}</h4>
        <p style="color: #6B7280; font-size: 0.9rem; margin-bottom: 10px;">Topic: {example_pairs[1][2]}</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button(f"Select Pair", key=f"btn2"):
        set_example(*example_pairs[1])

with example_col3:
    st.markdown(f"""
    <div class="example-card">
        <h4 style="color: #2563EB; margin-bottom: 5px;">{example_pairs[2][0]} & {example_pairs[2][1]}</h4>
        <p style="color: #6B7280; font-size: 0.9rem; margin-bottom: 10px;">Topic: {example_pairs[2][2]}</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button(f"Select Pair", key=f"btn3"):
        set_example(*example_pairs[2])

# Second row of examples
more_example_pairs = [
    ("Krishna", "Arjuna", "Duty and Dharma"),
    ("Rama", "Ravana", "Ethics of Leadership"),
    ("Leonardo da Vinci", "Elon Musk", "Future of Art and Technology")
]

example_col4, example_col5, example_col6 = st.columns(3)

with example_col4:
    st.markdown(f"""
    <div class="example-card">
        <h4 style="color: #2563EB; margin-bottom: 5px;">{more_example_pairs[0][0]} & {more_example_pairs[0][1]}</h4>
        <p style="color: #6B7280; font-size: 0.9rem; margin-bottom: 10px;">Topic: {more_example_pairs[0][2]}</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button(f"Select Pair", key=f"btn4"):
        set_example(*more_example_pairs[0])

with example_col5:
    st.markdown(f"""
    <div class="example-card">
        <h4 style="color: #2563EB; margin-bottom: 5px;">{more_example_pairs[1][0]} & {more_example_pairs[1][1]}</h4>
        <p style="color: #6B7280; font-size: 0.9rem; margin-bottom: 10px;">Topic: {more_example_pairs[1][2]}</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button(f"Select Pair", key=f"btn5"):
        set_example(*more_example_pairs[1])

with example_col6:
    st.markdown(f"""
    <div class="example-card">
        <h4 style="color: #2563EB; margin-bottom: 5px;">{more_example_pairs[2][0]} & {more_example_pairs[2][1]}</h4>
        <p style="color: #6B7280; font-size: 0.9rem; margin-bottom: 10px;">Topic: {more_example_pairs[2][2]}</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button(f"Select Pair", key=f"btn6"):
        set_example(*more_example_pairs[2])

# Third row of examples from Indian history and mythology
st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
example_col7, example_col8, example_col9 = st.columns(3)

indian_examples = [
    ("Emperor Akbar", "Birbal", "Wit and Wisdom"),
    ("Shiva", "Parvati", "Divine Partnership"),
    ("Chanakya", "Chandragupta Maurya", "Statecraft and Politics")
]

with example_col7:
    st.markdown(f"""
    <div class="example-card">
        <h4 style="color: #2563EB; margin-bottom: 5px;">{indian_examples[0][0]} & {indian_examples[0][1]}</h4>
        <p style="color: #6B7280; font-size: 0.9rem; margin-bottom: 10px;">Topic: {indian_examples[0][2]}</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button(f"Select Pair", key=f"btn7"):
        set_example(*indian_examples[0])

with example_col8:
    st.markdown(f"""
    <div class="example-card">
        <h4 style="color: #2563EB; margin-bottom: 5px;">{indian_examples[1][0]} & {indian_examples[1][1]}</h4>
        <p style="color: #6B7280; font-size: 0.9rem; margin-bottom: 10px;">Topic: {indian_examples[1][2]}</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button(f"Select Pair", key=f"btn8"):
        set_example(*indian_examples[1])

with example_col9:
    st.markdown(f"""
    <div class="example-card">
        <h4 style="color: #2563EB; margin-bottom: 5px;">{indian_examples[2][0]} & {indian_examples[2][1]}</h4>
        <p style="color: #6B7280; font-size: 0.9rem; margin-bottom: 10px;">Topic: {indian_examples[2][2]}</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button(f"Select Pair", key=f"btn9"):
        set_example(*indian_examples[2])

# Divider with styling
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

# Custom Interview Creation section
st.markdown("""
<h3 style="margin-bottom: 20px; color: #3B82F6; text-align: center;">
    Create Your Custom Interview
</h3>
""", unsafe_allow_html=True)

# Enhanced character input section
input_col1, input_col2 = st.columns(2)

with input_col1:
    st.markdown("""
    <div style="background-color: #EFF6FF; padding: 10px 15px; border-radius: 8px; margin-bottom: 10px;">
        <h4 style="color: #1E40AF; margin: 0;">Character 1</h4>
    </div>
    """, unsafe_allow_html=True)
    character1 = st.text_input("Enter name", value=st.session_state.char1, placeholder="e.g., Albert Einstein", key="char1_input")

with input_col2:
    st.markdown("""
    <div style="background-color: #EFF6FF; padding: 10px 15px; border-radius: 8px; margin-bottom: 10px;">
        <h4 style="color: #1E40AF; margin: 0;">Character 2</h4>
    </div>
    """, unsafe_allow_html=True)
    character2 = st.text_input("Enter name", value=st.session_state.char2, placeholder="e.g., Cleopatra", key="char2_input")

# Topic input with styling
st.markdown("""
<div style="background-color: #EFF6FF; padding: 10px 15px; border-radius: 8px; margin-bottom: 10px;">
    <h4 style="color: #1E40AF; margin: 0;">Interview Topic</h4>
</div>
""", unsafe_allow_html=True)
topic = st.text_input("What should they discuss? (Optional)", value=st.session_state.topic, placeholder="e.g., Power & Leadership")

# Tone selection with visual options
st.markdown("""
<div style="background-color: #EFF6FF; padding: 10px 15px; border-radius: 8px; margin-bottom: 10px;">
    <h4 style="color: #1E40AF; margin: 0;">Conversation Tone</h4>
</div>
""", unsafe_allow_html=True)

# Initialize tone with session state or default
tone = st.session_state.tone

# Visual tone selector
tone_cols = st.columns(4)
tone_options = ["Funny", "Dramatic", "Philosophical", "Creative"]
tone_icons = ["😂", "😲", "🧠", "✨"]
tone_descriptions = [
    "Humorous dialogue", 
    "Emotional exchanges", 
    "Deep conversations", 
    "Imaginative ideas"
]

# Set the selected class based on the current tone
for i, (t_col, t_option, t_icon, t_desc) in enumerate(zip(tone_cols, tone_options, tone_icons, tone_descriptions)):
    with t_col:
        is_selected = tone == t_option
        selected_class = "selected" if is_selected else ""
        
        st.markdown(f"""
        <div class="tone-option {selected_class}">
            <div class="tone-icon">{t_icon}</div>
            <div><strong>{t_option}</strong></div>
            <div style="font-size: 0.8rem; color: #6B7280;">{t_desc}</div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(t_option, key=f"tone_{t_option}"):
            tone = t_option
            st.session_state.tone = tone

# Generate button with a more attractive styling
st.markdown("<div style='margin: 30px 0;'></div>", unsafe_allow_html=True)
generate_col1, generate_col2, generate_col3 = st.columns([1, 2, 1])

with generate_col2:
    st.markdown("""
    <div style="text-align: center; margin-bottom: 10px;">
        <p style="color: #6B7280;">Ready to create your fictional interview?</p>
    </div>
    """, unsafe_allow_html=True)
    generate_interview_clicked = st.button("✨ Generate Interview", type="primary", use_container_width=True)

# Create a container for the interview result
interview_container = st.container()

# Store the interview in session state
if 'interview' not in st.session_state:
    st.session_state.interview = None
if 'current_chars' not in st.session_state:
    st.session_state.current_chars = {"char1": "", "char2": "", "topic": "", "tone": ""}

# Display validation messages or process the interview generation
if generate_interview_clicked:
    if not character1 or not character2:
        st.error("Please provide both character names.")
    elif not api_key:
        st.error("Please enter your Google API Key in the sidebar.")
    else:
        # Show a styled progress message
        progress_message = st.empty()
        progress_message.markdown("""
        <div style="text-align: center; padding: 20px; background-color: #EFF6FF; border-radius: 10px; margin: 20px 0;">
            <h3 style="color: #1E40AF; margin-bottom: 10px;">🧠 Creating Your Interview</h3>
            <p>Using Gemini 1.5 Pro to generate a creative dialogue between your characters...</p>
            <div style="margin-top: 10px; width: 100%; height: 4px; background-color: #E0E7FF; border-radius: 2px; overflow: hidden;">
                <div id="progress-bar" style="width: 0%; height: 100%; background-color: #3B82F6; border-radius: 2px;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Generate the interview
        with st.spinner(""):
            interview = generate_interview(character1, character2, topic, tone, api_key)
            st.session_state.interview = interview
            st.session_state.current_chars = {"char1": character1, "char2": character2, "topic": topic, "tone": tone}
        
        # Clear the progress message
        progress_message.empty()
        
        # Rerun to show the result in a cleaner way
        st.rerun()

# Display the interview if it exists in session state
if st.session_state.interview:
    interview = st.session_state.interview
    character1 = st.session_state.current_chars["char1"]
    character2 = st.session_state.current_chars["char2"]
    topic = st.session_state.current_chars["topic"]
    tone = st.session_state.current_chars["tone"]
    
    # Create a stylish header for the interview results
    st.markdown(f"""
    <div class="interview-header" style="text-align: center; margin: 30px 0 20px 0;">
        <h2 style="color: #1E40AF; margin-bottom: 5px;">🎬 Interview between {character1} and {character2}</h2>
        <p style="color: #4B5563; font-size: 0.9rem;">
            <span style="margin-right: 15px;"><strong>Topic:</strong> {topic if topic else "General conversation"}</span>
            <span><strong>Tone:</strong> {tone}</span>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Display the interview in a nicely formatted box
    with st.container():
        st.markdown('<div class="generated-interview">', unsafe_allow_html=True)
        
        # Process the interview to add better formatting
        lines = interview.split('\n')
        formatted_text = ""
        
        for line in lines:
            if line.strip():
                if ":" in line:
                    parts = line.split(":", 1)
                    speaker = parts[0].strip()
                    dialogue = parts[1].strip()
                    
                    # Determine which character is speaking
                    if speaker == character1:
                        color = "#2563EB"
                    elif speaker == character2:
                        color = "#DB2777"
                    else:
                        color = "#4B5563"
                        
                    formatted_text += f'<p><span style="color: {color}; font-weight: 600;">{speaker}:</span> {dialogue}</p>\n'
                else:
                    formatted_text += f'<p style="font-style: italic; color: #6B7280;">{line}</p>\n'
            else:
                formatted_text += '<br>\n'
        
        st.markdown(formatted_text, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Create action buttons with better styling
        st.markdown("<div style='margin: 30px 0 20px 0;'>", unsafe_allow_html=True)
        
        button_col1, button_col2, button_col3 = st.columns([1, 1, 1])
        
        # Create download button
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"interview_{character1}_{character2}_{current_time}.txt"
        
        with button_col1:
            st.download_button(
                label="📥 Download Script",
                data=interview,
                file_name=filename,
                mime="text/plain",
                use_container_width=True
            )
        
        # Generate new interview button
        with button_col2:
            if st.button("🔄 Create New Interview", key="new_interview", use_container_width=True):
                st.session_state.interview = None
                st.rerun()
                
        # Try different tone button
        with button_col3:
            if st.button("🎭 Try Different Tone", key="diff_tone", use_container_width=True):
                # Keep the same characters but clear the interview
                st.session_state.interview = None
                st.rerun()
                
        st.markdown("</div>", unsafe_allow_html=True)

# Footer with enhanced styling
st.markdown("<div style='margin-top: 50px;'>", unsafe_allow_html=True)
st.markdown("<hr style='margin: 30px 0; border-color: #E5E7EB;'>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; padding: 20px 0;">
    <p style="color: #6B7280; font-size: 0.9rem;">Made with ❤️ using Streamlit and Google's Gemini 1.5 Pro</p>
    <p style="color: #9CA3AF; font-size: 0.8rem; margin-top: 5px;">© 2025 AI Fictional Interview Generator</p>
</div>
""", unsafe_allow_html=True)
