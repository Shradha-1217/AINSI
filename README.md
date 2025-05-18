# AI Fictional Interview Generator 🎭

## Overview

The **AI Fictional Interview Generator** is a web-based application that allows users to create imaginative and entertaining dialogues between two characters of their choice, powered by Google's Gemini 1.5 Pro AI model. Whether you want to see Socrates debating Steve Jobs on innovation or Krishna discussing duty with Arjuna, this app brings fictional interviews to life with customizable topics and tones.

Built with **Streamlit**, the app offers a sleek and user-friendly interface with custom styling, interactive features, and the ability to download generated scripts. It’s perfect for writers, educators, or anyone looking to explore creative conversations between historical, mythical, or pop culture figures.

---

## Features

- **Dynamic Interview Generation:** Generate 8–10 exchange dialogues between two characters using Google’s Gemini 1.5 Pro model.
- **Customizable Inputs:** Choose your characters, specify an optional topic, and select a tone (Funny, Dramatic, Philosophical, Creative).
- **Predefined Character Pairs:** Select from popular combinations like Socrates & Steve Jobs, Krishna & Arjuna, or Emperor Akbar & Birbal.
- **Tone Selection with Visuals:** Pick a conversation tone with intuitive icons and descriptions (e.g., 😂 for Funny, 🧠 for Philosophical).
- **Enhanced UI/UX:** 
  - Custom CSS for a polished look with hover effects, color-coded dialogue, and responsive design.
  - Interactive elements like example cards, tone selectors, and expandable sections.
  - Progress animation during interview generation.
- **Downloadable Scripts:** Save your generated interview as a `.txt` file with a timestamped filename.
- **Error Handling:** Validates user inputs (e.g., character names, API key) with clear error messages.
- **Sidebar Configuration:** Securely input your Google API key and access app instructions in a styled sidebar.
- **Cultural Representation:** Includes character pairs from Indian mythology and history (e.g., Rama & Ravana, Shiva & Parvati).

---

## Technologies Used

- **Python:** Core programming language for app logic.
- **Streamlit:** Framework for building the web application.
- **Google Generative AI SDK (google.generativeai):** For integrating the Gemini 1.5 Pro model.
- **Datetime:** For timestamping downloadable files.
- **CSS:** Custom styles for enhanced UI/UX (e.g., buttons, cards, tone selectors).

---

## Installation

Follow these steps to set up and run the AI Fictional Interview Generator on your local machine:

### Prerequisites
- Python 3.8 or higher
- A Google API Key for the Gemini 1.5 Pro model (available from [Google AI Studio](https://makersuite.google.com/))
- Git (optional, for cloning the repository)

### Steps
1. **Clone the Repository (Optional):**
   If the project is hosted on a Git repository, clone it to your local machine:
   ```bash
   git clone https://github.com/[your-username]/ai-fictional-interview-generator.git
   cd ai-fictional-interview-generator
   ```

2. **Install Dependencies:**
   Create a virtual environment and install the required packages:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install streamlit google-generative-ai
   ```

3. **Set Up Your API Key:**
   - Obtain your Google API Key from [Google AI Studio](https://makersuite.google.com/).
   - You can either:
     - Set it as an environment variable:
       ```bash
       export GEMINI_API_KEY="your-api-key-here"  # On Windows: set GEMINI_API_KEY="your-api-key-here"
       ```
     - Or enter it directly in the app’s sidebar when prompted.

4. **Run the Application:**
   Start the Streamlit server:
   ```bash
   streamlit run app.py
   ```
   The app will open in your default web browser at `http://localhost:8501`.

---

## Usage

1. **Enter Your API Key:**
   - In the sidebar, input your Google API Key to enable the Gemini 1.5 Pro model.
   - A success message will confirm the API key is valid.

2. **Select or Input Characters:**
   - Choose a pre-made character pair (e.g., Nikola Tesla & Tony Stark) by clicking "Select Pair" on an example card.
   - Alternatively, enter custom character names in the "Create Your Custom Interview" section.

3. **Specify a Topic (Optional):**
   - Provide a topic for the interview (e.g., "Future of Technology") or leave it blank for the AI to decide.

4. **Choose a Tone:**
   - Select a conversation tone (Funny, Dramatic, Philosophical, Creative) using the visual tone selector.

5. **Generate the Interview:**
   - Click the "✨ Generate Interview" button.
   - The app will display a progress animation while the Gemini model generates the dialogue.

6. **View and Interact with the Result:**
   - The generated interview will appear in a formatted box with color-coded speaker labels (e.g., blue for Character 1, pink for Character 2).
   - Use the action buttons to:
     - **Download Script:** Save the interview as a `.txt` file.
     - **Create New Interview:** Start over with new characters.
     - **Try Different Tone:** Regenerate the interview with a different tone.

---

## Example

### Input
- **Character 1:** Leonardo da Vinci  
- **Character 2:** Elon Musk  
- **Topic:** Future of Art and Technology  
- **Tone:** Creative  

### Output (Sample)
**Leonardo da Vinci:** Elon, my friend, how do you envision the canvas of the future—will technology paint a new Renaissance?  
**Elon Musk:** Leonardo, art and tech will merge like never before! Imagine neural-linked brushes—your thoughts directly creating masterpieces on a digital canvas.  
**Leonardo da Vinci:** Fascinating! But what of the human touch? My Mona Lisa’s smile took years of delicate strokes.  
**Elon Musk:** We’ll enhance that touch. AI can simulate your techniques, but the artist’s soul will guide it—maybe even on Mars!  

---

## Screenshots

*(Note: Screenshots are not included in this README but can be added by taking snapshots of the app interface, such as the homepage with example cards, the tone selector, and a generated interview.)*

- **Homepage:** Displays example character pairs and input fields.
- **Generated Interview:** Shows a formatted dialogue with color-coded speakers and action buttons.

---

## Project Structure

```
ai-fictional-interview-generator/
│
├── app.py                # Main application script
├── README.md            # Project documentation (this file)
└── requirements.txt     # List of dependencies (optional, can be generated with `pip freeze > requirements.txt`)
```

---

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m "Add your feature"`).
4. Push to your branch (`git push origin feature/your-feature`).
5. Create a pull request with a detailed description of your changes.

Potential contributions could include:
- Adding more tone options or character pairs.
- Enhancing the UI with additional styling or animations.
- Implementing multilingual support for generated interviews.

---

## Troubleshooting

- **API Key Error:** Ensure your Google API Key is valid and has access to the Gemini 1.5 Pro model. Check your API key in [Google AI Studio](https://makersuite.google.com/).
- **No Output Generated:** Verify that both character names are provided and the API key is entered correctly.
- **App Not Running:** Confirm that all dependencies are installed (`streamlit`, `google-generative-ai`) and you’re using a compatible Python version.
- **Styling Issues:** Clear your browser cache or ensure you’re running the latest version of Streamlit.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- **Google AI:** For providing the Gemini 1.5 Pro model and API.
- **Streamlit:** For the framework used to build this interactive web app.
- **Community:** Thanks to the open-source community for inspiration and support.

---

## Contact

For questions, feedback, or suggestions, please reach out:  
- **Email:** [Your Email Address]  
- **GitHub:** [Your GitHub Profile]  

Made with ❤️ by [Your Name] © 2025
