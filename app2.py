from flask import Flask,request
from models.task import Task

app = Flask(__name__)

tasks = []

task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json
    print(data)

if __name__ == "__main__":
    app.run(debug=True)