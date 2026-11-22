from flask import Flask, request, redirect
app = Flask(__name__)
tasks = []
@app.get('/')
def index():
    items = ''.join(f'<li>{t}</li>' for t in tasks)
    return f'<h1>To-Do List</h1><form method="post" action="/add"><input name="task" required><button>Add</button></form><ul>{items}</ul>'
@app.post('/add')
def add():
    task = request.form.get('task','').strip()
    if task: tasks.append(task)
    return redirect('/')
@app.get('/health')
def health(): return {'status':'healthy'}
if __name__ == '__main__': app.run(host='0.0.0.0', port=5000)
