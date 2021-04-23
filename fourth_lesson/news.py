import requests
from lxml import html
import pandas

MAIL_RU = "https://news.mail.ru/"
LENTA = "https://lenta.ru/"
YANDEX = "https://yandex.ru/news"

# Написать приложение, которое собирает основные новости с сайтов news.mail.ru, lenta.ru,
# yandex.news

r = requests.get(MAIL_RU)
dom = html.fromstring(r.text)

print()