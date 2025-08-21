import sys, os

import customtkinter as ctk
from tkinter import PhotoImage
from filegen import FileStructureOperator


def get_languages() -> list:
    """Get the list of available programming languages from the config file."""
    config = FileStructureOperator('', '').read_config()
    if not config or 'projects' not in config:
        print("No languages configured.")
        return []
    return list(config['projects'].keys())

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and PyInstaller"""
    try:
        # PyInstaller tworzy folder tymczasowy _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class CustomTkinterApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green")
        self.title("Project Generator")
        self.geometry("400x300")
        self.available_languages = get_languages()
        self.project_name = ctk.StringVar()
        self.project_language = ctk.StringVar()

        if sys.platform.startswith("win"):
            self.iconbitmap(resource_path("icon.ico"))
        else:
            icon = PhotoImage(file=resource_path("icon.png"))
            self.iconphoto(True, icon)

        self.create_widgets()

    def create_widgets(self) -> None:
        ctk.CTkLabel(self, text="Project Name:").pack(pady=10)
        ctk.CTkEntry(self, textvariable=self.project_name).pack(pady=5)

        ctk.CTkLabel(self, text="Project Language:").pack(pady=10)
        ctk.CTkOptionMenu(self, variable=self.project_language, values=self.available_languages).pack(pady=5)

        ctk.CTkButton(self, text="Create Project", command=self.create_project).pack(pady=20)

    def create_project(self) -> None:
        project_name = self.project_name.get()
        project_language = self.project_language.get()
        if not project_name or not project_language:
            print("Please enter both project name and language.")
            return
        file_operator = FileStructureOperator(project_name, project_language)
        file_operator.create_project_structure()
        sys.exit(1)
