import bs4
import requests
import pandas as pd
import re, os
from io import StringIO

path1 = os.path.realpath(__file__)
parentPath = os.path.dirname(path1)

def scrape():

    public = pd.read_pickle(os.path.join(parentPath,"store","public.pkl"))
    adviser = public = pd.read_pickle(os.path.join(parentPath,"store","adviser.pkl"))

    report_list = [public,adviser]

    frames = []
    for report in report_list:
        frames.append(report)

    big_frame = pd.concat(frames)
    big_frame['url'] = 'https://www.citizensadvice.org.uk' + big_frame['Path']



    results = big_frame.Path

    urls = ["https://www.citizensadvice.org.uk" + page for page in results]


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

        

    big_frame['bodycontent'] = big_frame.url.map(body_content)



    #big_frame.to_pickle(os.path.join(parentPath,"store","big_frame_new.pkl"))

    return big_frame




def check(txt):
    try:
        return re.search(" her | she |(\b..?\/\b)", txt)
    except:
        return "an error"


def final():
    data = scrape()
    data['check'] = data.bodycontent.map(check)

    out = data[['url','check']]
    out.to_csv(os.path.join(parentPath,"store","out.csv"))


if __name__ == "__main__":
    final()