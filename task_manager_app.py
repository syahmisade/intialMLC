import tkinter as tk  # Import tkinter for creating the GUI
from tkinter import ttk, messagebox  # Import ttk for advanced widgets and messagebox for alerts
from task_manager_logic import TaskManagerLogic  # Import business logic for managing tasks and subtasks
from task_view import TaskView  # Import the task view to display tasks and subtasks

class TaskManagerApp:
    def __init__(self, root):
        """
        Initialize the TaskManagerApp class.
        This sets up the main GUI window, logic handler, and the notebook (tab container).
        """
        self.root = root
        self.root.title("Task Management System")  # Set window title
        self.root.geometry("800x600")  # Set default window size

        # Create the logic handler to manage tasks and subtasks
        self.logic = TaskManagerLogic()

        # Create the notebook (tab container) for organizing the tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both")  # Make the notebook fill the window

        # Create task viewer tab (displays tasks and subtasks)
        self.task_view = TaskView(self.notebook, self.logic)

        # Initialize the Insert Task tab (for adding tasks and subtasks)
        self.init_insert_tab()

    def init_insert_tab(self):
        """
        Initializes the task and subtask insertion form tab.
        This method sets up the form inputs for adding tasks and subtasks.
        """
        tab2 = ttk.Frame(self.notebook)  # Create a new tab in the notebook
        self.notebook.add(tab2, text="Insert Task")  # Add the tab to the notebook with a label

        # Task Form for inserting new tasks
        form_frame = tk.Frame(tab2)  # Frame for holding task input fields
        form_frame.pack(pady=20)  # Add padding for better layout

        # Create label and input for Task Name
        tk.Label(form_frame, text="Task Name").grid(row=0, column=0, padx=10, pady=5)
        self.entry_task_name = tk.Entry(form_frame)
        self.entry_task_name.grid(row=0, column=1, padx=10, pady=5)

        # Create label and input for Category
        tk.Label(form_frame, text="Category").grid(row=1, column=0, padx=10, pady=5)
        self.entry_category = tk.Entry(form_frame)
        self.entry_category.grid(row=1, column=1, padx=10, pady=5)

        # Create label and input for Priority
        tk.Label(form_frame, text="Priority").grid(row=2, column=0, padx=10, pady=5)
        self.entry_priority = tk.Entry(form_frame)
        self.entry_priority.grid(row=2, column=1, padx=10, pady=5)

        # Create label and input for Start Date
        tk.Label(form_frame, text="Start Date").grid(row=3, column=0, padx=10, pady=5)
        self.entry_start_date = tk.Entry(form_frame)
        self.entry_start_date.grid(row=3, column=1, padx=10, pady=5)

        # Create label and input for Due Date
        tk.Label(form_frame, text="Due Date").grid(row=4, column=0, padx=10, pady=5)
        self.entry_due_date = tk.Entry(form_frame)
        self.entry_due_date.grid(row=4, column=1, padx=10, pady=5)

        # Create label and input for Status
        tk.Label(form_frame, text="Status").grid(row=5, column=0, padx=10, pady=5)
        self.entry_status = tk.Entry(form_frame)
        self.entry_status.grid(row=5, column=1, padx=10, pady=5)

        # Create label and input for Progress
        tk.Label(form_frame, text="Progress").grid(row=6, column=0, padx=10, pady=5)
        self.entry_progress = tk.Entry(form_frame)
        self.entry_progress.grid(row=6, column=1, padx=10, pady=5)

        # Create label and input for Notes
        tk.Label(form_frame, text="Notes").grid(row=7, column=0, padx=10, pady=5)
        self.entry_notes = tk.Entry(form_frame)
        self.entry_notes.grid(row=7, column=1, padx=10, pady=5)

        # Button to add task
        add_task_button = tk.Button(form_frame, text="Add Task", command=self.add_task)
        add_task_button.grid(row=8, columnspan=2, pady=10)  # Add the task when clicked

        # Subtask Form for inserting new subtasks
        subtask_frame = tk.Frame(tab2)  # Frame for holding subtask input fields
        subtask_frame.pack(pady=20)

        # Create label and input for Task ID (the ID of the task to which the subtask belongs)
        tk.Label(subtask_frame, text="Task ID").grid(row=0, column=0, padx=10, pady=5)
        self.entry_subtask_task_id = tk.Entry(subtask_frame)
        self.entry_subtask_task_id.grid(row=0, column=1, padx=10, pady=5)

        # Create label and input for Subtask Name
        tk.Label(subtask_frame, text="Subtask Name").grid(row=1, column=0, padx=10, pady=5)
        self.entry_subtask_name = tk.Entry(subtask_frame)
        self.entry_subtask_name.grid(row=1, column=1, padx=10, pady=5)

        # Create label and input for Subtask Status
        tk.Label(subtask_frame, text="Subtask Status").grid(row=2, column=0, padx=10, pady=5)
        self.entry_subtask_status = tk.Entry(subtask_frame)
        self.entry_subtask_status.grid(row=2, column=1, padx=10, pady=5)

        # Create label and input for Subtask Progress
        tk.Label(subtask_frame, text="Subtask Progress").grid(row=3, column=0, padx=10, pady=5)
        self.entry_subtask_progress = tk.Entry(subtask_frame)
        self.entry_subtask_progress.grid(row=3, column=1, padx=10, pady=5)

        # Create label and input for Subtask Due Date
        tk.Label(subtask_frame, text="Subtask Due Date").grid(row=4, column=0, padx=10, pady=5)
        self.entry_subtask_due_date = tk.Entry(subtask_frame)
        self.entry_subtask_due_date.grid(row=4, column=1, padx=10, pady=5)

        # Create label and input for Subtask Completed Date
        tk.Label(subtask_frame, text="Subtask Completed Date").grid(row=5, column=0, padx=10, pady=5)
        self.entry_subtask_completed_date = tk.Entry(subtask_frame)
        self.entry_subtask_completed_date.grid(row=5, column=1, padx=10, pady=5)

        # Button to add subtask
        add_subtask_button = tk.Button(subtask_frame, text="Add Subtask", command=self.add_subtask)
        add_subtask_button.grid(row=6, columnspan=2, pady=10)  # Add the subtask when clicked

    def add_task(self):
        """Adds a new task to the task list by collecting form data and passing it to the logic."""
        # Collect data from the form input fields
        task_data = {
            "name": self.entry_task_name.get(),
            "category": self.entry_category.get(),
            "priority": self.entry_priority.get(),
            "start_date": self.entry_start_date.get(),
            "due_date": self.entry_due_date.get(),
            "status": self.entry_status.get(),
            "progress": self.entry_progress.get(),
            "notes": self.entry_notes.get()
        }

        # Validate that required fields (name, category, start date, due date) are filled
        if not task_data["name"] or not task_data["category"] or not task_data["start_date"] or not task_data["due_date"]:
            messagebox.showwarning("Input Error", "Please fill out all required fields.")
            return

        # Add the task using TaskManagerLogic and refresh the task view
        self.logic.add_task(task_data)
        self.task_view.refresh_task_table()  # Update the task table with the new task
        messagebox.showinfo("Success", "Task added successfully.")  # Show success message

    def add_subtask(self):
        """Adds a new subtask to the subtask list by collecting form data and passing it to the logic."""
        # Collect data from the subtask form input fields
        subtask_data = {
            "task_id": int(self.entry_subtask_task_id.get()),  # The ID of the task to which the subtask belongs
            "name": self.entry_subtask_name.get(),
            "status": self.entry_subtask_status.get(),
            "progress": self.entry_subtask_progress.get(),
            "due_date": self.entry_subtask_due_date.get(),
            "completed_date": self.entry_subtask_completed_date.get()
        }

        # Validate that required fields (task ID, name, status) are filled
        if not subtask_data["task_id"] or not subtask_data["name"] or not subtask_data["status"]:
            messagebox.showwarning("Input Error", "Please fill out all required fields.")
            return

        # Validate if the Task ID exists by checking the list of tasks
        if not any(task.task_id == subtask_data["task_id"] for task in self.logic.tasks):
            messagebox.showwarning("Error", "Task ID does not exist.")
            return

        # Add the subtask using TaskManagerLogic
        self.logic.add_subtask(subtask_data)

        # Refresh the task view to reflect the new subtask in the task table
        self.task_view.refresh_task_table()

        # Display success message
        messagebox.showinfo("Success", "Subtask added successfully.")

