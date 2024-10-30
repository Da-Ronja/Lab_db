import os
import requests
from dotenv import load_dotenv, dotenv_values


load_dotenv()
GITHUB_USER = os.getenv('GITHUB_USER')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')


def get_data():
    url = f'https://api.github.com/users/{GITHUB_USER}/repos'
    response = requests.get(url, headers={'Authorization': f'Bearer {BEARER_TOKEN}'})
    if response.status_code == 200:
        repos = response.json()
        
        repos_list = []
        for repo in repos:
            repos_list.append(repo['name'])


        return repos_list
    else:
        return f"Failed to retrieve repositories. Status code: {response.status_code}"

respons_repo = get_data()

if isinstance(respons_repo, list):
    for item in respons_repo:
        print(item)
else:
    print(respons_repo)
