#!/usr/bin/python3
"""
Fetches the TODO list progress for a specified employee ID using REST API.
"""
import requests
import sys

if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]

    user_url = f'{base_url}users/{user_id}'
    user_data = requests.get(user_url).json()

    todo_url = f'{base_url}todos'
    todo_data = requests.get(todo_url, params={'userId': user_id}).json()

    completed_tasks = [
        task["title"] for task in todo_data if task['completed']
    ]

    employee_name = user_data.get('name')
    num_tasks = len(completed_tasks)
    total_tasks = len(todo_data)

    print(f"Employee {employee_name} is done with "
          f"tasks({num_tasks}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t {task}")
