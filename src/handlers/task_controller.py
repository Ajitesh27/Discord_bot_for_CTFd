from databases import task_database

def create_task(name, category, description, files, flag):
    
    if task_database.task_exist(name):
        return 'Task already exist'

    if task_database.not_unique_flag(flag):
        return 'Flag must be unique'

    task = task_database.create_task(name, category, description, files, flag)
    return f'Task with `id {task.id}` succesfully created'

def release_task(task_id):
    
    if task_database.find_task(task_id) == None:
        return f'Task with `id {task_id}` didnt exist'
    
    task_database.release_task(task_id)
    return f'Task with `id {task_id}` succesfully released'

def hide_task(task_id):
    
    if task_database.find_task(task_id) == None:
        return f'Task with `id {task_id}` didnt exist'
    
    task_database.hide_task(task_id)
    return f'Task succesfully hidden'

def delete_task(task_id):
    if task_database.find_task(task_id) == None:
        return f'Task with `id {task_id}` didnt exist'
    
    task_database.delete_task(task_id)
    return f'Task succesfully deleted'
    
