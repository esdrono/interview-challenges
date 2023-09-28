import requests
import yaml

def read_todo_file(filename: str):
    todos = []
    with open(filename, 'rb') as file
        todos = yaml.safe_load(file)
    return todos

def get_todo_list(ids: list):
    todos = []
    ## TODO: implement this
    return todos

def get_todo(id: int):
    r = requests.get("https://jsonplaceholder.typicode.com/todos/{id}")
    return r.json()

def get_user(id: int):
    r = requests.get("https://jsonplaceholder.typicode.com/users/{id}")
    return r.json()

