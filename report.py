import bs4
import requests
import pandas as pd
import os
import datetime
from io import StringIO

### Use REQUESTS to get a url, then assign the text of it to 'html'
path1 = os.path.dirname(os.path.realpath(__file__))
parentPath = os.path.dirname(path1)

username = os.environ.get('epiname')
password = os.environ.get('epipass')
details = "username=" + username + "&password=" + password
edit_login = "https://edit.citizensadvice.org.uk/login/?" + details





def epi_pages_report():
    path1 = os.path.abspath(__file__)
    parentPath = os.path.dirname(path1)

    epi_login = edit_login
    public = "https://edit.citizensadvice.org.uk/api/reports/section.csv?root=6_260261"
    advisernet = "https://edit.citizensadvice.org.uk/api/reports/section.csv?root=36473_242727"
    public = makeFrame(public)
    adviser = makeFrame(advisernet)
    public.to_pickle(os.path.join(parentPath,"store","public.pkl"))
    adviser.to_pickle(os.path.join(parentPath,"store","adviser.pkl"))

    return 1

 
def makeFrame(link):
    site = 'https://www.citizensadvice.org.uk'
    country_code = dict([
        ('en-GB',''),
        ('en-SCT','/scotland'),
        ('en-NIR','/nireland'),
        ('en-WLS','/wales'),
        ('cy','/cymraeg')
    ])
    with requests.Session() as login:
        login.get(edit_login)
        # wrapping next line in a 'with' statement to hopefully reduce failures
        # makes requests release the connection properly when stream = True
        with login.get(link, stream = True) as getting:
            sheet = StringIO(getting.text)

        frame = pd.read_csv(sheet)

        return frame

if __name__ == "__main__":
    epi_pages_report()