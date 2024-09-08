from excel_handler import ExcelHandler  # Import the class responsible for handling Excel file operations
from task_model import Task, Subtask  # Import the Task and Subtask models
import threading  # Import threading for background saving operations

class TaskManagerLogic:
    def __init__(self):
        """
        Initialize the TaskManagerLogic class.
        This class manages the tasks and subtasks in memory and interacts with the ExcelHandler for data persistence.
        """
        self.excel_handler = ExcelHandler()  # Create an instance of ExcelHandler to manage Excel file I/O
        self.tasks = []  # List to hold all tasks
        self.subtasks = []  # List to hold all subtasks
        self.load_data()  # Load existing tasks and subtasks from the Excel file

    def load_data(self):
        """
        Load tasks and subtasks from the Excel file using ExcelHandler.
        This method initializes the task and subtask lists with data from the file.
        """
        self.tasks, self.subtasks = self.excel_handler.load_data()  # Load data from the Excel file

    def save_data(self):
        """
        Save tasks and subtasks to the Excel file using ExcelHandler.
        This method runs in a separate thread to avoid blocking the UI.
        """
        save_thread = threading.Thread(target=self.excel_handler.save_data, args=(self.tasks, self.subtasks))
        save_thread.start()  # Start the saving process in the background

    def get_new_task_id(self):
        """
        Generate a new unique Task ID.
        This method checks the highest Task ID in the current list of tasks and returns a new unique ID.
        """
        return max((task.task_id for task in self.tasks), default=0) + 1  # Generate the next Task ID

    def get_new_subtask_id(self):
        """
        Generate a new unique Subtask ID.
        This method checks the highest Subtask ID in the current list of subtasks and returns a new unique ID.
        """
        return max((subtask.subtask_id for subtask in self.subtasks), default=0) + 1  # Generate the next Subtask ID

    def add_task(self, task_data: dict):
        """
        Add a new task to the task list.
        This method creates a new Task object, appends it to the task list, and saves the updated list to the Excel file.
        :param task_data: A dictionary containing the task attributes.
        """
        task_id = self.get_new_task_id()  # Generate a new Task ID
        new_task = Task(task_id, **task_data)  # Create a new Task object with the provided data
        self.tasks.append(new_task)  # Add the new task to the list
        self.save_data()  # Save the updated task list to the Excel file

    def add_subtask(self, subtask_data: dict):
        """
        Add a new subtask to the subtask list.
        This method creates a new Subtask object, appends it to the subtask list, and saves the updated list to the Excel file.
        :param subtask_data: A dictionary containing the subtask attributes.
        """
        subtask_id = self.get_new_subtask_id()  # Generate a new Subtask ID
        new_subtask = Subtask(subtask_id, **subtask_data)  # Create a new Subtask object with the provided data
        self.subtasks.append(new_subtask)  # Add the new subtask to the list
        self.save_data()  # Save the updated subtask list to the Excel file

    def delete_task(self, task_id: int):
        """
        Delete a task and its associated subtasks.
        This method removes a task by its ID and also removes any subtasks associated with that task.
        :param task_id: The ID of the task to be deleted.
        """
        self.tasks = [task for task in self.tasks if task.task_id != task_id]  # Filter out the task with the given ID
        self.subtasks = [subtask for subtask in self.subtasks if subtask.task_id != task_id]  # Remove associated subtasks
        self.save_data()  # Save the updated task and subtask lists to the Excel file

    def delete_subtask(self, subtask_id: int):
        """
        Delete a subtask by its ID.
        This method removes a subtask from the subtask list based on its ID.
        :param subtask_id: The ID of the subtask to be deleted.
        """
        self.subtasks = [subtask for subtask in self.subtasks if subtask.subtask_id != subtask_id]  # Filter out the subtask
        self.save_data()  # Save the updated subtask list to the Excel file
