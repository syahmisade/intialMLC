import tkinter as tk
from tkinter import ttk, messagebox
from task_manager_logic import TaskManagerLogic
from task_view import TaskView

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Management System")
        self.root.geometry("800x600")

        # Create the logic handler
        self.logic = TaskManagerLogic()

        # Create the notebook (tab container)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both")

        # Create task viewer tab
        self.task_view = TaskView(self.notebook, self.logic)

        # Initialize the Insert Task tab
        self.init_insert_tab()

    def init_insert_tab(self):
        """Initializes the task and subtask insertion form tab."""
        tab2 = ttk.Frame(self.notebook)
        self.notebook.add(tab2, text="Insert Task")

        # Task Form for inserting new tasks
        form_frame = tk.Frame(tab2)
        form_frame.pack(pady=20)

        tk.Label(form_frame, text="Task Name").grid(row=0, column=0, padx=10, pady=5)
        self.entry_task_name = tk.Entry(form_frame)
        self.entry_task_name.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Category").grid(row=1, column=0, padx=10, pady=5)
        self.entry_category = tk.Entry(form_frame)
        self.entry_category.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Priority").grid(row=2, column=0, padx=10, pady=5)
        self.entry_priority = tk.Entry(form_frame)
        self.entry_priority.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Start Date").grid(row=3, column=0, padx=10, pady=5)
        self.entry_start_date = tk.Entry(form_frame)
        self.entry_start_date.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Due Date").grid(row=4, column=0, padx=10, pady=5)
        self.entry_due_date = tk.Entry(form_frame)
        self.entry_due_date.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Status").grid(row=5, column=0, padx=10, pady=5)
        self.entry_status = tk.Entry(form_frame)
        self.entry_status.grid(row=5, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Progress").grid(row=6, column=0, padx=10, pady=5)
        self.entry_progress = tk.Entry(form_frame)
        self.entry_progress.grid(row=6, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Notes").grid(row=7, column=0, padx=10, pady=5)
        self.entry_notes = tk.Entry(form_frame)
        self.entry_notes.grid(row=7, column=1, padx=10, pady=5)

        # Button to add task
        add_task_button = tk.Button(form_frame, text="Add Task", command=self.add_task)
        add_task_button.grid(row=8, columnspan=2, pady=10)

        # Subtask Form for inserting new subtasks
        subtask_frame = tk.Frame(tab2)
        subtask_frame.pack(pady=20)

        tk.Label(subtask_frame, text="Task ID").grid(row=0, column=0, padx=10, pady=5)
        self.entry_subtask_task_id = tk.Entry(subtask_frame)
        self.entry_subtask_task_id.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(subtask_frame, text="Subtask Name").grid(row=1, column=0, padx=10, pady=5)
        self.entry_subtask_name = tk.Entry(subtask_frame)
        self.entry_subtask_name.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(subtask_frame, text="Subtask Status").grid(row=2, column=0, padx=10, pady=5)
        self.entry_subtask_status = tk.Entry(subtask_frame)
        self.entry_subtask_status.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(subtask_frame, text="Subtask Progress").grid(row=3, column=0, padx=10, pady=5)
        self.entry_subtask_progress = tk.Entry(subtask_frame)
        self.entry_subtask_progress.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(subtask_frame, text="Subtask Due Date").grid(row=4, column=0, padx=10, pady=5)
        self.entry_subtask_due_date = tk.Entry(subtask_frame)
        self.entry_subtask_due_date.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(subtask_frame, text="Subtask Completed Date").grid(row=5, column=0, padx=10, pady=5)
        self.entry_subtask_completed_date = tk.Entry(subtask_frame)
        self.entry_subtask_completed_date.grid(row=5, column=1, padx=10, pady=5)

        # Button to add subtask
        add_subtask_button = tk.Button(subtask_frame, text="Add Subtask", command=self.add_subtask)
        add_subtask_button.grid(row=6, columnspan=2, pady=10)

    def add_task(self):
        """Adds a new task to the task table."""
        task_data = {
            "task_name": self.entry_task_name.get(),
            "category": self.entry_category.get(),
            "priority": self.entry_priority.get(),
            "start_date": self.entry_start_date.get(),
            "due_date": self.entry_due_date.get(),
            "status": self.entry_status.get(),
            "progress": self.entry_progress.get(),
            "notes": self.entry_notes.get()
        }

        # Add the task using TaskManagerLogic
        self.logic.add_task(task_data)
        self.task_view.refresh_task_table()
        messagebox.showinfo("Success", "Task added successfully.")  # Show success message after adding task

    def add_subtask(self):
        """Adds a new subtask to the subtask list."""
        subtask_data = {
            "task_id": int(self.entry_subtask_task_id.get()),
            "subtask_name": self.entry_subtask_name.get(),
            "subtask_status": self.entry_subtask_status.get(),
            "subtask_progress": self.entry_subtask_progress.get(),
            "subtask_due_date": self.entry_subtask_due_date.get(),
            "subtask_completed_date": self.entry_subtask_completed_date.get()
        }

        # Validate Task ID to ensure the subtask is linked to an existing task
        task_exists = any(task[0] == subtask_data['task_id'] for task in self.logic.main_tasks)
        if not task_exists:
            messagebox.showwarning("Error", "Task ID does not exist.")
            return

        # Add the subtask using TaskManagerLogic
        self.logic.add_subtask(subtask_data)
        self.task_view.refresh_task_table()  # Refresh the task view to display new subtask
        messagebox.showinfo("Success", "Subtask added successfully.")
