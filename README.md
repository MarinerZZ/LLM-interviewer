
# LLM Interviewer

Welcome to the LLM Interview Agent project! This application leverages LangChain and Streamlit to create an interactive interview experience. Users can generate interview questions and provide answers through a user-friendly web interface.

## Table of Contents
- [LLM Interviewer](#llm-interviewer)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Steps](#steps)
  - [Usage](#usage)
  - [Acknowledgements](#acknowledgements)

## Introduction

The LLM Interview Agent is designed to simulate an interview to a famous person process. Using the power of LangChain, it generates relevant number of interview questions. The user then provides answers as the person being interviewed and at the end of the process an html file is generated simulating a blog post that summarizes the content of the interview.

## Features

- **Interactive Interface**: User-friendly interface powered by Streamlit.
- **Customizable Interviews**: Specify the interviewee's name and the number of questions to generate.
- **Dynamic Question Generation**: Leverages LangChain to generate relevant and context-aware interview questions.
- **Answer Input**: Users can input their answers directly into the app for each generated question.

## Installation

### Prerequisites

- Python 3.12 or higher
- pip (Python package installer)
- conda (recommended, for environment management)

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MarinerZZ/llm-interviewer.git
   cd llm-interviewer
   ```

2. **Create a virtual environment** (optional but recommended):
   - Using `pip` and `venv`:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```
   - Using `conda`:
     ```bash
     conda create --name llm-interviewer python=3.12
     conda activate llm-interviewer
     ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment variables**:
    - ``OPENAI_API_KEY``: Optional if you decide to use a gpt model
    - ``ASKNEWS_CLIENT_ID``: Required for the news searching langchian retriever
    - ``ASKNEWS_CLIENT_SECRET``: Required for the news searching langchian retriever
    - ``NVIDIA_API_KEY``: Required to use the default model **meta/llama3-70b-instruct**

## Usage

1. **Run the Streamlit app**:
   ```bash
   streamlit run streamlit_app.py
   ```

2. **Navigate to the local server**:
   Open your web browser and go to `http://localhost:8501`.

3. **Interact with the app**:
   - Specify the number of questions you want to generate.
   - Enter the name of the interviewee.
   - Answer the generated questions in the provided text input field.

<!-- 
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details. -->

## Acknowledgements
- [NVIDIA](https://build.nvidia.com/explore/discover)
- [LangChain](https://github.com/langchain-ai/langchain)
- [Streamlit](https://streamlit.io)