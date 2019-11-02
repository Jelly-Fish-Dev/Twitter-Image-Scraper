import requests
import twitter


class Scrape:
    img_links = []

    def __init__(self, url):
        self.url = url
        r = requests.get(self.url)
        soup = BeautifulSoup(r.content, 'html.parser')

        for images in soup.findAll("img"):
            if (link := images.get("src")) is not  None: #make sure to install python3.8 
                self.img_links.append(link)
    
    def getImageLinks(self):
        return(self.img_links)
