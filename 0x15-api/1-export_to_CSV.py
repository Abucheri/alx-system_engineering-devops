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
    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    username = user.get("username")
    todos = (requests.get("{}/todos".format(base_url),
             params={"userId": employee_id}).json())

    # Preparing CSV data
    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [employee_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]

    # print("Data exported to {}".format(csv_filename))


if __name__ == "__main__":
    if len(argv) != 2:
        pass
    else:
        try:
            employee_id = int(argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            pass
