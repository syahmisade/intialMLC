import tkinter as tk
from tkinter import ttk


class TaskView:
    def __init__(self, notebook, logic):
        self.logic = logic

        # Create Task Viewer Tab
        tab1 = ttk.Frame(notebook)
        notebook.add(tab1, text="Task Viewer")

        # Main Task Table (Treeview)
        self.main_task_frame = tk.Frame(tab1)
        self.main_task_frame.pack(pady=10)

        main_task_label = tk.Label(self.main_task_frame, text="Main Task Table", font=("Arial", 12, "bold"))
        main_task_label.pack()

        # Define columns for the Main Task Table
        main_task_columns = ("Task ID", "Task Name", "Category", "Priority", "Start Date", "Due Date", "Status", "Progress", "Notes")
        self.main_task_table = ttk.Treeview(self.main_task_frame, columns=main_task_columns, show="headings")

        # Define column headings and set column widths
        for col in main_task_columns:
            self.main_task_table.heading(col, text=col)
            self.main_task_table.column(col, width=100)

        self.main_task_table.pack()

        # Insert sample data into the Main Task Table
        self.refresh_task_table()

        # Subtask Table (Treeview)
        subtask_frame = tk.Frame(tab1)
        subtask_frame.pack(pady=10)

        subtask_label = tk.Label(subtask_frame, text="Subtask Table", font=("Arial", 12, "bold"))
        subtask_label.pack()

        # Define columns for the Subtask Table
        subtask_columns = ("Subtask ID", "Task ID", "Subtask Name", "Subtask Status", "Subtask Progress", "Subtask Due Date", "Subtask Completed Date")
        self.subtask_table = ttk.Treeview(subtask_frame, columns=subtask_columns, show="headings")

        # Define column headings and set column widths
        for col in subtask_columns:
            self.subtask_table.heading(col, text=col)
            self.subtask_table.column(col, width=100)

        self.subtask_table.pack()

        # Bind task selection to loading subtasks
        self.main_task_table.bind("<<TreeviewSelect>>", self.on_task_select)

    def refresh_task_table(self):
        """Refreshes the task table and reloads subtasks if a task is selected."""
        # Clear the main task table
        for item in self.main_task_table.get_children():
            self.main_task_table.delete(item)

        # Reload all tasks
        for task in self.logic.main_tasks:
            self.main_task_table.insert("", "end", values=task)

        # Reload subtasks for the selected task (if any)
        selected_item = self.main_task_table.focus()
        if selected_item:
            task_id = self.main_task_table.item(selected_item)['values'][0]
            self.load_subtasks(task_id)

    def on_task_select(self, event):
        """Loads subtasks when a task is selected."""
        selected_item = self.main_task_table.focus()
        if selected_item:
            task_id = self.main_task_table.item(selected_item)['values'][0]
            self.load_subtasks(task_id)

    def load_subtasks(self, task_id):
        """Loads subtasks related to the selected task."""
        for item in self.subtask_table.get_children():
            self.subtask_table.delete(item)

        for subtask in self.logic.subtasks:
            if subtask[1] == task_id:
                self.subtask_table.insert("", "end", values=subtask)
