import requests
import json


def get_repos(username):
    base_url = "https://api.github.com"
    user_repositories_url = f"/users/{username}/repos"
    resp = requests.get(base_url+user_repositories_url).json()
    result = []
    for i in resp:
        result.append(i["name"])
    return result


print(get_repos("hannamarkevich"))

