#!/usr/bin/python3
# API

import requests

def fetch_employee_todo_progress(employee_id):
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Construct the URL for user details
    user_url = f"{base_url}/users/{employee_id}"
    
    # Send a GET request to fetch the user details
    response_user = requests.get(user_url)
    
    # Convert the response to a dictionary (JSON object)
    user_data = response_user.json()
    
    # Extract the employee's name from the user data
    employee_name = user_data['name']
    
    # Construct the URL for the employee's TODO list
    todos_url = f"{base_url}/todos?userId={employee_id}"
    
    # Send a GET request to fetch the TODO list
    response_todos = requests.get(todos_url)
    
    # Convert the response to a list of dictionaries (JSON array)
    todos_data = response_todos.json()
    
    # Calculate the total number of tasks
    total_tasks = len(todos_data)
    
    # Filter the list to only include completed tasks
    done_tasks = [task for task in todos_data if task['completed']]
    
    # Calculate the number of completed tasks
    number_of_done_tasks = len(done_tasks)
    
    # Print the progress information
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    
    # Print the titles of completed tasks
    for task in done_tasks:
        print(f"\t {task['title']}")

# Example usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            fetch_employee_todo_progress(employee_id)
        except ValueError:
            print("Please provide a valid integer for employee ID.")

