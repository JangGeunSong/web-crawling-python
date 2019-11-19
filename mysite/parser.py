from bs4 import BeautifulSoup
import requests

req = requests.get('https://news.google.com/?hl=ko&gl=KR&ceid=KR:ko')

soup = BeautifulSoup(req.text, 'html.parser')

posts = soup.findAll(class_='ipQwMb')

for post in posts:
    title = post.find(class_='DY5T1d')
    link = post.find('a')['href']
    print(title.text, link)