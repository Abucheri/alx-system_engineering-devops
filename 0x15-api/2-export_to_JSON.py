#!/usr/bin/python3
"""
Fetches TODO list progress for a given
employee ID from JSONPlaceholder REST API
and exports the data to a JSON file.
"""

import json
import requests
from sys import argv


def get_employee_todo_progress(employee_id):
    """
    Retrieves TODO list progress for a given
    employee ID and exports data to a JSON file.

    Args:
        employee_id (int): Employee ID to fetch TODO list.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user data
    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    username = user.get("username")

    # Fetch TODO list for the user
    todos = (requests.get("{}/todos".format(base_url),
             params={"userId": employee_id}).json())

    # Prepare JSON data
    json_data = {str(employee_id): [
        {"task": task['title'],
            "completed": task['completed'],
            "username": username}
        for task in todos
    ]}

    # Export to JSON file
    json_filename = "{}.json".format(employee_id)
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    if len(argv) != 2:
        pass
    else:
        try:
            employee_id = int(argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            pass
