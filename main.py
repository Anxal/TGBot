from bs4 import BeautifulSoup
import requests, openai
import csv

def parser(url:str):
    res = requests.get(url=url)
    soup = BeautifulSoup(res.text,"lxml")
    bus = soup.find_all("div", class_="ui-content")
    for bas in bus:
        namebus = bas.get("ul data-role")
    print(namebus)
    print(bus)

if __name__== "__main__":
    parser(url="https://www.m.gortransperm.ru/stoppoint-arrival-times/55100/")
