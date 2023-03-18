from bs4 import BeautifulSoup
import requests

url = "https://vemcount.app/embed/widget/5MDzNwHx8n6Guxl?locale=en"

result = requests.get(url)
print(result.text)