import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/TensorFlow')
soup = bs4.BeautifulSoup(res,'lxml')
print(soup.text())