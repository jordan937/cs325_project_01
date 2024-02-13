import requests
from bs4 import BeautifulSoup

def Webscrap(url):
 
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find the main div content of the article
    article_content = soup.find('div', id='storytext')
    # Finds all the <p> tags in the main div
    paragraph = article_content.find_all('p')
    text = ""
    if paragraph:
        # cycles through the paragraphs
        for p in paragraph:
            # appends each paragraph together
            text = text + p.get_text() + "\n"
        # returns variable
        return text
    # Case if fails      
    else:
        print(f"Failed to extract content from URL: {url}")
        return None

# Read the list of URLs from the text file
# note: stores urls in input text file into variable "urls" as a list
with open('url.txt', 'r') as file:
    urls = (file.readlines())


# cycling through the urls and it's index calling the Webscrap function each time;
for index, url in enumerate(urls):
    page = str(url)
    # assigns the article's paragraphs
    content = Webscrap(page)
    if content:
         with open(f'article{index + 1}.txt', 'w') as content_file:
                # writes article text into assigned text file
                content_file.write(content)
    