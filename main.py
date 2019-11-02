from Scrape import Scrape
from Downloader import Downloader


twitter_user = "MasterDaye"

sc = Scrape("https://twitter.com/{}/media".format(twitter_user))
dl = Downloader(sc.getImageLinks())
dl.download("masterdaye")

