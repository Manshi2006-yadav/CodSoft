from assets.file_handler import load_tasks, save_tasks


def add_task(task_name):

    tasks = load_tasks()

    tasks.append({
        "task": task_name,
        "completed": False
    })

    save_tasks(tasks)


def view_tasks():
    return load_tasks()


def mark_completed(task_number):

    tasks = load_tasks()

    if 0 <= task_number < len(tasks):
        tasks[task_number]["completed"] = True
        save_tasks(tasks)
        return True

    return False


def delete_task(task_number):

    tasks = load_tasks()

    if 0 <= task_number < len(tasks):
        tasks.pop(task_number)
        save_tasks(tasks)
        return True

    return False