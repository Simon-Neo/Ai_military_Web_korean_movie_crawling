import requests
import re
import csv
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/running/current.nhn'

#tab 후기 참조 주소
url_base_movie_post =  'https://movie.naver.com/movie/bi/mi/point.nhn?code='

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

list_li_movie = soup.select("div[id=wrap] > div[id=container] > "
                            "div[id=content] > div[class=article] > "
                            "div:nth-child(1) > div[class=lst_wrap] > "
                            "ul[class=lst_detail_t1] > li")


# -------------------------------------------- Read_contnet
list_dic_movies = []
list_columns_name = ['title', 'url_code']
for li_val in list_li_movie:
    dic_movie = {}
    # title = test = li_val.select_one("div > a > img")["alt"]
    select_a = li_val.select_one("dl > dt > a")
    title = re.compile('\<.*?\>').sub('', str(select_a))
    # print(title)
    dic_movie['title'] = title

    url_code = select_a["href"]
    url_code = re.compile("\D+").sub('', url_code)
    dic_movie['url_code'] = url_code

    list_dic_movies.append(dic_movie)

print(list_dic_movies)

# -------------------------------------------- Post Scripts
# response = requests.get(url_base_movie_post + list_dic_movies[0]['url_code']+ '#tab')
# soup = BeautifulSoup(response.text, 'html.parser')
# list_li_posts = soup.select("div[id=wrap] > div[id=container] > "
#                             "div[id=content] > div[class=article] > "
#                             "div[]")
