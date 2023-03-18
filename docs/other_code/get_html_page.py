import requests
import html2text
import re

class get_html_page():
    def __init__(self):
        pass   

    def get_html_and_txt(self, page_link, file_name, txt_file_path):
        # Make a GET request to the specified URL
        response = requests.get(page_link)
        # Check if the request was successful
        if response.status_code == 200:
            # Write the page code to a file
            with open(file_name, 'w', encoding="utf-8") as file:
                file.write(response.text)
        # Parse through the html object
        html = open(file_name).read()
        text = html2text.html2text(html)          
        with open(txt_file_path, 'w') as file:
        # Write contents of textual representation of the html file to a .txt file
            file.write(text)
