import bs4
import requests
import pandas as pd
import re, os
from io import StringIO
import numpy as np
from tqdm import tqdm
from decouple import config



tqdm.pandas()

path1 = os.path.realpath(__file__)
parentPath = os.path.dirname(path1)
urls = pd.read_csv(os.path.join(parentPath,"store","urls.csv"))

username = config('epiname')
password = config('epipass')
details = "username=" + username + "&password=" + password
edit_login = "https://www.citizensadvice.org.uk/login/?" + details

s = requests.Session()
s.get(edit_login)



def check(url):
    try:
        page = s.get(url)
        html = page.text

        if page.status_code == 404:
            return "404 page"


        soup = bs4.BeautifulSoup(html, 'html.parser')
        bodycopy = soup.find(class_ = 'articleContent')
        if bodycopy is None:
            bodycopy = soup.find(class_ = 'main-content')
            if bodycopy is None:
                return "i can not search the text"


        bodycopytext = bodycopy.get_text()
        #print(bodycopytext)

        try:
            #regex = r"\btransgender\b|\bsame.?sex\b|\bgender\b|\btranssexual\b|\bsingle.?sex\b"
            #test = re.findall(regex, bodycopytext)
            word_list = bodycopytext.split()
            return len(word_list)
        except AttributeError:
            return "no match"
        except Exception as e:
            return "match error - "+str(e)

    except Exception as e:
        return "url error - "+str(e)




def final():
    #urls['check'] = urls["url"].apply(lambda x: Row(x.key), check(x) if x == 3 else None)
    #urls.iloc[1::5]

    df2 = urls


    df2["check"] = df2["url"].progress_apply(check)

    df2.to_csv(os.path.join(parentPath,"store","data.csv"),header=True)



if __name__ == "__main__":
    final()
