import requests
import re
from bs4 import BeautifulSoup
from googlesearch import  search

allLinks = [];mails=[]


url='https://www.gse.harvard.edu/staff/min-z'
response = requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')

def findMails(soup):
    for name in soup.find_all('a'):
        if(name is not None):
            emailText=name.text
            match=bool(re.match('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',emailText))
            if('@' in emailText and match==True):
                emailText=emailText.replace(" ",'').replace('\r','')
                emailText=emailText.replace('\n','').replace('\t','')
                if(len(mails)==0)or(emailText not in mails):
                    print(emailText)
                mails.append(emailText)
            else:
                print("Sorry no email Found")
                break

r=requests.get(url)
data=r.text
soup=BeautifulSoup(data,'html.parser')
findMails(soup)
