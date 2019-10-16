import bs4 as bs
from multiprocessing import Pool
import requests
import string
import random 

def starting_url():
    url = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(3))
    url = ''.join(['https://', url, '.com'])
    return url

def handle_local_links(url, link):
    if link.startswith('/'):
        return ''.join([url, link])
    return link

def get_links(url):
    try:
        resp = requests.get(url)
        soup = bs.BeautifulSoup(resp.text, 'lxml')
        body = soup.body
        links = [link.get('href') for link in body.find_all('a')]
        links = [str(handle_local_links(url, link).encode('ascii')) for link in links]
        return links
    except TypeError as e:
        print(e)
        print('Probably got a null value or None, returning empyt list')
        return []
    except IndexError as e:
        print(e)
        print('Probably got an empty list, returning empyt list')
        return []
    except Exception as e:
        print(str(e))
        return []

def main():
    number = int(input("enter number of url "))
    parse_us = [starting_url() for _ in range(number)]

    for _ in range(1):
        with Pool(processes=number) as p:
            links = p.map(get_links, parse_us)
            links = [link for url_list in links for link in url_list]
            parse_us = links

    with open('urls.txt', 'w') as file:
        file.write(str(parse_us))

if __name__ == '__main__':
    main()