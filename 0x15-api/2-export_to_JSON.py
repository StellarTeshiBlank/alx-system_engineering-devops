#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about an employee and export to JSON """
import json
import requests
import sys

def fetch_employee_tasks(user_id):
    """ Fetches user and task data, then writes to JSON file """
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

        # Prepare data for JSON
        task_list = [
            {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            }
            for task in tasks
        ]

        # Format data into dictionary
        data = {user_id: task_list}

        # Write data to JSON file
        filename = f'{user_id}.json'
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f'Data has been written to {filename}')

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./script.py <user_id>")
    else:
        fetch_employee_tasks(sys.argv[1])
