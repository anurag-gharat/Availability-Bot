from textblob import TextBlob
import requests
from bs4 import BeautifulSoup

class Analysis:
    def  __init__(self,term):
        self.term=term
        self.subjectivity=0
        self.sentiment=0
        self.url='https://www.google.com/search?q=[0]&source='.format(self.term)


    def run(self):
        resonse=requests.get(self.url)
        soup=BeautifulSoup(resonse.text,'html.parser')
        headline_results=soup.find_all('div',class.='st')