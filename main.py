from bs4 import BeautifulSoup
import requests, openai

html = requests.get("https://www.m.gortransperm.ru").text

print(html)

