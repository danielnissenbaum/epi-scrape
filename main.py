import bs4
import requests
import pandas as pd
import re, os
from io import StringIO
import numpy as np
from multiprocessing import cpu_count, Pool

cores = cpu_count() #Number of CPU cores on your system
partitions = cores #Define as many partitions as you want

path1 = os.path.realpath(__file__)
parentPath = os.path.dirname(path1)
urls = pd.read_csv(os.path.join(parentPath,"store","urls.csv")) 

def check(url):
    try:
        page = requests.get(url)
        html = page.text
        soup = bs4.BeautifulSoup(html, "lxml")
        bodycopy = soup.find(class_ = 'articleContent')
        bodycopytext = bodycopy.get_text()
        #return bodycopy
        try: 
            return re.search(" her | she |(\b..?\/\b)", bodycopytext)
        except:
            return "a checking error"
    except:
        return "no bodycopy"

      



def final():
    #urls['check'] = urls["url"].apply(lambda x: Row(x.key), check(x) if x == 3 else None)
    #
    #urls.iloc[1::5]

    df2 = urls.iloc[1::5]


    df2["check"] = df2["url"].apply(check)
    
    df2.to_csv(os.path.join(parentPath,"store","data.csv"),header=True)



if __name__ == "__main__":
    final()