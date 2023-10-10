import requests
from bs4 import BeautifulSoup

url = 'https://example.com'

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string
    print(f'Title: {title}')
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))
else:
    print('Failed to retrieve the webpage')

