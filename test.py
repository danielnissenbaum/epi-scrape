import bs4
import requests
import pandas as pd
import re, os
from io import StringIO


path1 = os.path.realpath(__file__)
parentPath = os.path.dirname(path1)

def main():
    urls = pd.read_csv(os.path.join(parentPath,"store","urls.csv"))
    x = urls[:5]
    print(x.index.values)



if __name__ == "__main__":
    main()