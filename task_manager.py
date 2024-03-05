# Notes:
# 1. Use the following username and password to access the admin rights
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the
# program will look in your root directory for the text files.

# =====importing libraries===========
import os # for creation and management of files and directories
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

task_list = []
for t_str in task_data:
    current_task = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    current_task['username'] = task_components[0]
    current_task['title'] = task_components[1]
    current_task['description'] = task_components[2]
    current_task['due_date'] = datetime.strptime(
        task_components[3], DATETIME_STRING_FORMAT)
    current_task['assigned_date'] = datetime.strptime(
        task_components[4], DATETIME_STRING_FORMAT)
    current_task['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(current_task)

# ====Login Section====
"""This code reads usernames and password from the user.txt file to 
    allow a user to login.
"""


def clear_screen():
    # Clear the screen based on the platform (windows operation system)
    os.system('cls' if os.name == 'nt' else 'clear')


clear_screen()

# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:
    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


def user_reg():
    # Function to register a new user.
    while True:
        # - Request input of a new username
        new_username = input("New Username: ")

        # Check if the username already exists
        if new_username in username_password.keys():
            print("Error: Username already exists. Please choose a different username.")
        else:
            # - Request input of a new password
            new_password = input("New Password: ")
            # - Request input of password confirmation.
            confirm_password = input("Confirm Password: ")
            # - Check if the new password and confirmed password are the same.
            if new_password == confirm_password:
                # - If they are the same, add them to the user.txt file
                print("New user added")
                username_password[new_username] = new_password

                with open("user.txt", "w") as out_file:
                    user_data = [
                        f"{k};{username_password[k]}" for k in username_password]
                    out_file.write("\n".join(user_data))
                break  # Break out of the loop if registration is successful
            else:
                print("Passwords do not match")


def add_task():
    """
    Function to add a new task. Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and 
             - the due date of the task.
    """

    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        return
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")

    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(
                task_due_date, DATETIME_STRING_FORMAT)

            # Check if the due date is before today's date
            if due_date_time.date() < date.today():
                print("Error: Due date cannot be before today's date.")
                continue

            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # Then get the current date.
    curr_date = date.today()
    """
    Add the data to the file task.txt and
    Include 'No' to indicate if the task is complete.
    """
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "a") as task_file:
        str_attrs = [
            new_task['username'],
            new_task['title'],
            new_task['description'],
            new_task['due_date'].strftime(DATETIME_STRING_FORMAT),
            new_task['assigned_date'].strftime(DATETIME_STRING_FORMAT),
            "Yes" if new_task['completed'] else "No"
        ]
        task_file.write(";".join(str_attrs) + "\n")
    print("Task successfully added.")


def view_all():
    """
    Function to view all tasks. Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
    """
    task_number = len(task_list)
    if task_number == 0:
        print("Sorry, there is no task to display at this time")
        return
    
    for t in task_list:
        disp_str = f"    Task: \t\t {t['title']}\n"
        disp_str += f"   Assigned to: \t {t['username']}\n"
        disp_str += f"   Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"   Due Date: \t\t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"   Task Description: \t {t['description']}\n"
        print(disp_str)


def view_mine():
    """
    Function to view tasks assigned to the current user. Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
    """
    while True:
        print("\nTasks assigned to you:")
        for index, t in enumerate(task_list, start=1):
            if t['username'] == curr_user:
                disp_str = f"{index}.   Task: \t\t {t['title']}\n"
                disp_str += f"   Assigned to: \t {t['username']}\n"
                disp_str += f"   Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"   Due Date: \t\t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"   Task Description: \t {t['description']}\n"
                disp_str += f"   Completed: \t\t {'Yes' if t['completed'] else 'No'}\n"
                print(disp_str)

        selected_task = input(
            "Enter the task number to mark as complete or edit, or enter '-1' to return to the main menu: ")

        if selected_task == '-1':
            return  # Return to the main menu

        try:
            selected_task_index = int(selected_task)
            selected_task_index -= 1  # Adjust for 0-based indexing

            if 0 <= selected_task_index < len(task_list) and task_list[selected_task_index]['username'] == curr_user:
                action = input(
                    "Enter 'c' to mark as complete, 'e' to edit, or any other key to cancel: ").lower()

                if action == 'c':
                    task_list[selected_task_index]['completed'] = True
                    print("Task marked as complete.")
                elif action == 'e' and not task_list[selected_task_index]['completed']:
                    new_username = input(
                        "Enter the new assigned username (leave blank to keep current): ")
                    new_due_date = input(
                        "Enter the new due date (YYYY-MM-DD, leave blank to keep current): ")

                    if new_username:
                        task_list[selected_task_index]['username'] = new_username

                    if new_due_date:
                        try:
                            task_list[selected_task_index]['due_date'] = datetime.strptime(
                                new_due_date, DATETIME_STRING_FORMAT)
                        except ValueError:
                            print(
                                "Invalid datetime format. Task due date not updated.")

                    with open("tasks.txt", "w") as task_file:
                        task_list_to_write = []
                        for t in task_list:
                            str_attrs = [
                                t['username'],
                                t['title'],
                                t['description'],
                                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                                t['assigned_date'].strftime(
                                    DATETIME_STRING_FORMAT),
                                "Yes" if t['completed'] else "No"
                            ]
                            task_list_to_write.append(";".join(str_attrs))
                        task_file.write("\n".join(task_list_to_write))
                    print("Task edited successfully.")
                else:
                    print("Action cancelled.")

            else:
                print("Invalid task selection. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a valid task number.")


def display_statistics():
    """
    Function to display statistics. If the user is an admin they can display statistics about number of users
            and tasks.
    """
    num_users = len(username_password.keys())
    num_tasks = len(task_list)

    print("-----------------------------------")
    print(f"Number of users: \t\t {num_users}")
    print(f"Number of tasks: \t\t {num_tasks}")
    print("-----------------------------------")

    while True:
        print("\nStatistics Menu:")
        print("1. Display Existing Reports")
        print("2. Generate Reports and Display")
        print("3. Return to Main Menu")

        choice = input("Enter your choice (1, 2, or 3): ")

        match choice:

          case '1':
              if os.path.exists("task_overview.txt") and os.path.exists("user_overview.txt"):
                  with open("task_overview.txt", 'r') as task_file:
                      print("\n")
                      print(task_file.read())

                  with open("user_overview.txt", 'r') as user_file:
                      print("\n")
                      print(user_file.read())
              else:
                  print("No existing reports found. Please generate reports first.")

          case '2':
              if not os.path.exists("task_overview.txt") or not os.path.exists("user_overview.txt"):
                  generate_reports(task_list)

              with open("task_overview.txt", 'r') as task_file:
                  print("\n")
                  print(task_file.read())

              with open("user_overview.txt", 'r') as user_file:
                  print("\n")
                  print(user_file.read())

          case '3':
              return  # Return to the main menu

          case _:
              print("Invalid choice. Please enter 1, 2, or 3.")


def generate_reports(task_list):
    # Function to generate reports.
    total_tasks = len(task_list)

    if total_tasks == 0:
        print("No tasks to generate reports.")
        return
    completed_tasks = sum(task['completed'] for task in task_list)
    incomplete_tasks = total_tasks - completed_tasks
    overdue_tasks = sum(
        1 for task in task_list if not task['completed'] and task['due_date'].date() < date.today())

    total_users = len(username_password)
    tasks_assigned_to_users = [
        task for task in task_list if task['username'] in username_password.keys()]
    tasks_assigned_to_each_user = {user: tasks_assigned_to_users.count(
        user) for user in username_password.keys()}

    with open("task_overview.txt", "w") as task_overview_file:
        task_overview_file.write("Task Overview Report\n")
        task_overview_file.write(f"Total Tasks: {total_tasks}\n")
        task_overview_file.write(f"Completed Tasks: {completed_tasks}\n")
        task_overview_file.write(f"Incomplete Tasks: {incomplete_tasks}\n")
        task_overview_file.write(f"Overdue Tasks: {overdue_tasks}\n")
        task_overview_file.write(
            f"Percentage of Incomplete Tasks: {(incomplete_tasks / total_tasks) * 100:.2f}%\n")
        task_overview_file.write(
            f"Percentage of Overdue Tasks: {(overdue_tasks / total_tasks) * 100:.2f}%\n")

    with open("user_overview.txt", "w") as user_overview_file:
        user_overview_file.write("User Overview Report\n")
        user_overview_file.write(f"Total Users: {total_users}\n")
        user_overview_file.write(f"Total Tasks: {total_tasks}\n")
        for user, tasks_assigned in tasks_assigned_to_each_user.items():
            tasks_assigned = sum(1 for task in tasks_assigned_to_users if
                                 task['username'] == user)
            completed_tasks_user = sum(1 for task in tasks_assigned_to_users if
                                       task['username'] == user and task['completed'])
            incomplete_tasks_user = tasks_assigned - completed_tasks_user
            overdue_tasks_user = sum(1 for task in tasks_assigned_to_users if
                                     task['username'] == user and not task['completed'] and task[
                                         'due_date'].date() < date.today())

            user_overview_file.write(f"\nUser: {user}\n")
            user_overview_file.write(f"Tasks Assigned: {tasks_assigned}\n")
            user_overview_file.write(
                f"Percentage of Total Tasks Assigned: {(tasks_assigned / total_tasks) * 100:.2f}%\n")

            if tasks_assigned > 0:
                user_overview_file.write(
                    f"Percentage of Completed Tasks: {(completed_tasks_user / tasks_assigned) * 100:.2f}%\n")
                user_overview_file.write(
                    f"Percentage of Incomplete Tasks: {(incomplete_tasks_user / tasks_assigned) * 100:.2f}%\n")
                user_overview_file.write(
                    f"Percentage of Overdue Tasks: {(overdue_tasks_user / tasks_assigned) * 100:.2f}%\n")
                user_overview_file.write(
                    f"Percentage of Tasks that Must Still be Completed: {((incomplete_tasks_user - overdue_tasks_user) / tasks_assigned) * 100:.2f}%\n")
                user_overview_file.write(
                    f"Percentage of Overdue and Incomplete Tasks: {(overdue_tasks_user / tasks_assigned) * 100:.2f}%\n")

            else:
                user_overview_file.write(
                    "No tasks assigned to this user.\n")

    print("Reports generated successfully.")


# Main menu
clear_screen()


while True:
    # presenting the menu to the user and making sure that the user input is converted to lower case.
    print()
    menu = input('''
******************************************************************************
Please select one of the following options: \n
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
******************************************************************************
: ''').lower()

    if menu == 'r':
        # Add a new user to the user.txt file
        user_reg()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()

    elif menu == 'gr' and curr_user == 'admin':
        generate_reports(task_list)

    elif menu == 'ds' and curr_user == 'admin':
        display_statistics()

    elif menu == 'e':
        print('\nExiting the program now..Goodbye!')
        print('-'*60)
        exit()

    else:
        print("You have made a wrong choice, Please Try again")