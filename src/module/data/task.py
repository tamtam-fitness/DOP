def create_task_data(id, title, description, status, priority, due_date, user_id):
    return {
        "id": id,
        "title": title,
        "description": description,
        "status": status,
        "priority": priority,
        "due_date": due_date,
        "user_id": user_id
    }

