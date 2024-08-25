# Computer Vision Projects Web App

Welcome to the **Computer Vision Projects Web App**! This web application provides an easy way to list and run your Python-based computer vision projects directly from your browser.

## Features

- **Project Listing**: Automatically lists all your computer vision projects in a specified directory.
- **One-Click Execution**: Run any project with a single click directly from the web interface.
- **Dynamic Loading**: The app dynamically loads projects from the specified directory, so you can easily add or remove projects.
- **Subprocess Execution**: Runs your Python scripts in the background, allowing you to interact with multiple projects simultaneously.

## Directory Structure

Ensure your projects are organized in the following structure:

```
/path/to/computer_vision_projects/
│
├── project1/
│   ├── main.py
│   └── other_files...
├── project2/
│   ├── main.py
│   └── other_files...
└── project3/
    ├── main.py
    └── other_files...
```

Replace `/path/to/computer_vision_projects/` with the actual path to your projects directory, for example, `C:\Users\coeng\OneDrive\Desktop\webapp\projects`.

## Setup

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/computer-vision-projects-webapp.git
cd computer-vision-projects-webapp
```

### 2. Set Up the Python Environment

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install the required Python packages:

```bash
pip install Flask
```

### 3. Configure the Projects Directory

Edit the `app.py` file and update the `PROJECTS_DIR` variable with the path to your projects directory:

```python
PROJECTS_DIR = r'C:\Users\coeng\OneDrive\Desktop\webapp\projects'
```

### 4. Run the Application

Start the Flask web server:

```bash
python app.py
```

Open your web browser and navigate to `http://127.0.0.1:5000/`. You should see a list of your projects.

## Usage

- **Browse Projects**: On the home page, you'll see a list of all the available computer vision projects.
- **Run a Project**: Click on a project name to execute its `main.py` script.
- **Stop the Application**: To stop the Flask server, simply press `CTRL + C` in the terminal.

## Customization

You can customize the web app further by:

- **Adding Project Descriptions**: Modify the HTML template to include descriptions or images for each project.
- **Logging Output**: Capture the output of each project and display it on the web page.
- **Input Forms**: Add forms to the web interface to allow users to pass parameters to the projects.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to the developers and communities behind Flask and Python for providing the tools and libraries that make projects like this possible.

