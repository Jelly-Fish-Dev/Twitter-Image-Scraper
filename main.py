from Scrape import Scrape

sc = Scrape("https://twitter.com/MasterDaye/media")
print(sc.getImageLinks())