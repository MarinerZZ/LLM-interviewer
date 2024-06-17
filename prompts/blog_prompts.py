from models.llm import initialize_llm
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

chat_model = initialize_llm()
parser = StrOutputParser()

def generate_blog_post(interview_data, person_name):
    """
    Generates a blog post based on the interview data.

    Args:
        interview_data (list): A list of tuples containing questions and answers.

    Returns:
        str: The generated blog post content.
    """
    prompt = ChatPromptTemplate.from_template(
        """You are a professional writer.
        Based on the following interview data, write a blog post summarizing the interview made to {person_name}.
        Structure it with a headline, lead section and body section.
        Clearly mark each section with the following tags exactly as shown:
        [HEADLINE], [LEAD], and [BODY]. 
        The interview data is
        {interview_data}
        """
    )
    chain = (
        prompt
        | chat_model
        | parser
    )
    response = chain.invoke({"interview_data": interview_data, "person_name": person_name})
    return response
