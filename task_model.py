# Define the Task class, which represents a task with various attributes such as ID, name, category, and status.
class Task:
    def __init__(self, task_id: int, name: str, category: str, priority: str, start_date: str, due_date: str,
                 status: str, progress: str, notes: str):
        """
        Initializes a new Task object with the specified attributes.
        :param task_id: The unique identifier for the task.
        :param name: The name of the task.
        :param category: The category of the task (e.g., Work, Personal).
        :param priority: The priority level of the task (e.g., High, Medium, Low).
        :param start_date: The start date of the task.
        :param due_date: The due date of the task.
        :param status: The current status of the task (e.g., In Progress, Completed).
        :param progress: The percentage progress of the task (e.g., 50%).
        :param notes: Any additional notes related to the task.
        """
        self.task_id = task_id  # Unique ID for the task
        self.name = name  # Task name
        self.category = category  # Task category (e.g., Work, Personal)
        self.priority = priority  # Task priority (e.g., High, Medium, Low)
        self.start_date = start_date  # When the task starts
        self.due_date = due_date  # Task deadline
        self.status = status  # Task status (e.g., In Progress, Completed)
        self.progress = progress  # Progress percentage (e.g., 50%)
        self.notes = notes  # Additional task notes

    def as_list(self) -> list:
        """
        Returns the task's attributes as a list. This method is useful for saving the task data to Excel.
        :return: A list representation of the task's attributes.
        """
        return [self.task_id, self.name, self.category, self.priority, self.start_date, self.due_date,
                self.status, self.progress, self.notes]


# Define the Subtask class, which represents a subtask with various attributes such as ID, name, and status.
class Subtask:
    def __init__(self, subtask_id: int, task_id: int, name: str, status: str, progress: str,
                 due_date: str, completed_date: str):
        """
        Initializes a new Subtask object with the specified attributes.
        :param subtask_id: The unique identifier for the subtask.
        :param task_id: The ID of the parent task to which this subtask belongs.
        :param name: The name of the subtask.
        :param status: The current status of the subtask (e.g., In Progress, Completed).
        :param progress: The percentage progress of the subtask (e.g., 30%).
        :param due_date: The due date of the subtask.
        :param completed_date: The date the subtask was completed.
        """
        self.subtask_id = subtask_id  # Unique ID for the subtask
        self.task_id = task_id  # ID of the parent task
        self.name = name  # Subtask name
        self.status = status  # Subtask status (e.g., In Progress, Completed)
        self.progress = progress  # Subtask progress percentage (e.g., 30%)
        self.due_date = due_date  # Subtask deadline
        self.completed_date = completed_date  # Date the subtask was completed (optional)

    def as_list(self) -> list:
        """
        Returns the subtask's attributes as a list. This method is useful for saving the subtask data to Excel.
        :return: A list representation of the subtask's attributes.
        """
        return [self.subtask_id, self.task_id, self.name, self.status, self.progress, self.due_date, self.completed_date]
