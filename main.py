from Scrape import Scrape
from Downloader import Downloader
import argparse


parser = argparse.ArgumentParser("Scrape Pictures off the userpage of a Twitter User")
parser.add_argument('-u', '--user',  metavar="user", type=str, nargs=1, help="User to parse from")

args = parser.parse_args()
#twitter_user = "MasterDaye"
twitter_user = args.user[0]
print(twitter_user)
sc = Scrape("https://twitter.com/{}/media".format(twitter_user))
dl = Downloader(sc.getImageLinks())
dl.download(twitter_user)

