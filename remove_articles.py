import csv
import pandas as pd


heading=[]
date=[]
content=[]

filter_heading=[]
filter_content=[]

def removearticles_heading(text):


    articles = {'In': '', 'the':'', 'an':'' , 'in':'' , 'at':'' , 'At':''
        , 'The': '' , 'A':'' , 'a':''

                }
    output=""
    for word in text.split():
        if word not in articles:
            output=output+word+' '


    filter_heading.append(output)



def removearticles_content(text):
    articles = {'In': '', 'the': '', 'an': '', 'in': '', 'at': '', 'At': ''
        , 'The': '', 'A': '', 'a': ''

                }
    output=""
    for word in text.split():
        if word not in articles:
            output=output+word+' '


    filter_content.append(output)

if __name__ == '__main__':
    data = pd.read_csv('filter_data_on_keywords.csv')

    for h, d, dd in zip(data['Heading'], data['Date'], data['Detail']):
        heading.append(h)
        date.append(d)
        content.append(dd)


    for h, d, dd in zip(data['Heading'], data['Date'], data['Detail']):
        removearticles_heading(h)
        removearticles_content(dd)


    with open("articles_removed.csv", "w", newline='' ) as csvFile:
         fieldnames = ['Heading', 'Date', 'Detail']
         writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
         writer.writeheader()
         for h, d, c in zip(filter_heading, date, filter_content):
             writer.writerow({'Heading': h, 'Date': d, 'Detail': c})