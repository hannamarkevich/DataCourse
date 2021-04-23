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
    return collection.find({})

# функцию, которая производит поиск и выводит на экран вакансии с заработной
# платой больше введённой суммы, а также использование одновременно мин/макс
# зарплаты. Необязательно - возможность выбрать вакансии без указанных зарплат


def select_vacancies(position, salary_min, salary_max):
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DB]
    collection = db[position]
    for item in list(collection.find({"salary_min": {"$gte": salary_min}})):
        pprint(item)
    for item in list(collection.find({"salary_max": {"$lte": salary_max}, "salary_min": {"$gte": salary_min}})):
        pprint(item)


def add_unique(database, record):
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DB]
    collection = db[database]
    if len(list(collection.find({"link": record["link"]}).count())) > 0:
        collection.insert_one(record)


rec = {'link': 'https://www.superjob.ru//vakansii/senior-frontend-razrabotchik-36691339.html',
 'name': 'Senior frontend-разработчик',
 'salary_max': 180000,
 'salary_min': 180000}
client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
collection = db["qa"]
#print(len(list(add_unique("qa", rec))))



# select_vacancies("data", 100000, 500000)

