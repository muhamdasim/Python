import requests
from bs4 import BeautifulSoup
import csv
import  json
ending_page=373
detail=""
main_page_urls=[]
headlines=[]
date=[]
content=[]
team='https://www.urdupoint.com/en/team/'
for starting_page in range(ending_page):
    print("Scraping Page No:",starting_page+1)
    r=requests.get('https://www.urdupoint.com/en/news/pakistan/crime-updates'+ str(starting_page+1) +'.html')
    soup=BeautifulSoup(r.content,'lxml')

    for item in soup.find_all(class_='txt_box'):
        for link in item.find_all('a'):
            if not team in link.get('href'):
                print(link.get('href'))
                main_page_urls.append(link.get('href'))


for i in main_page_urls:
    r=requests.get(i)
    print("Url:",i)
    detail=""
    sp=BeautifulSoup(r.content,'lxml')
    data = sp.find_all("script", type="application/ld+json")[3]
    da = json.loads(str(data.text),strict=False)
    headlines.append(da['headline'])
    try:
        date.append(sp.find_all(class_='article-date')[2].get_text().strip())
    except:
        continue

    for item in sp.find_all(class_='detail_txt'):
        for link in item.find_all('p'):
            detail= detail + link.get_text().strip()

    d,*_=detail.split(')')
    fn=detail.replace(d, '')
    detail=fn.replace(')','').replace(':','').strip()
    content.append(detail)

with open("sample.csv", "w",newline='',encoding="utf-8") as csvFile:
    fieldnames = ['Heading','Date','Detail']
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
    writer.writeheader()
    for h,d,c in zip(headlines,date,content):
        writer.writerow({'Heading': h , 'Date': d, 'Detail':c})
