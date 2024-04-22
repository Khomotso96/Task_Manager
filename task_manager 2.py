#Import libraries
import datetime
import os

# Display current working directory
print("Current working directory:", os.getcwd())

# Dictionary to store users' credentials
users = {}

# Load users from user.txt
with open("user.txt", "r") as f:
    for line in f:
        parts = line.split(", ")
        if len(parts) == 2:
            username, password = parts
            password = password.strip()
            users[username] = password
        else:
            print("Invalid format in user.txt. Make sure each line contains a username and password separated by ', '.")

# Initialize variables for user login
current_user = ""
logged_in = False

# User login
while not logged_in:
    username = input("Enter your username: ")
    if username in users:
        password = input("Enter your password: ")
        if password == users[username]:
            current_user = username
            logged_in = True
            print(f"Welcome {current_user}!")
        else:
            print("Incorrect password. Please try again.")
    else:
        print("Invalid username. Please try again.")

# Main menu loop
while True:
    # Display menu options
    menu = input('''Select one of the following options: 
r - Register a user
a - Add task
va - View all tasks
vm - View my tasks
s - Statistics
e - Exit
: ''').lower()

    if menu == 'r':  # Register a new user
        if current_user == "admin":
            new_username = input("Enter a new username: ")
            if new_username in users:
                print("This username already exists. Please choose a different one.")
            else:
                new_password = input("Enter a new password: ")
                confirm_password = input("Confirm new password: ")
                if new_password == confirm_password:
                    with open("user.txt", "a") as f:
                        f.write(f"\n{new_username}, {new_password}")
                        users[new_username] = new_password
                        print(f"New user {new_username} has been registered.")
                else:
                    print("The passwords do not match. Please try again.")
        else:
            print("Only the admin can register a new user.")
    elif menu == 'a':  # Add a new task
        assigned_user = input("Enter the username of the person the task is assigned to: ")
        if assigned_user in users:
            task_title = input("Enter the title of the task: ")
            task_description = input("Enter task description: ")
            task_due_date = input("Enter due date for the task (dd/mm/yyyy): ")
            task_assigned_date = datetime.date.today().strftime("%d/%m/%y")
            with open("tasks.txt", "a") as f:
                f.write(f"\n{assigned_user}, {task_title}, {task_description}, {task_assigned_date}, {task_due_date}, No")
            print(f"New task {task_title} has been added.")
        else: 
            print("Invalid username. Please try again.")
    elif menu == 'va':  # View all tasks
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(", ")
                    if len(parts) == 6:
                        assigned_user, task_title, task_description, task_assigned_date, task_due_date, task_completed = parts
                        task_completed = task_completed.strip()
                        print(f"Task: {task_title}")
                        print(f"Assigned to: {assigned_user}")
                        print(f"Date assigned: {task_assigned_date}")
                        print(f"Due date: {task_due_date}")
                        print(f"Task complete: {task_completed}")
                        print(f"Task description: {task_description}")
                        print()
                    else: 
                        print("Invalid format in tasks.txt.")
        else:
            print("No tasks found.")
    elif menu == 'vm':  # View tasks assigned to the current user
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(", ")
                    if len(parts) == 6:
                        assigned_user, task_title, task_description, task_assigned_date, task_due_date, task_completed = parts
                        task_completed = task_completed.strip()
                        if current_user == assigned_user:
                            print(f"Task: {task_title}")
                            print(f"Assigned to: {assigned_user}")
                            print(f"Due date: {task_due_date}")
                            print(f"Task complete: {task_completed}")
                            print(f"Task description: {task_description}")
                            print()
                        else: 
                            print("No tasks found.")
                    else: 
                        print("Invalid format in tasks.txt.")
        else:
            print("No tasks found.")
    elif menu == 's':  # Display statistics
        if current_user == "admin":
            num_users = len(users)
            num_tasks = 0
            if os.path.exists("tasks.txt"):
                with open("tasks.txt", "r") as f:
                    num_tasks = sum(1 for line in f)
            print(f"Total number of users: {num_users}")
            print(f"Total number of tasks: {num_tasks}")
        else:
            print("Only the admin can view statistics.")
    elif menu == 'e':  # Exit
        print('Goodbye!!!')
        exit()
    else:
        print("You have entered an invalid input. Please try again.")
