from Scrape import Scrape
from Downloader import Downloader
import argparse


def main():
    parser = argparse.ArgumentParser("Scrape Pictures off the userpage of a Twitter User")
    parser.add_argument('-u', '--user',  metavar="user", type=str, nargs=1, help="User to parse from", default=None)

    args = parser.parse_args()
    #twitter_user = "MasterDaye"
    if (twitter_user := args.user[0]) != None:
        print(twitter_user)
        sc = Scrape("https://twitter.com/{}/media".format(twitter_user))
        dl = Downloader(sc.getImageLinks())
        dl.download(twitter_user)


if __name__ == "__main__":
    main()
