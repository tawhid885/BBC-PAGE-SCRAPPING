from bs4 import BeautifulSoup
import requests


source=requests.get('https://www.bbc.com/').text
soup=BeautifulSoup(source,'lxml')

article=soup.find_all('div',class_='media__content')

for post in article:
    try:
        headline= post.h3.a.text
        summary= post.p.text
        link= post.a['href']
    except Exception as e:
        pass
    print(headline.strip())
    print('       ',summary.strip())
    print(link)
    print('------------------------------------')

# for post in article:
#     # link=post.h3.a['href']
#     # link='https://www.bbc.com'+new_link
#     headline=post.h3.a.text
#     summary=post.p.text

#     # if link[0]=='h':
#     #     full_article=requests.get(link).text
#     #     soup_full=BeautifulSoup(full_article,'lxml')

#     #     print(soup_full.main.text)
#     print(headline)
#     print(summary)
#     print()
#     print()

    

# print(article)