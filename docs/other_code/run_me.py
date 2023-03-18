from get_html_page import get_html_page

page_link = 'https://vemcount.app/embed/widget/5MDzNwHx8n6Guxl?locale=en'
temp_files_location = 'temp_files/'
f_name = 'page.html'
temp_html_file = "_raw.html"
temp_text_file = "_raw.txt"

get_page = get_html_page()
get_page.get_html_and_txt(page_link, temp_html_file, temp_text_file)

