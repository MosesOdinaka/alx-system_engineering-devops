#!/usr/bin/python3
"""
This script uses the provided REST API to fetch the TODO list progress
for all employees and exports the data in JSON format.
"""
import json
import requests

if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com/'

    users_url = f'{base_url}users'
    users_data = requests.get(users_url).json()

    all_tasks = {}
    for user in users_data:
        user_id = user.get("id")
        username = user.get("username")

        todo_url = f'{base_url}todos'
        todo_data = requests.get(todo_url, params={'userId': user_id}).json()

        task_list = []
        for task in todo_data:
            task_info = {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            task_list.append(task_info)

        all_tasks[user_id] = task_list

    filename = "todo_all_employees.json"
    with open(filename, "w") as jsonfile:
        json.dump(all_tasks, jsonfile)
