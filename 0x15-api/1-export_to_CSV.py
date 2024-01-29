#!/usr/bin/python3
"""
Fetches TODO list progress for a given
employee ID from JSONPlaceholder REST API
and exports the data to a CSV file.
"""

import csv
import requests
from sys import argv


def get_employee_todo_progress(employee_id):
    """
    Retrieves TODO list progress for a given
    employee ID and exports data to a CSV file.

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

    # Prepare CSV data
    csv_data = ([["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                "TASK_TITLE"]])
    for task in todo_data:
        csv_data.append([
            str(user_data['id']),
            user_data['username'],
            str(task['completed']),
            task['title']
        ])

    # Export to CSV file
    csv_filename = "{}.csv".format(user_data['id'])
    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(csv_data)

    print("Data exported to {}".format(csv_filename))


if __name__ == "__main__":
    if len(argv) != 2:
        pass
    else:
        try:
            employee_id = int(argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            pass
