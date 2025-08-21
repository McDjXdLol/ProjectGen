import json
import os
import subprocess


class FileStructureOperator:
    def __init__(self, project_name, project_language):
        self.CONFIG_FILE = 'config.json'
        self.project_name = project_name
        self.project_language = project_language

    @staticmethod
    def run_command(command: str) -> str:
        """Run a shell command and return its output."""
        try:
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Error running command '{command}': {e}")
            return None

    @staticmethod
    def create_directory(path: str) -> None:
        """Create a directory if it does not exist."""
        try:
            os.makedirs(path, exist_ok=True)
            print(f"Directory created: {path}")
        except Exception as e:
            print(f"Error creating directory '{path}': {e}")

    @staticmethod
    def create_file(path: str, content: str) -> None:
        """Create a file with the specified content."""
        try:
            with open(path, 'w') as file:
                file.write(content)
            print(f"File created: {path}")
        except Exception as e:
            print(f"Error creating file '{path}': {e}")

    def read_config(self) -> dict:
        """Read configuration from a JSON file."""
        if not os.path.exists(self.CONFIG_FILE):
            print(f"Configuration file '{self.CONFIG_FILE}' not found.")
            return None
        try:
            with open(self.CONFIG_FILE, 'r') as file:
                config = json.load(file)
                print("Configuration loaded successfully.")
                return config
        except json.JSONDecodeError as e:
            print(f"Error reading configuration file '{self.CONFIG_FILE}': {e}")
            return None
        except Exception as e:
            print(f"Unexpected error reading configuration file '{self.CONFIG_FILE}': {e}")
            return None

    def select_language(self) -> dict:
        """Select a language and return its configuration."""
        language = self.project_language
        if not language:
            print("No language specified.")
            return None
        config = self.read_config()['projects']
        if not config or language not in config:
            print(f"Language '{language}' not found in configuration.")
            return None
        return config[language]

    def open_editor(self, editor: str, path: str) -> None:
        editors = self.read_config().get('editors')
        if not editors:
            print("No editors configured.")
            return None
        if editor not in editors:
            print(f"Editor '{editor}' not found in configuration.")
            return None
        command = editors[editor]['command']
        if not command:
            print(f"No command configured for editor '{editor}'.")
            return None
        print(f"Opening editor '{editor}' with command: {command}")
        return subprocess.run([command, path], check=True, shell=True)

    def init_git(self, path: str) -> None:
        """Initialize a Git repository in the specified path."""
        if not os.path.exists(path):
            print(f"Path '{path}' does not exist.")
            return None
        command = ["git", "-C", str(path), "init"]
        print(f"Initializing Git repository at {path} with command: {' '.join(command)}")
        return self.run_command(command)

    def create_project_structure(self) -> None:
        """Create a project structure based on the selected language."""
        language = self.project_language
        project_name = self.project_name

        if not language or not project_name:
            print("Language or project name not specified.")
            return None
        config = self.select_language()
        if not config:
            print(f"No configuration found for language '{language}'.")
            return None
        editor = config['editor']
        structure = config['structure']
        projects_path = self.read_config().get('default_projects_path', os.getcwd())
        project_path = os.path.join(projects_path, project_name)
        if not projects_path:
            print("No projects path specified in configuration.")
            return None
        self.create_directory(project_path)

        for file in structure:
            file_path = os.path.join(project_path, file)
            self.create_file(file_path, '# ' + project_name)

        self.init_git(project_path)
        self.open_editor(editor, project_path)
        return None
