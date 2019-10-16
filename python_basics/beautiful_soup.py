import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

soup = bs.BeautifulSoup(source, 'lxml')

#print(soup.prettify())

#print(soup.get_text())

#print(soup.p.text)

# for paragraph in soup.find_all('p'):
#     print(paragraph.text)

[print(url.get('href')) for url in soup.find_all('a')]
