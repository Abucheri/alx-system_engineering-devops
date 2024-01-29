#!/usr/bin/python3
"""
Module for exporting tasks of all employees to JSON format.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = 'https://jsonplaceholder.typicode.com/users'

    # Fetching data from the API
    tasks = requests.get(url).json()
    users = requests.get(user_url).json()

    # Creating a dictionary to store tasks by user ID
    user_tasks = {}

    for user in users:
        user_id = str(user['id'])
        username = user['username']

        # Filtering tasks for the current user
        user_task_list = [
                {
                    "username": username,
                    "task": task['title'],
                    "completed": task['completed']
                }
                for task in tasks if task['userId'] == user['id']
            ]

        # Adding the user's tasks to the dictionary
        user_tasks[user_id] = user_task_list

    # Exporting the data to JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(user_tasks, json_file)
