#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    # Check if the script was given an argument (employee ID)
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Get the employee ID from the command line
    employee_id = sys.argv[1]

    try:
        # Convert employee_id to an integer
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    # Fetch user information
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    
    if user_response.status_code != 200:
        print(f"User with ID {employee_id} not found.")
        sys.exit(1)

    # Parse the user information
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch tasks for the user
    tasks_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    tasks_response = requests.get(tasks_url)
    tasks_data = tasks_response.json()

    # Filter tasks into completed and total
    completed_tasks = [task for task in tasks_data if task.get('completed')]
    total_tasks = len(tasks_data)

    # Print the employee's TODO list progress
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")

    # Print each completed task title
    for task in completed_tasks:
        print(f"\t {task.get('title')}")

