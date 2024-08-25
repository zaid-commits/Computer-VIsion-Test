from flask import Flask, render_template, request, redirect, url_for
import os
import subprocess

app = Flask(__name__)

# Path to your projects directory
PROJECTS_DIR = r'C:\Users\coeng\OneDrive\Desktop\co-final\projects'

@app.route('/')
def index():
    # List all directories in the projects directory
    projects = [d for d in os.listdir(PROJECTS_DIR) if os.path.isdir(os.path.join(PROJECTS_DIR, d))]
    return render_template('index.html', projects=projects)

@app.route('/run/<project_name>')
def run_project(project_name):
    project_path = os.path.join(PROJECTS_DIR, project_name, 'main.py')
    
    if os.path.exists(project_path):
        # Run the project using subprocess
        subprocess.Popen(['python', project_path], cwd=os.path.join(PROJECTS_DIR, project_name))
        return f'Running {project_name}...'
    else:
        return f'Project {project_name} does not exist or is not executable.'

if __name__ == '__main__':
    app.run(debug=True)
