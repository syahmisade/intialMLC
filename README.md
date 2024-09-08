### intialMLC

## Summary of When to Modify Each File:

# main.py:

- Only modified when you need to change the entry point of the app (e.g., if you're adding arguments or initializing a new module).

# task_manager_app.py (GUI and User Interaction):

- Add/modify buttons and form fields.
- Define what happens when buttons are clicked (linking to logic functions).
- Handle user input and basic validation before calling business logic.

# task_view.py (Displaying Data in the GUI):

- Modify how tasks and subtasks are displayed (e.g., adding new columns or changing formatting).
- Add dynamic loading of subtasks when tasks are selected.
- Modify Treeview behavior and refresh mechanisms when tasks are updated.

# task_manager_logic.py (Business Logic):

- Add or modify how tasks/subtasks are added, deleted, or modified.
- Implement any new operations related to task management (e.g., sorting, filtering, archiving).
- Link between the GUI and data (pass user input to Excel handling functions).

# excel_handler.py (File I/O and Excel Operations):

- Modify how tasks and subtasks are saved to or loaded from the Excel file.
- Add new fields to be saved in the Excel file.
- Handle file creation, updates, and reading/writing to ensure data persistence.

# task_model.py (Task and Subtask Data Structures):

- Add new fields or attributes to the Task or Subtask classes.
- Modify how task/subtask objects are structured or represented.
- Ensure that task/subtask data can be easily saved to Excel by modifying as_list() methods.
