#these classes follow the Single Responsibility Principle which makes the code easier to understand, maintain, and modify
#WebFetcher is responsible for fetching the url content
#Extractor is responsible for getting the article text from the url's HTML
#WebScrap is responsible for getting the info from the two classes and returning the result
#The function called in run.py is article() and rawArticle() which has the url as input. It then calls the fetch() to fetch url's data
#then stores the result if the result is not NULL it returns the result of the ArticleExtractor()/RawArticleExtractor() that is given the url to extract from

import requests
from bs4 import BeautifulSoup

class WebFetcher:

    def fetch(url):
        response = requests.get(url)
        
        if response:
            return response.text
        
        else:
            print(f'Failed to fetch url: {url}')
            return None

class Extractor:

    def ArticleExtractor(html):
 
        soup = BeautifulSoup(html, 'html.parser')
        # Find the main div content of the article
        article_content = soup.find('div', id='storytext')
        
        text = ""
        if article_content:
            # cycles through the direct children
            for child in article_content.children:
                if child.name == 'p':
                    # appends each paragraph together that is a direct child of article_content
                    text = text + child.get_text() + "\n"
            # returns variable
            return text
        # Case if fails      
        else:
            print(f"Failed to extract content from URL: {html}")
            return None
        
    def RawArticleExtractor(html):
 
        soup = BeautifulSoup(html, 'html.parser')
        # Find the main div content of the article
        article_content = soup.find('div', id='storytext')
        
        text = ""
        if article_content:
            # cycles through the direct div
            for i in article_content:
            
                # appends each paragraph together that is a direct child of article_content
            
                text = text + i.get_text() + "\n"
            # returns variable
            return text
        
        # Case if fails      
        else:
            print(f"Failed to extract content from URL: {html}")
            return None
        
class WebScrap:

    def article(url):
        html = WebFetcher.fetch(url)
        if html:
            return Extractor.ArticleExtractor(html)
        else:
            return None
        
    def rawArticle(url):
        html = WebFetcher.fetch(url)
        if html:
            return Extractor.RawArticleExtractor(html)
        else:
            return None