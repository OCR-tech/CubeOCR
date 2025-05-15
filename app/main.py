# Import necessary modules
import src.module.py_window_main as py_window_main


def main():
    """
    Main function to launch the GUI application.
    """
    # This function is the entry point of the application.
    py_window_main.setup_system()  # Check the system environment for compatibility
    py_window_main.launch_gui()  # Launch the GUI by invoking the `launch_gui` function from the `py_main_gui` module.


if __name__ == '__main__':
    main()  # Call the main function to start the application
