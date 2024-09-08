import tkinter as tk  # Import tkinter for creating the GUI
from tkinter import ttk  # Import ttk for advanced widgets like Treeview

class TaskView:
    def __init__(self, notebook, logic):
        """
        Initialize the TaskView class.
        This class manages the display of tasks and subtasks in the Task Viewer tab.
        :param notebook: The parent ttk.Notebook where the tabs will be added.
        :param logic: An instance of TaskManagerLogic to access the task and subtask data.
        """
        self.logic = logic  # Reference to the business logic that holds tasks and subtasks

        # Create Task Viewer Tab
        tab1 = ttk.Frame(notebook)  # Create a new tab
        notebook.add(tab1, text="Task Viewer")  # Add the tab to the notebook

        # Main Task Table (Treeview) to display tasks
        self.main_task_frame = tk.Frame(tab1)  # Create a frame to hold the task table
        self.main_task_frame.pack(pady=10)  # Add some padding for better spacing

        # Label for the Main Task Table
        main_task_label = tk.Label(self.main_task_frame, text="Main Task Table", font=("Arial", 12, "bold"))
        main_task_label.pack()

        # Define columns for the Main Task Table (Treeview)
        main_task_columns = ("Task ID", "Task Name", "Category", "Priority", "Start Date", "Due Date", "Status", "Progress", "Notes")
        self.main_task_table = ttk.Treeview(self.main_task_frame, columns=main_task_columns, show="headings")

        # Set column headings and widths
        for col in main_task_columns:
            self.main_task_table.heading(col, text=col)  # Set heading for each column
            self.main_task_table.column(col, width=100)  # Set column width

        self.main_task_table.pack()  # Pack the Treeview into the frame

        # Load tasks into the Main Task Table
        self.refresh_task_table()

        # Subtask Table (Treeview) to display subtasks
        subtask_frame = tk.Frame(tab1)  # Create a frame for the subtask table
        subtask_frame.pack(pady=10)  # Add padding for layout

        # Label for the Subtask Table
        subtask_label = tk.Label(subtask_frame, text="Subtask Table", font=("Arial", 12, "bold"))
        subtask_label.pack()

        # Define columns for the Subtask Table (Treeview)
        subtask_columns = ("Subtask ID", "Task ID", "Subtask Name", "Subtask Status", "Subtask Progress", "Subtask Due Date", "Subtask Completed Date")
        self.subtask_table = ttk.Treeview(subtask_frame, columns=subtask_columns, show="headings")

        # Set column headings and widths for the subtask table
        for col in subtask_columns:
            self.subtask_table.heading(col, text=col)  # Set heading for each column
            self.subtask_table.column(col, width=100)  # Set column width

        self.subtask_table.pack()  # Pack the Treeview into the frame

        # Bind selection in the main task table to load subtasks
        self.main_task_table.bind("<<TreeviewSelect>>", self.on_task_select)

    def refresh_task_table(self):
        """
        Refreshes the task table and reloads subtasks if a task is selected.
        This method clears the table and reloads all tasks from the logic.
        """
        # Clear the main task table
        for item in self.main_task_table.get_children():
            self.main_task_table.delete(item)

        # Reload all tasks from the logic
        for task in self.logic.tasks:
            self.main_task_table.insert("", "end", values=task.as_list())  # Insert task data into the table

        # Check if a task is currently selected and load its subtasks
        selected_item = self.main_task_table.focus()  # Get currently selected task (if any)
        if selected_item:
            task_id = self.main_task_table.item(selected_item)['values'][0]  # Get the task ID of the selected task
            self.load_subtasks(task_id)  # Load the subtasks for the selected task

    def on_task_select(self, event):
        """
        Loads subtasks when a task is selected in the main task table.
        This method is triggered when the user selects a task in the Treeview.
        :param event: The event object that holds the event information.
        """
        selected_item = self.main_task_table.focus()  # Get the selected item in the task table
        if selected_item:
            task_id = self.main_task_table.item(selected_item)['values'][0]  # Get the task ID of the selected task
            self.load_subtasks(task_id)  # Load the corresponding subtasks for this task

    def load_subtasks(self, task_id):
        """
        Loads subtasks related to the selected task into the subtask table.
        This method clears the current subtask table and reloads the subtasks for the selected task.
        :param task_id: The ID of the task whose subtasks are to be loaded.
        """
        # Clear the subtask table before loading new data
        for item in self.subtask_table.get_children():
            self.subtask_table.delete(item)

        # Load subtasks that are associated with the selected task ID
        for subtask in self.logic.subtasks:
            if subtask.task_id == task_id:  # Check if the subtask belongs to the selected task
                self.subtask_table.insert("", "end", values=subtask.as_list())  # Insert subtask data into the table
