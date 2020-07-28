import requests
from bs4 import BeautifulSoup
url="https://www.google.com/search?q=see"
page = requests.get(url)
soup = BeautifulSoup(page.content)
links = soup.findAll("a")
for link in links:
     print (re.split(":(?=http)",link["href"].replace("/url?q=","")))
imgData =soup.findAll("img")
imgHref1=[]
for img in imgData:
    imgHref1.append(img.get("link"))
for i in imgHref1:
    x=i
    response=requests.get(i)
    filename=type(file)+"/"+imgName;
    with open(filename,'wd') as fd:
        for chunk in response.iter_content(chunk_size=128):
            fd.write(chunk)
