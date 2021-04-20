from pymongo import MongoClient
from second_lesson.hh import search_vacancies


def add_to_db(position):
    client = MongoClient('localhost', 27017)
    db = client['test_database']
    collection = db.cource_collection
    collection.insertMany(search_vacancies(position))
    print(db.vacancies.find({}))


add_to_db("data")

