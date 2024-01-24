from bs4 import BeautifulSoup
import requests, openai

html = requests.get("https://www.m.gortransperm.ru/stoppoint-arrival-times/55100/").text


print(html)

