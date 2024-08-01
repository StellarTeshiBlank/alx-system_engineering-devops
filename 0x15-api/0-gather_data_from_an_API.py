#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about an employee """
import requests
import sys

def fetch_employee_data(user_id):
    """ Fetch and print tasks for a given user ID """
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = f'{base_url}users/{user_id}'
    todos_url = f'{base_url}todos?userId={user_id}'

    try:
        # Fetch user data
        user_res = requests.get(user_url)
        user_res.raise_for_status()  # Raise HTTPError for bad responses
        user_data = user_res.json()
        name = user_data.get('name', 'Unknown User')

        # Fetch tasks
        todos_res = requests.get(todos_url)
        todos_res.raise_for_status()  # Raise HTTPError for bad responses
        tasks = todos_res.json()

        # Filter completed tasks
        completed_tasks = [task for task in tasks if task.get('completed')]

        # Print results
        print(f"Employee {name} is done with tasks({len(completed_tasks)}/{len(tasks)}):")
        for task in completed_tasks:
            print(f"\t {task.get('title')}")
    
    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./script.py <user_id>")
    else:
        fetch_employee_data(sys.argv[1])
