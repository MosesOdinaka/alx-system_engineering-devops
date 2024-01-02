#!/usr/bin/python3
"""
Fetches the TODO list progress for a specified employee ID using REST API.
"""
import csv
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

    filename = f"{user_id}.csv"
    with open(filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo_data:
            task_completed = task.get("completed")
            task_title = task.get("title")
            csv_writer.writerow([user_id, username,
                                 task_completed, task_title])
