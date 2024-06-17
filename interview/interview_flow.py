import re
from .blog_generator import create_html_output
from utils.data_storage import store_interview_data
from prompts.blog_prompts import generate_blog_post
from langchain_community.retrievers import AskNewsRetriever
from prompts.interview_prompts import generate_questions, generate_follow_up_questions, check_answer


def ask_news(input_text):
    """
    Retrieves recent news articles about the given topic.
    """
    retriever = AskNewsRetriever(k=3)
    news_articles = retriever.invoke(input_text)
    return news_articles

class Interview():
    
    def __init__(self, person_name, n_questions, depth) -> None:
        self.interview_data = []
        self.person_name = person_name
        questions = generate_questions(self.person_name, ask_news(person_name), n_questions)
        self.questions = []
        for _, q in enumerate(questions.split("\n")):
            if q.strip():
                self.questions.append(q)
        self.depth = depth
        self.is_interview_going = True
        self.current_question = self.questions.pop(0)
        self.is_first_question = True
        self.is_follow_up_question = False
        self.follow_up_questions = []

    def transcribe_audio(self, user_audio):
        pass

    def answer_question(self, user_response):
        self.is_first_question = False
        self.interview_data.append((self.current_question, user_response))
        check = check_answer(self.person_name, self.current_question, user_response)
        # check="yes"
        if "yes" in check.lower():
            if not self.is_follow_up_question:
                temp_follow_up_questions = generate_follow_up_questions(
                    self.current_question,
                    user_response,
                    self.depth
                )
                for follow_up_question in temp_follow_up_questions.split('\n'):
                    if follow_up_question.strip():
                        self.follow_up_questions.append(follow_up_question)
            self.update_current_question()
            return True
        else:
            return False

    def update_current_question(self):
        if not self.is_follow_up_question or len(self.follow_up_questions) > 0:
            self.current_question = self.follow_up_questions.pop(0)
            self.is_follow_up_question = True
        elif len(self.questions) > 0:
            self.current_question = self.questions.pop(0)
            self.is_follow_up_question = False
        else:
            self.is_interview_going = False
            self.create_blog_post()

    def create_blog_post(self):
        # Store interview data
        store_interview_data(self.interview_data)

        # Generate and format the blog post
        interview_summary = generate_blog_post(self.interview_data, self.person_name)
        interview_summary = interview_summary.replace("\n", "")

        tags = {
            "[HEADLINE]": 'headline',
            "[LEAD]": 'lead',
            "[BODY]": 'body',
            "**HEADLINE:**": 'headline',
            "**LEAD:**": 'lead',
            "**BODY:**": 'body',
            }
        pattern = '|'.join(map(re.escape, tags))
        split_text = re.split(f'({pattern})', interview_summary)

        sections = {'headline': '', 'lead': '', 'body': ''}
        current_tag = None
    
        for part in split_text:
            if part in tags.keys():
                current_tag = tags[part]
            elif not part.isspace():
                sections[current_tag] = part

        create_html_output(sections, 'output/interview_summary.html')
