import requests
from bs4 import BeautifulSoup

class Scrape:
    img_links = []

    def __init__(self, url):
        self.url = url
        r = requests.get(self.url)
        soup = BeautifulSoup(r.content, 'html.parser')

        for images in soup.findAll("img"):
            if link := images.get("src") is not  None:
                self.img_links.append(link)


    
    def getImageLinks(self):
        return(self.img_links)
