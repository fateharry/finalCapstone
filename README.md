**Task Management System**

This is a task management system written in Python. It allows users to add, view, edit, and mark tasks as complete. It also offers functionalities for user registration, generating reports, and displaying statistics (for admins).

**Features:**

**User Login and Registration:** Manages user accounts with usernames and passwords.

**Task Management:**

Add tasks with title, description, assigned user, and due date.
View all tasks or view tasks assigned to a specific user.
Mark tasks as complete.
Edit task details (assigned user and due date) for incomplete tasks (admin functionality not included).
Reporting (Admin only):
Generates reports on task completion status, overdue tasks, and user task assignment.
Statistics (Admin only):
Displays statistics on the total number of users and tasks.

**Requirements:**

Python 3.x

**How to Use:**

Clone or download the repository.
Open a terminal or command prompt and navigate to the directory containing the script.
Run the script using python task_management.py (replace task_management.py with the actual filename if different).

**User Interface:**
The program uses a text-based interface for user interaction. Users will be prompted to select options from a menu.

**File Usage:**

**tasks.txt:** Stores task data in a semi-colon separated format (username;title;description;due_date;assigned_date;completed).
**user.txt:** Stores user credentials in a username;password format (one pair per line).
**task_overview.txt** and **user_overview.txt** (generated): Stores generated reports on tasks and users (admin only).

**Notes:**
Ensure you open the entire folder for this task in VS Code, otherwise, the program will look in your root directory for the text files.
The username and password used for initial login are **"admin"** and **"password"** respectively. These credentials are stored in plain text in user.txt for simplicity. In a production environment, consider more secure password storage mechanisms (e.g., hashing).

**Exiting the Program:**

Type **e** at the main menu prompt to exit the program.
