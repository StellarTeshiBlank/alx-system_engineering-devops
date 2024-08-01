#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about an employee and export to CSV """
import csv
import requests
import sys

def fetch_employee_data(user_id):
    """ Fetch user and tasks data, then write to CSV """
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = f'{base_url}users/{user_id}'
    todos_url = f'{base_url}todos?userId={user_id}'

    try:
        # Fetch user data
        user_res = requests.get(user_url)
        user_res.raise_for_status()  # Raise HTTPError for bad responses
        user_data = user_res.json()
        username = user_data.get('username', 'Unknown')

        # Fetch tasks
        todos_res = requests.get(todos_url)
        todos_res.raise_for_status()  # Raise HTTPError for bad responses
        tasks = todos_res.json()

        # Prepare data for CSV
        task_records = [
            [user_id, username, task.get('completed'), task.get('title')]
            for task in tasks
        ]

        # Write data to CSV file
        csv_filename = f'{user_id}.csv'
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            writer.writerows(task_records)
        print(f'Data has been written to {csv_filename}')

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./script.py <user_id>")
    else:
        fetch_employee_data(sys.argv[1])
