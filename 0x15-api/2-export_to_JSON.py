#!/usr/bin/python3
"""
This script uses the provided REST API to fetch the TODO list progress
for a specified employee ID and exports the data in JSON format.
"""
import json
import requests
import sys

if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]

    user_url = f'{base_url}users/{user_id}'
    user_data = requests.get(user_url).json()
    username = user_data.get('username')

    todo_url = f'{base_url}todos'
    todo_data = requests.get(todo_url, params={'userId': user_id}).json()

    task_list = []
    for task in todo_data:
        task_info = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        task_list.append(task_info)

    filename = f"{user_id}.json"
    with open(filename, "w") as jsonfile:
        json.dump({user_id: task_list}, jsonfile)
