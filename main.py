import bs4
import requests
import pandas as pd
import re, os
from io import StringIO

path1 = os.path.realpath(__file__)
parentPath = os.path.dirname(path1)


def body_content(url):
    try:
        page = requests.get(url)
        html = page.text
        soup = bs4.BeautifulSoup(html, "lxml")
        bodycopy = soup.find(class_ = 'articleContent')
        bodycopytext = bodycopy.get_text()
        return bodycopy
    except:
        return "no bodycopy"


def check(txt):
    try:
        return re.search(" her | she |(\b..?\/\b)", txt)
    except:
        return "a checking error"


def scrape():
    urls = pd.read_csv(os.path.join(parentPath,"store","urls.csv")) 

    for url in urls:
        text = body_content(url)
        response = check(text)
        return url, response    







def final():
    return "nope"





if __name__ == "__main__":
    final()