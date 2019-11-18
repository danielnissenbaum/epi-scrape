import bs4
import requests
import pandas as pd
import re, os
from io import StringIO


def body_content():

    url = "https://www.citizensadvice.org.uk/work/rights-at-work/parental-rights/rights-while-youre-on-maternity-leave/"
    try:
        page = requests.get(url)
        html = page.text
        soup = bs4.BeautifulSoup(html, "lxml")
        bodycopy = soup.find(class_ = 'articleContent')
        bodycopytext = bodycopy.get_text()
        return bodycopytext
    except:
        return "no bodycopy"


def check(txt):
    try:
        return re.search(" her | she |(\b..?\/\b)", txt)
    except Exception as err:
        return err



def main():
    x = str(body_content())
    y = check(x)
    print(y)


if __name__ == "__main__":
    main()