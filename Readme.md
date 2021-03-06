# Twitter Image Scraper

This is a simple python script that uses [Beautiful Soup 4](https://pypi.org/project/beautifulsoup4/) and [Requests](https://pypi.org/project/requests2/) in order to scrape images from a Twitter user's Media Tab. Unfortunately due to the Twitter API, it isn't able to download images before a certain date.

# Dependencies
To run Twitter Image Scraper, run the following pip command in your python environment:

```pip install BeautifulSoup4 Requests tqdm```

This Program uses PEP 572 (The Walrus Operator :=) so please make sure that you are running Python 3.8, otherwise it will not execute.
# Running the Image Scraper

To run the Image Scraper, run the following command, with the Twitter Page you want to download from as replacing `<User>`.

```Python3 main.py -U <User>```


# Screenshots/Video
[![asciicast](https://asciinema.org/a/WWmTLK4WRygzHdpY2lT67w8en.svg)](https://asciinema.org/a/WWmTLK4WRygzHdpY2lT67w8en)
![Files when downloaded](https://user-images.githubusercontent.com/15014078/68304160-4e601d80-00f9-11ea-8d77-572e9123adfc.png)

# License

This Project uses the GNU General Public License Version 3.
