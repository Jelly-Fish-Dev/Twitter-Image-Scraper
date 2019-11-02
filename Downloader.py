import requests
import os
from tqdm import tqdm

class Downloader:
    urls = []

    def __init__(self, urls):
        self.urls = urls

    def download(self, folder):
         for link in self.urls:
            print("Downloading {}".format(link))
            r = requests.get(link, allow_redirects=True)
            
            if not os.path.exists("images"):
                os.mkdir("images")
            
            if not os.path.exists("images/" + folder):
                os.mkdir("images/" + folder)

            if link.find('/'):
                filename =  (link.rsplit('/',1)[1])
            total_size = int(r.headers.get('content_length', 0))
            block_size = 1024 # One 1kb
            t = tqdm(total_size, unit="iB", unit_scale=True)
            with open("images/{}/{}".format(folder, filename), 'wb') as f:
                for data in r.iter_content(block_size):
                    t.update(len(data))
                    f.write(data)
            t.close()
