import os
from utils.html_formatter import format_to_html


def create_html_output(blog_content, output_file_path='output/interview_summary.html'):
    """
    Creates the HTML output for the blog content and saves it to a file.

    Args:
        blog_content (str): The blog post content.
        output_file_path (str): The file path where the HTML content will be saved.

    Returns:
        None
    """
    formatted_html = format_to_html(blog_content)
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
    with open(output_file_path, 'w') as file:
        file.write(formatted_html)
    print(f"Blog post has been saved to {output_file_path}")
