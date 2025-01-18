import os
from dotenv import load_dotenv
import streamlit as st
import openai

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("🚀 AI-Powered Coding Assistant 🌟")

import streamlit as st
from streamlit_ace import st_ace
import openai

st.title("🚀 AI-Powered Coding Assistant 🌟")

# OpenAI API Key
openai.api_key = "your_openai_api_key"

# Code editor with syntax highlighting
code = st_ace(
    placeholder="Write your code here...",
    language="python",
    theme="monokai",
    height=300,
)

# Button to analyze code
if st.button("Analyze Code"):
    if code:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a coding assistant."},
                {"role": "user", "content": f"Explain the following code:\n{code}"}
            ],
            max_tokens=300,
        )
        st.subheader("💡 AI Response:")
        st.write(response["choices"][0]["message"]["content"])
    else:
        st.warning("Please write some code to analyze!")

# Input for coding problem description
problem_description = st.text_area("Describe your coding problem", height=150)
if st.button("Get Hint"):
    if problem_description:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a coding assistant."},
                {"role": "user", "content": f"Give a solution for the following problem:\n{problem_description}"}
            ],
            max_tokens=300,
        )
        st.subheader("💡 AI Hint:")
        st.write(response["choices"][0]["message"]["content"])
    else:
        st.warning("Please describe a problem to get hints!")

