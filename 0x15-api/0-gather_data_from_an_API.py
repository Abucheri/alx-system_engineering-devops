#!/usr/bin/python3
"""
Fetches TODO list progress for a given
employee ID from JSONPlaceholder REST API.
"""

import requests
from sys import argv


def get_employee_todo_progress(employee_id):
    """
    Retrieves and prints the TODO list progress for a given employee ID.

    Args:
        employee_id (int): Employee ID to fetch TODO list.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user data
    user_response = requests.get("{}/users/{}".format(base_url, employee_id))
    user_data = user_response.json()

    # Fetch TODO list for the user
    todo_response = requests.get("{}/todos?userId={}"
                                 .format(base_url, employee_id))
    todo_data = todo_response.json()

    # Calculate progress
    total_tasks = len(todo_data)
    done_tasks = sum(task['completed'] for task in todo_data)

    # Display information
    print("Employee {} is done with tasks({}/{total}):".format(
          user_data['name'], done_tasks, total=total_tasks))

    for task in todo_data:
        if task['completed']:
            print("\t{}".format(task['title']))


if __name__ == "__main__":
    if len(argv) != 2:
        pass
    else:
        try:
            employee_id = int(argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            pass
