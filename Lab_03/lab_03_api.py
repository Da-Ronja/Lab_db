from flask import Flask, app, jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'Task 1',
        'description': 'This is task 1'
    },
    {
        'id': 2,
        'title': 'Task 2',
        'description': 'This is task 2'
    },
    {
        'id': 3,
        'title': 'Task 3',
        'description': 'This is task 3'
    }
]
next_id = 4

# Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    if len(tasks) == 0:
        return 'No tasks available', 404

    return jsonify({'tasks': tasks}), 200

# Post a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    global next_id
    task_data = request.get_json()

    if 'title' not in task_data or 'description' not in task_data:
        return 'Missing data', 400
    
    task = {
        'id': next_id,
        'title': task_data['title'],
        'description': task_data['description']
    }

    tasks.append(task)
    next_id += 1

    return jsonify(task), 201

# Delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks

    task = next((task for task in tasks if task['id'] == task_id), None)
    
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    
    tasks.remove(task)

    return jsonify({'message': f'Task {task_id} deleted'}), 200
    
if __name__ == '__main__':
    app.run(debug=True)