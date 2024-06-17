import os

def format_to_html(blog_content):
    """
    Formats the blog post content into an HTML template.

    Args:
        blog_content (str): The blog post content.

    Returns:
        str: The formatted HTML content.
    """
    with open('templates/interview_template.html', 'r') as file:
        html_template = file.read()
    
    formatted_html = html_template.replace("<!-- Headline will be inserted here -->", blog_content['headline'])
    formatted_html = formatted_html.replace("<!-- Lead will be inserted here -->", blog_content['lead'])
    formatted_html = formatted_html.replace("<!-- Body will be inserted here -->", blog_content['body'])
    
    return formatted_html
