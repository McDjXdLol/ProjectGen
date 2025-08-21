# Project Generator

This is a simple project generator application written in Python using `CustomTkinter` for the graphical user interface.
It allows you to quickly create a new project with a predefined file structure for various programming languages and
automatically open it in your preferred code editor.

## Features

- **Quick Project Creation:** Create a new project directory with a single click.

- **Configurable Languages:** The application reads project templates from a `config.json` file. You can easily add,
  remove, or modify languages and their file structures.

- **Configurable Editors:** Customize the list of code editors and their respective commands to suit your development
  environment.

- **Automatic Git Initialization:** The application can automatically initialize a Git repository in the new project
  directory.

- **Cross-Platform Compatibility:** Designed to work on different operating systems (Windows, macOS, Linux).

## Getting Started

### Prerequisites

- Python 3.x

- Git (optional, but recommended for repository initialization)

- The required Python libraries.

### Installation

1. Clone this repository or download the project files.

2. Install the required Python libraries using pip:

   ```bash
   pip install customtkinter
   ```

### Usage

1. Run the main application file:

   ```bash
   python main.py
   ```

2. In the application window, enter your desired project name.

3. Select the programming language for your project from the dropdown menu.

4. Click the **"Create Project"** button.

The application will create the project directory with the specified file structure and open it in the configured
editor.

## Configuration

The application's behavior is controlled by the `config.json` file. You can customize it to fit your needs.

### `default_projects_path`

This key specifies the default directory where all new projects will be created. You can change this to any path you
prefer.

- **Example:** `"default_projects_path": "C:/Users/YourUser/Documents/Projects"`

### `editors`

This section defines the code editors the application can use.

- Each key is a name for the editor (e.g., `"code"`, `"pycharm"`).

- The `name` value is a friendly name displayed in the application.

- The `command` value is the shell command used to open the editor.

- **Example:**

  ```json
  "code": {
    "name": "Visual Studio Code",
    "command": "code"
  },
  "pycharm": {
    "name": "PyCharm",
    "command": "pycharm"
  }
  ```

### `projects`

This section defines the available project templates for different programming languages.

- Each key is the name of a language (e.g., `"Python"`, `"HTML"`).

- The `editor` value is the key from the `editors` section that specifies which editor to use for this language.

- The `structure` is an array of strings representing the files and directories to be created in the new project.

- **Example:**

  ```json
  "Python": {
    "editor": "pycharm",
    "structure": [
      "README.md",
      "requirements.txt",
      "main.py"
    ]
  },
  "HTML": {
    "editor": "atom",
    "structure": [
      "index.html",
      "style.css",
      "script.js"
    ]
  }
  ```

You can add your own custom project structures here, like `"React"` or `"Java"`, and the application will automatically
pick them up.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.