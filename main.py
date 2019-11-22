import bs4
import requests
import pandas as pd
import re, os
from io import StringIO
import numpy as np

path1 = os.path.realpath(__file__)
parentPath = os.path.dirname(path1)
urls = pd.read_csv(os.path.join(parentPath,"store","urls.csv")) 

username = os.environ.get('epiname')
password = os.environ.get('epipass')
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
            return "No article content to check"
        
        bodycopytext = bodycopy.get_text()
        print(bodycopytext)

        try:
            regex = r"\bher\b|\bshe\b|(\b[a-zA-Z][a-zA-Z]?\/\b)"
            test = re.findall(regex, bodycopytext)
            return len(test)
        except AttributeError:
            return "no match"
        except Exception as e:
            return "match error - "+str(e)

    except Exception as e:
        return "url error - "+str(e)

      


def final():
    #urls['check'] = urls["url"].apply(lambda x: Row(x.key), check(x) if x == 3 else None)
    #urls.iloc[1::5]

    df2 = urls.iloc[7:8]


    df2["check"] = df2["url"].apply(check)
    
    df2.to_csv(os.path.join(parentPath,"store","data.csv"),header=True)



if __name__ == "__main__":
    final()