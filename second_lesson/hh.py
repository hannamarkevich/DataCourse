import requests
import time
import pprint
# import pandas as pd
from bs4 import BeautifulSoup as bs
NOT_DEFINED = "По договорённости"
FROM = "от"
TILL = "до"
SPACE = " "
RUB = "руб."
BASE_URL = "https://www.superjob.ru/"
# DOLLAR = ""
vacancies = [
    {"title": "apple", "link": 3, "min_salary": "", "max_salary": ""}
]


def parse_salary(salary_str):
    result = {}
    salary_array = salary_str.split(SPACE)
    if salary_array[0] == FROM:
        result["min"] = int(salary_array[1]) * 1000 + int(salary_array[2])
        result["max"] = None
    elif salary_array[0] == TILL:
        result["min"] = None
        result["max"] = int(salary_array[1]) * 1000 + int(salary_array[2])
    elif salary_str == NOT_DEFINED:
        result["min"] = None
        result["max"] = None
    else:
        if "-" not in salary_array:
            result["min"] = int(salary_array[0]) * 1000 + int(salary_array[1])
            result["max"] = result["min"]
    return result


def collect_info(vacancies):
    res = []
    for vac in vacancies:
        for f in vac.findChildren(recursive=False):
            vac_dict = {}
            if f.find("a") is not None:
                if "vakansii" in f.find("a")["href"]:
                    vac_dict["name"] = f.find("a").text
                    vac_dict["link"] = BASE_URL + f.find("a")["href"]
                    salary = f.findChildren(recursive=False)[0].findChildren(recursive=False)[0].findChildren(recursive=False)[
                        0].findChildren(recursive=False)[2].findChildren(recursive=False)[0].findChildren(
                        recursive=False)[0].findChildren(recursive=False)[1].findChildren(recursive=False)[0].text
                    salary_value = parse_salary(salary)
                    vac_dict["salary_min"] = salary_value["min"]
                    vac_dict["salary_max"] = salary_value["max"]
                    res.append(vac_dict)
    return res

def search_vacancies(position):
    result = []
    url = "https://www.superjob.ru/vacancy/search/?keywords={}&geo%5Bt%5D%5B0%5D=4&page={}"
    proxies = {
        'https': 'https://36.89.156.146:8181',
    }
    page_num = 1
    r = requests.get(url.format(position, str(page_num)))
    print(url.format(position, str(page_num)))
    r = requests.get(url.format(position, str(page_num)))
    soup = bs(r.text, "html.parser")
    vacs = list(soup.find_all(attrs={"class": "f-test-search-result-item"}))
    result += collect_info(vacs)
    while len(list(soup.find_all('span', text="Дальше"))) > 0:
        vacs = list(soup.find_all(attrs={"class": "f-test-search-result-item"}))
        result.append(collect_info(vacs))
        r = requests.get(url.format(position, str(page_num)))
        page_num += 1
        soup = bs(r.text, "html.parser")
    return result
