#Libraries

import os
import hashlib
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import unquote, urlparse
from pathlib import PurePosixPath


//Data Function

def GetPageData(page_url,dest_dir):

    # Download page html
    page_data = requests.get(page_url).text

    # Find all links in page
    images_urls = [
        image.attrs.get('src')
        for image in BeautifulSoup(page_data, 'lxml').find_all('img')
    ]

    # Clean empty links (<img src="" /> <img> etc)
    images_urls = [
        image_url
        for image_url in images_urls
        if image_url and len(image_url)>0
    ]

    # TODO: add filename extension
    for image_url in images_urls:
        image_url=os.path.basename(image_url)
        with open(os.path.join(dest_dir, image_url), 'wb') as f:
            source_url = 'http://www.burlingamepezmuseum.com/' + image_url
            image_data = requests.get(source_url).content
            f.write(image_data)


##Fetching Urls.

def generateLinks():
    df = pd.read_csv('data.csv')
    urls = df['Links'].values.tolist()
    for i in urls:
        path=urlparse(i)
        newpath=path.path
        if not os.path.exists('Replace Your Directory Path here'+newpath):   #Replace Path 
            os.makedirs('Replace Your Directory Path here'+newpath)   #Replace Path
        print("Processing:",i)
        GetPageData(i,'Replace Your Directory Path here'+newpath)    #Replace Path



##Main Function

if __name__ == '__main__':
    generateLinks()
