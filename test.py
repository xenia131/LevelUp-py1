import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

resp = requests.get("http://learn.python.ru/")
print(resp.text)