import datetime
import os

print("Current working directory:", os.getcwd())

# Initialize dictionary to store usernames and passwords
users = {}

# Read usernames and passwords from user.txt
with open("user.txt", "r") as f:
    for line in f:
        parts = line.split(", ")
        if len(parts) == 2:
            username, password = parts
            password = password.strip()
            users[username] = password
        else:
            print("Invalid format in user.txt. Make sure each line contains a username and password separated by ', '.")

current_user = ""
logged_in = False

# Loop until logged in
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
    menu = input('''Select one of the following options: 
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()
    
    # Register a new user (admin only)
    if menu == 'r':
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
    
    # Add a new task
    elif menu == 'a':
        assigned_user = input("Enter the username of the person the task is assigned to: ")
        if assigned_user in users:
            task_title = input("Enter the title of the task: ")
            task_description = input("Enter task description: ")
            task_due_date = input("Enter due date for the task (dd/mm/yyyy): ")
            task_assigned_date = datetime.date.today().strftime("%d/%m/%y")
            # Prompt user for task completion status until valid input is provided
            while True:
                task_completed = input("Is the task completed? (Yes/No): ").lower()
                if task_completed in ['yes', 'no']:
                    break
                else:
                    print("Invalid input. Please enter either 'Yes' or 'No'.")
            # Write task data to tasks.txt
            with open("tasks.txt", "a") as f:
                f.write(f"\n{assigned_user}, {task_title}, {task_description}, {task_assigned_date}, {task_due_date}, {task_completed.capitalize()}")
            print(f"New task {task_title} has been added.")
        else: 
            print("Invalid username. Please try again.")

    # View all tasks
    elif menu == 'va':
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
                        print("No tasks found.")

    # View tasks assigned to current user
    elif menu == 'vm':
        if os.path.exists("tasks.txt"):
            found_task = False
            with open("tasks.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(", ")
                    if len(parts) == 6:
                        assigned_user, task_title, task_description, task_assigned_date, task_due_date, task_completed = parts
                        task_completed = task_completed.strip()
                        if current_user == assigned_user:
                            found_task = True
                            print(f"Task: {task_title}")
                            print(f"Assigned to: {assigned_user}")
                            print(f"Due date: {task_due_date}")
                            print(f"Task complete: {task_completed}")
                            print(f"Task description: {task_description}")
                            print()
                        if not found_task:
                            print("No tasks found for the current user.")
                                
                    else:
                        print("No tasks found.")
                                
    # exit application
    elif menu == 'e':
        print("Goodbye!!!")
        exit()
    else:
        print("You have entered and invalid input. Please try again.")