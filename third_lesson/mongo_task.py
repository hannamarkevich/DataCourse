from pymongo import MongoClient
from second_lesson.hh import search_vacancies
from pprint import pprint

MONGO_URI = 'localhost:27017'
MONGO_DB = 'test_database'

# Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB и
# реализовать функцию, записывающую собранные вакансии в созданную БД.
def add_to_db(position):
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DB]
    collection = db[position]
    collection.insert_many(search_vacancies(position))

# функцию, которая производит поиск и выводит на экран вакансии с заработной
# платой больше введённой суммы, а также использование одновременно мин/макс
# зарплаты. Необязательно - возможность выбрать вакансии без указанных зарплат


def select_vacancies(position, salary):
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DB]
    collection = db[position]
    for item in list(collection.find({})):
        pprint(item)
    for item in list(collection.find({"max_salary": None})):
        pprint(item)


add_to_db("data")
select_vacancies("data", 3)

