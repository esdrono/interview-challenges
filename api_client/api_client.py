import requests
import json
import yaml

def read_todo_file(filename: str):
    with open(filename, 'r') as file:
        todos = json.load(file)
    return todos

def get_todo_list(ids: list):
    todos = []
    for id in ids:
        todo = get_todo(id)
        todos.append(todo)
    return todos

def get_todo(id: int):
    r = requests.get(f"https://jsonplaceholder.typicode.com/todos/{id}")
    return r.json()

def get_user(id: int):
    r = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}")
    return r.json()
