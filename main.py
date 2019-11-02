from Scrape import Scrape
from Downloader import Downloader

sc = Scrape("https://twitter.com/MasterDaye/media")
dl = Downloader(sc.getImageLinks())
dl.download("masterdaye")