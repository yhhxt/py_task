import requests
import os
goal = requests.get("https://movie.douban.com/chart?qq-pf-to=pcqq.group")
a=goal.text
with open('movies.txt','w',encoding='utf-8')as file :
    file.write(a)
print (goal.text)

