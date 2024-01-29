from bs4 import BeautifulSoup
import requests, openai, aiogram
import csv
import telebot

url = 'https://www.m.gortransperm.ru/stoppoint-arrival-times/55100/'
bot = telebot.TeleBot('6826891756:AAFhGsMbOT-Y2C59XQ1e1uQUsOdwR-_9MTA')

#Функция отправляющая гет запрос
def parser(url):
    res = requests.get(url=url)
    soup = BeautifulSoup(res.text,"lxml")
    bus_stop = soup.find("div", class_='ui-content').find("h4").text.strip()
    print(bus_stop)
    bus_number = soup.find_all("li")

    for bus_time in bus_number:
        return bus_time.text

def sum():
    return 2+2


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, parser(url))


#Бесконечный цикл получения новых записей со стороны Telegram:
if __name__ == '__main__':
     bot.infinity_polling()
