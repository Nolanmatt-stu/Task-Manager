'''This code is a multi-user task manager in which:
    Users can be added and removed
    New tasks can be added and removed
    Tasks can be viewed and edited
    Reports and statistics regarding the list of tasks can be created in .txt files'''

# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: Admin
# password: Password
# 2. Ensure you open the whole folder for this programme in VS Code otherwise the 
# program will look in your root directory for the text files.

#Functions:

def reg_user():
    '''Add a new user to the user.txt file'''
    # - Request input of a new username
    
    while True:
        new_username = input("New Username: ")

        with open("user.txt", "r") as usernames:
            file_check = usernames.read()
            if new_username in file_check:
                print("That username is already taken, please enter a new username")
                continue
            break
    while True:
        
        new_password = input("New Password: ")
        confirm_password = input("Confirm Password: ")
 
        # - Check if the new password and confirmed password are the same.   
        if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
            print("New user added")

            username_password[new_username] = new_password

            new_username_password = new_username + ";" + new_password

            
            with open("user.txt", 'a') as out_file:
                out_file.write(f"\n{new_username_password}")
                break
        print("Passwords do no match")

def add_task():
    '''Allows a user to add a new task to task.txt file
            Prompts the user for the following: 
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and 
             - the due date of the task.'''
    while True:
        task_username = input("Name of person assigned to task: ").strip()
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
            continue
        elif task_username == "Admin":
            print("The Admin user cannot be assigned tasks. Please enter a different valid username")
            continue
            
        break

    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = str(date.fromisoformat(task_due_date))
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")
        

    
    # Then get the current date.
    curr_date = str(date.today())
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }
    
    task_list.append(new_task)
    
    with open("tasks.txt", "w") as task_file:
        
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'],
                t['assigned_date'],
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")

def view_all():
    '''Reads the task from task.txt file and prints to the console'''
    
    while True:
        task_number = 0
        for t in task_list:

            disp_str = f"Task {task_number}: \t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date']}\n"
            disp_str += f"Due Date: \t {t['due_date']}\n"
            disp_str += f"Task Description: \n{t['description']}\n"
            print(disp_str)
            task_number += 1
        print()
        return_choice = input("Enter 'Y' to retun to main menu: ")
        if return_choice == 'Y':
            os.system('cls')
            break
        else:
            continue
            
                

def view_mine():
    '''Reads the task from task.txt file and prints to the console'''

    task_number = 0
    for t in task_list:
        #
        if t['username'] == curr_user:
            disp_str = f"Task {task_number}: \t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date']}\n"
            disp_str += f"Due Date: \t {t['due_date']}\n"
            disp_str += f"Task Description: \n{t['description']}\n"
            print(disp_str)
        task_number += 1
    
    
    while True:
        try: task_choice = int(input("""Please enter the number of the task that you would like to edit or mark complete \nYou can also enter "-1" to return to the main menu """))
        except ValueError:
            print("invalid character entered, please enter one of the numbers shown")
        else:                
        
            if task_choice == -1:
                break
            else: 
                os.system('cls')
                while True:
                    try: edit_or_complete = int(input(f"Would you like to: \n1. Edit Task {task_choice}: {task_list[task_choice]['title']} \n2. Mark this task as complete "))
                    except ValueError:
                                print("invalid character entered, please enter one of the numbers shown")
                    else:              
                        if edit_or_complete == 1:
                            if task_list[task_choice]['completed'] is True:
                                print("This task cannot be edited as it has already been completed")
                            else:
                                os.system('cls')
                                while True:
                                    try: edit_choice = int(input("""Select the number of the option you would like to edit: \n1) Assigned User \n2) Due Date
                        You can also enter "-1" to return to the main menu """))
                                    
                                    
                                    except ValueError:
                                        print("invalid character entered, please enter one of the numbers shown")

                                    #This False value is used later so that the user can break out of a sub-menu back to this one without having to start the whole loop again    
                                    due_date_amended = False
                                    if task_choice == -1:
                                        break
                                    if edit_choice == 1:

                                        #This while loop searches for the user's input in the list of usernames, 
                                        #assigning the task to that user if found
                                        while True:
                                            new_assigned_user = input("Please enter the user you would like to reassign this task to: ")
                                            if new_assigned_user not in username_password.keys():
                                                print("User not found in database, please try again or enter '-1' to return to the previous menu")
                                                if new_assigned_user == -1:
                                                    break
                                                else:
                                                    continue
                                            else:
                                                with open('tasks.txt','r') as tasks:
                                                    task_data = tasks.readlines()

                                                task_split = task_data[task_choice].split(";")
                                                task_split[0] = new_assigned_user
                                                task_with_new_user = ';'.join(task_split)

                                                task_data[task_choice] = task_with_new_user

                                                with open('tasks.txt','w') as tasks:
                                                    tasks.write("".join(task_data))

                                                print(f"Task {task_choice}:  {task_list[task_choice]['title']} has been successfully assigned to {new_assigned_user} ")
                                                break
                                    
                                    
                                #This choice takes new input and replaces the date and time of the selected task
                                    elif edit_choice == 2:

                                        if due_date_amended is True:
                                            break
                                        while True:
                                            try:
                                                os.system('cls')
                                                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                                                due_date_time = date.fromisoformat(task_due_date)
                                                with open('tasks.txt','r') as tasks:
                                                    task_data = tasks.readlines()

                                                task_split = task_data[task_choice].split(";")
                                                task_split[3] = str(due_date_time)
                                                task_with_new_date = ';'.join(task_split)

                                                task_data[task_choice] = task_with_new_date

                                                with open('tasks.txt','w') as tasks:
                                                    tasks.write("".join(task_data))
                                                print("Due date amended")

                                                #This value is now True so that the user breaks out of this While loop but not the enclosing While loop
                                                due_date_amended = True
                                                break

                                            except ValueError:
                                                print("Invalid datetime format. Please use the format specified")
                                                continue

                                            
                                                


                                    else:
                                        print("Invalid character entered.  Please type '1' or '2' to select an option: ")

                    #This choice will search through the tasks.txt file for the completion status of a task and change it to "Yes"
                    #It then changes the status to True so that the task can no longer be edited within this function
                        elif edit_or_complete == 2:
                                with open('tasks.txt','r') as tasks:
                                    task_data = tasks.readlines()

                                task_split = task_data[task_choice].split(";")
                                task_split[-1] = "Yes\n"
                                task_now_completed = ';'.join(task_split)

                                task_data[task_choice] = task_now_completed

                                with open('tasks.txt','w') as tasks:
                                    tasks.write("".join(task_data))
                                task_list[task_choice]['completed'] = True


                                print("Congratulations! Task Completed")
                        else:
                            print("Invalid character entered.  Please type '1' or '2' to select an option: ")

def gen_reports():
    '''Takes input from the tasks.txt file and generates to new output files:
            task_overview.txt:
                Shows statistics relating to the entire list of tasks across all users
                  
            user_overview.txt:
                Shows statistics relating to the tasks of each user separately'''
   
    with open('task_overview.txt', 'w') as task_file:
        with open('tasks.txt', 'r') as tasks_list:
            #These variables will act as counters  
        
            total_num_of_tasks = 0
            total_completed_tasks = 0
            total_uncompleted_tasks = 0
            total_overdue_tasks = 0

            #This for loop will read each line of the tasks_list and update the above counter variables 
            for task in tasks_list:
                total_num_of_tasks += 1
                
                if task[-3:] == "Yes":
                    total_completed_tasks += 1
                else:
                    total_uncompleted_tasks +=1
                    
                    #This will compare the due date of the task with the current date 
                    due_date = task[-25:-15]
                    current_time = datetime.now()
                    today_date = current_time.strftime(DATETIME_STRING_FORMAT) 
                    
                    if due_date < today_date:
                        total_overdue_tasks += 1

        #These will calculate the percentages to the nearest integer        
        percentage_incompleted_task = (f"{round((total_uncompleted_tasks / total_num_of_tasks) *100)}%") 
        percentage_overdue_task = (f"{round((total_overdue_tasks / total_num_of_tasks) *100)}%")  


        task_file.write (f"Total number of tasks: {total_num_of_tasks}\n")
        task_file.write (f"Total completed tasks: {total_completed_tasks}\n") 
        task_file.write (f"Total uncompleted tasks: {total_uncompleted_tasks}\n") 
        task_file.write (f"Total overdue tasks: {total_overdue_tasks}\n") 
        task_file.write (f"Percentage of tasks that are incomplete: {percentage_incompleted_task}\n")
        task_file.write (f"Percentage of tasks that are overdue: {percentage_overdue_task}\n")


    #This section will work similarly to the previous loop that added to the 'total' counters and created the task_overview.txt file
    #Except this time it will only be counting for a specific user at a time

    with open('user_overview.txt', 'w') as user_file:
        list_of_usernames = []
        user_data_string_dict = {}
        #Uses the user.txt file to create list of users, excluding 'Admin' as they will not have tasks assigned
        with open('user.txt','r') as user_list:
            for line in user_list:             
                i = line.index(';')
                user = line[:i]
                if user != "Admin":
                    list_of_usernames.append(user)

        
        for person in list_of_usernames:
            
            user_data_string_dict[person] = ''

        for person in list_of_usernames:
            total_user_assigned_tasks = 0
            total_user_completed_tasks = 0
            total_user_uncompleted_tasks = 0
            total_user_overdue_tasks = 0

            with open('tasks.txt', 'r') as tasks_list:
                
                #Reads the user data in tasks.txt create a variable that will be compared to the list_of_usernames
                for line in tasks_list:    
                    i = line.index(';')
                    task_assigned_to = line[:i]        

                    if person == task_assigned_to:
                
                        total_user_assigned_tasks += 1
                        
                        #Determines if the task has been marked complete
                        if line[-3:] == "Yes":
                            total_user_completed_tasks += 1
                        else:
                            total_user_uncompleted_tasks +=1
                            
                            #This will compare the due date of the task with the current date, determining if the task is overdue
                            due_date = line[-25:-15]
                            current_time = datetime.now()
                            today_date = current_time.strftime(DATETIME_STRING_FORMAT) 
                            
                            if due_date < today_date:
                                total_user_overdue_tasks += 1
                            
                #These strings with produce a percentage rounded to the nearest integer
                percent_assigned_to_user = (f"{round((total_user_assigned_tasks/ total_num_of_tasks) *100)}%")
                percent_assigned_to_user_completed = (f"{round((total_user_completed_tasks / total_user_assigned_tasks) *100)}%")
                percent_assigned_to_user_incomplete = (f"{round((total_user_uncompleted_tasks / total_user_assigned_tasks) * 100)}%")
                percent_assigned_to_user_overdue = (f"{round((total_user_overdue_tasks / total_user_assigned_tasks) * 100)}%")
            
                #This creates a string containing all of the user's information to be displayed
                user_data_string = ((f"{person}\n")+
                (f"Total tasks assigned: {total_user_assigned_tasks} \n") +
                (f"Percentage of the total tasks assigned: {percent_assigned_to_user} \n") + 
                (f"Percentage of tasks completed: {percent_assigned_to_user_completed} \n") + 
                (f"Percentage of tasks not yet completed: {percent_assigned_to_user_incomplete} \n") +
                (f"Percentage of tasks overdue: {percent_assigned_to_user_overdue}\n") +
                "--------------------------------- \n")

            user_data_string_dict[person] = user_data_string
        
        #Writes the data to the file in a readable format
        user_file.write(f"Total tasks: {total_num_of_tasks}\n")
        user_file.write("--------------------------------- \n")
        for i in user_data_string_dict:
            user_file.write (user_data_string_dict[i])

def display_stats():
    '''If the user is an admin they can display statistics about number of users and tasks.'''
    if curr_user == 'Admin': 
        
            with open('users.txt','r') as users:
                num_users = 0
                for line in users:
                    num_users += 1
            
            with open('tasks.txt','r') as tasks:
                num_tasks = 0
                for line in tasks:
                    num_users += 1

            print("-----------------------------------")
            print(f"Number of users: \t\t {num_users}")
            print(f"Number of tasks: \t\t {num_tasks}")
            print("-----------------------------------")  

    else:
        print("You do not have Admin status.  Login as a system admin to access statistics") 
        

#=====importing libraries===========
import os
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
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = task_components[3]
    curr_t['assigned_date'] = task_components[4]
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("Admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    # user_data = user_file.read().split("\n")
    username_password = {}
    for user in user_file:
        username , password = user.split(';')
        username_password[username] = password.strip("\n")

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
        logged_in = True
        os.system('cls')
        print("Login Successful!")


while True:
    
    print(f"Current user: {curr_user}\n")
    
    # presenting the menu to the user and ensuring that the user input is converted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my tasks
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()


    if menu == 'r':
        os.system('cls')
        reg_user()

    elif menu == 'a':
        os.system('cls')
        add_task()

    elif menu == 'va':
        os.system('cls')
        view_all()

    elif menu == 'vm':
        os.system('cls')
        view_mine()

    elif menu == 'gr':
        os.system('cls')
        gen_reports()
        print("Reports have been generated within this folder")
        print("Please see files 'task_overview.txt' and 'user_overview.txt' ")          
    
    elif menu == 'ds':
        os.system('cls')
        display_stats()
        
    elif menu == 'e':
        print('Goodbye!')
        exit()

    else:
        print(f"Unfortunately, {menu} is not a selectable option. Please Try again")