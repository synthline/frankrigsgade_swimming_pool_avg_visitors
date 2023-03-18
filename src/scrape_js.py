from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# Create a new instance of a web driver
driver = webdriver.Chrome()

# Load the webpage
driver.get("https://vemcount.app/embed/widget/5MDzNwHx8n6Guxl?locale=en")

# Wait for the page to fully load
driver.implicitly_wait(10)

# Retrieve the dynamically generated content
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
text = soup.get_text()

# Close the web driver
driver.quit()

# Process the text as needed
print(text)





"""
# Create a new instance of a web driver
driver = webdriver.Chrome()

# Load the webpage
driver.get("https://vemcount.app/embed/widget/5MDzNwHx8n6Guxl?locale=en")

# Wait for the page to fully load
driver.implicitly_wait(10)

# Retrieve the dynamically generated content
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
data = soup.find_all("div", {"class": "vc-result-item-text"})

# Extract the two strings from the HTML
string1 = data.text.strip()
#string2 = data[1].text.strip()

# Close the web driver
driver.quit()

# Process the strings as needed
print(string1)
#print(string2)

# Create a new instance of a web driver
driver = webdriver.Chrome()

# Load the webpage
driver.get("https://vemcount.app/embed/widget/5MDzNwHx8n6Guxl?locale=en")

# Wait for the page to fully load
driver.implicitly_wait(10)

# Simulate user interaction (e.g. click a button, enter text)
search_box = driver.find_element_by_name("q")
search_box.send_keys("example search")
search_box.send_keys(Keys.RETURN)

# Wait for the page to fully load
driver.implicitly_wait(10)

# Retrieve the dynamically generated content
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
data = soup.find("div", {"class": "example-class"})

# Close the web driver
driver.quit()

# Process the data as needed
"""