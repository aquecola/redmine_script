from dotenv import load_dotenv, find_dotenv
import os
import requests

load_dotenv(find_dotenv())
env_key = (os.environ.get('KEY'))

redmine_url = 'https://example.com'
api_key = env_key

response = requests.get(f'{redmine_url}/projects.json', headers={'X-Redmine-API-Key': api_key})
projects = response.json()['projects']

for project in projects:
    print(f"Project ID: {project['id']}, Project Name: {project['name']}")
