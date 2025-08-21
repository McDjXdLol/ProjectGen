from gui import CustomTkinterApp


def main() -> None:
    """Main function to run the CustomTkinter application."""
    app = CustomTkinterApp()
    app.mainloop()


if __name__ == "__main__":
    main()
else:
    print("This script is intended to be run as a standalone program.")
