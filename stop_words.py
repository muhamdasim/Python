from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import  pandas as pd
import csv
data=pd.read_csv('filter_data_on_keywords.csv')

heading=[]
detail=[]

filter_heading=[]
filter_detail=[]
date=[]

for h,d,dd in zip(data['Heading'],data['Date'],data['Detail']):
    heading.append(h)
    date.append(d)
    detail.append(dd)


for h,d in zip(data['Heading'],data['Detail']):
    heading_sent = h
    detail_sent=d
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(heading_sent)
    detail_tokens = word_tokenize(detail_sent)

    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = []
    heading=""
    for w in word_tokens:
        if w not in stop_words:
            heading=heading+w+' '

    filter_heading.append(heading)

    detail=""
    filtered_sentence = [w for w in detail_tokens if not w in stop_words]
    filtered_sentence = []
    for w in detail_tokens:
        if w not in stop_words:
            detail=detail+w + ' '

    filter_detail.append(detail)



with open("stop_words.csv", "w",newline='',encoding="utf-8") as csvFile:
     fieldnames = ['Heading','Date','Detail']
     writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
     writer.writeheader()
     for h,d,c in zip(filter_heading,date,filter_detail):
         writer.writerow({'Heading': h , 'Date': d, 'Detail':c})