#!/usr/bin/python3
"""
This script uses the provided REST API to fetch the TODO list progress 
for a specified employee ID.
"""
import requests
import sys

if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    
    user_data = requests.get(f'{base_url}users/{user_id}').json()
    todo_data = requests.get(f'{base_url}todos', params={'userId': user_id}).json()
    
    completed_tasks = [task["title"] for task in todo_data if task['completed']]
    
    print(f"Employee {user_data.get('name')} is done with tasks({len(completed_tasks)}/{len(todo_data)}):")
    for task in completed_tasks:
        print(f"\t {task}")
