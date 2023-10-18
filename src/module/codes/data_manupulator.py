class NameCalculation:
    @staticmethod
    def full_name(data):
        return f"{data['first_name']} {data['last_name']}"


class TaskManipulation:

    @staticmethod
    def add_task(tasks, task):
        return tasks + [task]

    @staticmethod
    def remove_task(tasks, task_id):
        return [task for task in tasks if task['id'] != task_id]

    @staticmethod
    def update_task(tasks, task):
        return [task if t['id'] == task['id'] else t for t in tasks]

    @staticmethod
    def search_task(tasks, key, value):
        return [task for task in tasks if task[key] == value]

    @staticmethod
    def find_task(tasks, task_id):
        for task in tasks:
            if task['id'] == task_id:
                return task

