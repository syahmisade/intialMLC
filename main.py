from task_manager_app import TaskManagerApp  # Import the TaskManagerApp class for handling the main application
import tkinter as tk  # Import tkinter for creating the GUI

if __name__ == "__main__":
    """
    This is the entry point of the application. When this script is run, 
    it initializes the Tkinter window and starts the task management app.
    """
    
    # Create the root Tkinter window
    root = tk.Tk()

    # Create an instance of TaskManagerApp, passing the root window as a parameter
    # This will initialize the app and setup the GUI.
    app = TaskManagerApp(root)

    # Start the Tkinter main event loop, which listens for user interactions and keeps the window open
    root.mainloop()
