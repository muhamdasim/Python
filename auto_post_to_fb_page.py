import facebook
import os
import fnmatch
import time
token="#replace with token from Facebook Developers" 
fb = facebook.GraphAPI(access_token=token)
i = 0
path = r"#replace with source folder"
source = os.listdir(r"#replace with source folder")
path = path + "\\"
iterator = len(fnmatch.filter(os.listdir(path), '*.jpg'))

while i < iterator:
    target = path + source[i]
    with open(target, 'rb') as f:
        photo = f.read()


    fb.put_photo(parent_object='me', connection_name='feed', image=photo ,message='this is cool photo')
    print("FileName Posted:", source[i])
    time.sleep(60)
    source = os.listdir(r"#replace with source folder")
    iterator = len(fnmatch.filter(os.listdir(path), '*.jpg'))
    i = i + 1
print("finised")
