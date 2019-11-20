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
edit_login = "https://edit.citizensadvice.org.uk/login/?" + details



def check(url):
    try:
        with requests.Session() as login:
            login.get(edit_login)


            with login.get(url, stream = True) as getting:
                html = getting.text
                print(html)



        #s = requests.Session()
        #s.get(edit_login)

        #page = s.get(url)
        #html = page.text
        #print(page)


        #soup = bs4.BeautifulSoup(html, 'html.parser')
        #bodycopy = soup.find(class_ = 'articleContent')
        #bodycopytext = bodycopy.get_text()

        try: 
            return re.search(" her | she |(\b..?\/\b)", bodycopytext)
        except:
            return "a checking error"
    except Exception as e:
        return str(e)

      


def final():
    #urls['check'] = urls["url"].apply(lambda x: Row(x.key), check(x) if x == 3 else None)
    #urls.iloc[1::5]

    df2 = urls.iloc[1:2]


    df2["check"] = df2["url"].apply(check)
    
    df2.to_csv(os.path.join(parentPath,"store","data.csv"),header=True)



if __name__ == "__main__":
    final()