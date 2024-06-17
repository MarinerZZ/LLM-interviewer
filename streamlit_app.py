import streamlit as st
from interview.interview_flow import Interview

# Initialize session state for storing chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

if "disabled" not in st.session_state:
    st.session_state["disabled"] = False

if "text_input" not in st.session_state:
    st.session_state["text_input"] = ""

if "num_questions" not in st.session_state:
    st.session_state["num_questions"] = None

if "submitted" not in st.session_state:
    st.session_state["submitted"] = False

def disable_inputs():
    st.session_state["disabled"] = True

def check_and_disable():
    if st.session_state["num_questions"] is not None and st.session_state["text_input"] and not st.session_state["disabled"]:
        disable_inputs()
        if "interview" not in st.session_state:
            st.session_state["interview"] =  Interview(st.session_state["text_input"], st.session_state["num_questions"], 1)
        st.session_state["submitted"] = True  # Trigger rerun
        

# Define the app's sidebar
st.sidebar.header('Number of Main Questions')
num_questions = st.sidebar.number_input("Enter a number:", min_value=1, max_value=10, value=st.session_state["num_questions"], on_change=check_and_disable, disabled=st.session_state.disabled)

st.sidebar.header('Famous Person Name')
text_input = st.sidebar.text_input("Enter some text:", value=st.session_state["text_input"], on_change=check_and_disable, disabled=st.session_state.disabled)

if st.sidebar.button("Submit"):
    st.session_state["num_questions"] = num_questions
    st.session_state["text_input"] = text_input
    check_and_disable()

# Trigger a rerun if the form was submitted
if st.session_state["submitted"]:
    st.session_state["submitted"] = False  # Reset the flag
    st.experimental_rerun()

# Add authorship text to the sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### LLM interviewer")
st.sidebar.markdown("Project by [Marino Pérez Segura]")

# Define the main app interface
st.title('Interview LLM Agent')
st.write('Welcome to the Interview LLM Agent! Fill the data on the sidebar to define the number of main questions there would be and the person who is going to be interviewed. Each main question will have a follow up question by default')

# Display the number of questions setting
st.write(f'Number of questions: {num_questions}')

if "interview" in st.session_state:
    interview = st.session_state["interview"]

    # Placeholder for chatbot interaction
    st.subheader('Put your answer here')
    # Add a form for user input
    with st.form(key='user_input_form', clear_on_submit=True):
        user_input = st.text_input('You:', '', key='input')
        submit_button = st.form_submit_button(label='Send')

        if submit_button and user_input:
            # Append user input and a placeholder for bot response to chat history
            answer_status = interview.answer_question(user_input)
            if interview.is_interview_going:
                bot_response = interview.current_question if answer_status else "Please, answer the question provided"
            else:
                bot_response = "Interview concluded. Thank you for your time!"
            st.session_state['chat_history'].append({'user': user_input, 'bot': bot_response})
            # Clear the input after submission
            user_input = ''

    # Display the chat history
    st.subheader('Interview history')
    if interview.is_first_question:
        st.session_state['chat_history'].append({'user': None, 'bot': interview.current_question})
    for message in reversed(st.session_state['chat_history']):
        st.write(f'**Interviewer:** {message["bot"]}')
        if message["user"] is not None:
            st.write(f'**You:** {message["user"]}')
        st.write('---')
