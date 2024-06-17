from models.llm import initialize_llm
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


parser = StrOutputParser()
chat_model = initialize_llm()

def generate_questions(person_name, retriever, n_questions=1):
    """
    Generates relevant questions to ask a person based on the retrieved news articles.
    """

    prompt = ChatPromptTemplate.from_template(
        """Based on the following news articles about {person_name}, generate {n_questions} relevant and thoughtful questions to ask.
        These questions should be interesting, respectful, and asked to {person_name}.
        Avoid sensationalism and focus on what {person_name} would likely find engaging and relevant to their work or personal interests:


        {context}

        Questions:
        """
    )

    # retriever = AskNewsRetriever(k=3)

    chain = (
        RunnablePassthrough.assign(context=(lambda x: retriever))
        | prompt
        | chat_model
        | parser
    )

    return chain.invoke({"person_name": person_name, "n_questions": n_questions})

# Function to check if the answer is valid
def check_answer(person_name, question, answer):
    prompt = ChatPromptTemplate.from_template(
        """You are an interview agent making an interview to {person_name}. The question was: "{question}"
        The answer provided was: "{answer}"
        Does the answer address the question, even if briefly? Reply with 'yes' or 'no' and explain why briefly.
        """
    )
    chain = (
        prompt
        | chat_model
        | parser
    )
    response = chain.invoke({"person_name": person_name, "question": question, "answer": answer})
    return response

# Function to generate follow-up questions based on an answer
def generate_follow_up_questions(question, answer, depth):
    prompt = ChatPromptTemplate.from_template(
        """You are an interview agent. The question was: "{question}"
        The answer provided was: "{answer}"
        Based on this answer, generate up to {depth} relevant follow-up questions.
        Follow-up Questions:
        """
    )
    chain = (
        prompt
        | chat_model
        | parser
    )
    response = chain.invoke({"question": question, "answer": answer, "depth": depth})
    return response