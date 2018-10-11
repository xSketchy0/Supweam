from bs4 import BeautifulSoup
import requests

url = "http://www.supremenewyork.com/shop/all/bags"
response = requests.get(url)


soup = BeautifulSoup(response.content, 'html.parser')

data = soup.find('a', {'class': ['name-link']}, href=True)

post_url = str(url+data['href'])

post = requests.post(post_url)

post_soup = BeautifulSoup(post.content, 'html.parser')

for a in post_soup.find_all('a', href=True):
    print ("Found the URL:", a['href'])

