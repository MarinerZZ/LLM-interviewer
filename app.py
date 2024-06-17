from interview.interview_flow import conduct_interview


if __name__ == "__main__":
    interviewee_name = "Will Smith"
    max_depth = 1  # Set the maximum depth for follow-up questions
    conduct_interview(interviewee_name, max_depth)