import requests
import os

class Downloader:
    urls = []

    def __init__(self, urls):
        self.urls = urls

    def download(self, folder):
         for link in self.urls:
            print("Downloading {}".format(link))
            r = requests.get(link, allow_redirects=True)
            if not os.path.exists(folder):
                os.mkdir(folder)
                
            if link.find('/'):
                filename =  (link.rsplit('/',1)[1])
            open("{}/{}".format(folder, filename), 'wb').write(r.content)