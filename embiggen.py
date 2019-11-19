import requests
import pandas as pd
import re, os
from io import StringIO

path1 = os.path.realpath(__file__)
parentPath = os.path.dirname(path1)

def embiggen():
    public = pd.read_pickle(os.path.join(parentPath,"store","public.pkl"))
    adviser = public = pd.read_pickle(os.path.join(parentPath,"store","adviser.pkl"))
    report_list = [public,adviser]

    frames = []
    for report in report_list:
        frames.append(report)

    big_frame = pd.concat(frames)
    big_frame['url'] = 'https://www.citizensadvice.org.uk' + big_frame['Path']
    big_frame.to_pickle(os.path.join(parentPath,"store","big_frame.pkl"))
    urls = big_frame.url
    urls.to_csv(os.path.join(parentPath,"store","urls.csv"))
    

if __name__ == "__main__":
    embiggen()