import json

def add_task(tasks):
    while True:
        task = input("Enter a task:")
        cleaned_task = task.strip()
        if cleaned_task == "":
            print("Write a task.")
            continue
        break
    tasks.append({
        "task": cleaned_task,
        "done": False
    })
    print("Task added!")
def show_tasks(tasks):
    if not tasks:
        print("No tasks.\nAdd a task")
    for number, task in enumerate(tasks, start=1):
        if task["done"] == False:
            print(number, task["task"], "- Не выполнено")
        else:
            print(number, task["task"], "- Выполнено")

def ask_user():
    choose = input("========== TASK MANAGER ==========\n1. Add task \n 2. Show tasks \n 3. Exit \n 4.Complete task\n 5.Delete task\n 6.Uncomplete task\n 7. Edit task\n 8. Search task\n==================================")
    return choose

def load_task():
    try:
        with open("tasks.json", "r") as data_file:
            data_read = data_file.read()
        tasks = json.loads(data_read)
    except FileNotFoundError:
        data_read = "[]"
        tasks = json.loads(data_read)
    return tasks

def save_task(tasks):
    with open("tasks.json", "w") as file_write:
        file_write.write(json.dumps(tasks))

def complete_task(tasks):
            number_of_task = get_task_index(tasks)
            if tasks[number_of_task]["done"] == True:
                print("Task is already completed.")
            else:
                tasks[number_of_task]["done"] = True
                save_task(tasks)

def delete_task(tasks):
        tasks.pop(get_task_index(tasks))
        save_task(tasks)
        print("Task deleted!")

def uncomplete_task(tasks):
        number_of_task = get_task_index(tasks)
        if tasks[number_of_task]["done"] == False:
            print("This task is already uncompleted")
        else:
            tasks[number_of_task]["done"] = False
            print("You changed the task status to not completed.")
        save_task(tasks)

def edit_task(tasks):
    number_of_task = get_task_index(tasks)
    while True:
        edit_input = input("Write a new task:")
        check_empty_list = edit_input.strip()
        if not check_empty_list:
           print("Write a tagit --versionsk.")
           continue
        else:
            tasks[number_of_task]["task"] = check_empty_list
            save_task(tasks)
            break

def search_task(tasks):
    while True:
        search_input = input("Search:").lower()
        delete_space = search_input.strip()
        found = False
        if delete_space:
            for task_list in tasks:
                if delete_space in task_list["task"].lower():
                        found = True
                        print(task_list["task"])

        if not found and delete_space:
            print("Nothing was found.")
            break
        if found:
            break
        if not delete_space:
            continue

def get_task_index(tasks):
    while True:
        show_tasks(tasks)
        try:
            task_number = int(input("Enter a number of task:"))
        except ValueError:
            print("Enter a number.")
            continue
        final_number = task_number - 1
        if task_number <= 0 or final_number > len(tasks) - 1:
            print("Enter a positive number or number of exist task.")
            continue
        return final_number

while True:
    tasks = load_task()
    user_choose = ask_user()

    if user_choose == "1":
        add_task(tasks)
        save_task(tasks)
    elif user_choose == "2":
        show_tasks(tasks)
    elif user_choose == "3":
        print("Bye!")
        break
    elif user_choose == "4":
        complete_task(tasks)
    elif user_choose == "5":
        delete_task(tasks)
    elif user_choose == "6":
        uncomplete_task(tasks)
    elif user_choose == "7":
        edit_task(tasks)
    elif user_choose == "8":
        search_task(tasks)








