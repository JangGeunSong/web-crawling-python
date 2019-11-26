from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from datetime import date
import json
import pymysql

# dbconfig.py
class MysqlController:
    def __init__(self, host, id, pw, db_name):
        self.conn = pymysql.connect(host=host, user=id, password=pw, db=db_name,charset='utf8')
        self.curs = self.conn.cursor()

    def insert_movie_data(self, rank, title, link):
        sql = 'INSERT INTO django_crawling.crawlingapi_movieinfo (movieID, title, articleLink) VALUES (%s, %s, %s)'
        self.curs.execute(sql,(rank, title, link))
        self.conn.commit()

def getData() :
    movieData = []
    day = date.today().strftime('%Y%m%d') 
    # 크롤링은 당일만 처리할 예정이므로 오늘을 받은 후 naver movie에서 date에 받는 인자의 포멧이 맞추어 정리함 (20190120 과 같은 포멧으로 되어 있었으므로 이를 따름)

    req = Request('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&tg=0&date=' + day)
    res = urlopen(req)
    html = res.read().decode('cp949') # naver movie 서비스의 경우 cp949로 인코딩 되어 있는데 프로젝트의 경우 utf-8이므로 이를 보정해줌

    soup = BeautifulSoup(html, 'html.parser')

    posts = soup.findAll(class_='title')
    # 웹 상에서 class=title 인 모든 엘레멘트들을 받아옴

    idx = 0 # rank를 primary key로 두기 위해 idx를 미리정의
    for post in posts:
        idx = idx + 1 # 0으로 초기화 했으므로 1을 더해서 1위부터 50위까지 숫자를 먼저 준다.
        rank = (int(day) * 100) + idx # (오늘날자 + 순위)의 방식으로 primary key를 주기로 결정하였으므로 이를 rank에 정의
        title = post.find('a').text
        link = 'https://movie.naver.com' + post.find('a')['href']
        movie = {'title': title, 'rank': rank, 'link': link}
        movieData.append(movie)
    
    return movieData

if __name__=='__main__':
    mysqlcontroller = MysqlController('localhost', 'root', '1234', 'django_crawling')
    moviedata = getData()
    for movie in moviedata:
        mysqlcontroller.insert_movie_data(rank=movie['rank'], title=movie['title'], link=movie['link'])