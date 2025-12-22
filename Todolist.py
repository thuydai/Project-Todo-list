"""
A To-Do List application built with tkinter.

This application allows users to add, delete, and mark tasks as completed.
Tasks can be categorized as Work, Housework, or Else.
"""

from tkinter import *
import tkinter.messagebox


window = Tk()
"""
Main application window (Tkinter root window).

:type: Tk
:attributes:
    - title: "To-Do List App"
    - geometry: 500x550 pixels
:contains:
    - Title label
    - Task list frame with listbox and scrollbar
    - Three action buttons (Add, Delete, Mark as completed)
:events:
    - Handles all user interactions through the Tkinter event loop
:raises tkinter.TclError: If window creation fails
"""
window.title("To-Do List App")
window.geometry("500x550")


work_var = IntVar()
"""
Variable to store the state of the Work checkbox.

:type: IntVar
:default: 0 (checked by default)
""" 
housework_var = IntVar()
"""
Variable to store the state of the Housework checkbox.

:type: IntVar
:default: 0 (unchecked by default)
"""
else_var = IntVar()
"""
Variable to store the state of the Else checkbox.

:type: IntVar
:default: 0 (unchecked by default)
"""


def entertask():
    """
    Open a new window to add a task with category selection.
    
    Creates a Toplevel window with:
    - A text entry field for the task description
    - Three checkboxes for category selection (Work, Housework, Else)
    - Add and Cancel buttons
    
    The function validates that:
    1. Task text is not empty
    2. At least one category is selected
    3. Only one category is selected
    
    If validation passes, the task is added to the main listbox
    in the format: "[Category] + [Entered task]"

    :raises tkinter.TclError: If there's an issue creating the Toplevel window
    :returns: None
    """
    def add():
        """
        Inner function to handle the addition of a new task.
        
        This function is called when the Add button is clicked.
        It retrieves the task text and selected categories,
        validates the input, and adds the task to the main listbox.
        
        Inner function to handle the addition of a new task.
        
        :raises ValueError: If input validation fails
        :raises IndexError: If category selection is invalid
        :returns: None
        """

        try:
            input_text = entry_task.get(1.0, "end-1c").strip()
            
            selected_categories = []
            if work_var.get() == 1:
                selected_categories.append("Work")
            if housework_var.get() == 1:
                selected_categories.append("Housework")
            if else_var.get() == 1:
                selected_categories.append("Else")
            
            if not input_text:
                raise ValueError("Please enter some text")
            
            if not selected_categories:
                raise ValueError("Please select at least one category")
            
            if len(selected_categories) > 1:
                raise ValueError("Please select only one category")
                       
            task_with_category = f"[{selected_categories[0]}] {input_text}"
            listbox_task.insert(END, task_with_category)
            root1.destroy()
            
        except ValueError as ve:
            tkinter.messagebox.showwarning(title="Input Error", message=str(ve))
        except Exception as e:
            tkinter.messagebox.showerror(title="Unexpected Error", 
                                         message="An unexpected error occurred while adding task")
    
    try:
        root1 = Toplevel()
        """
        The Toplevel window for adding new tasks.
    
        :type: Toplevel
        :attributes:
        - title: "Add your task"
        - geometry: 300x250 pixels
        :contains:
        - Label: "Enter your task:"
        - Text widget: For task input
        - Label: "Select task categories:"
        - Frame with three checkboxes
        - Frame with Add and Cancel buttons
        """
        root1.title("Add your task")
        root1.geometry("300x250")
    
        Label(root1, text="Enter your task:", font=("Arial", 10, "bold")).pack(pady=10)
        entry_task = Text(root1, width=40, height=3)
        """
        Text widget for entering task description.
    
        :type: Text
        :attributes:
        - width: 40 characters
        - height: 3 lines
        """
        entry_task.pack(pady=5)

        Label(root1, text="Select task categories:", font=("Arial", 10, "bold")).pack(pady=10)
    
        checkbox_frame = Frame(root1)
        """
        Frame containing the category checkboxes.
    
        :type: Frame
        :purpose: Organize checkboxes in a horizontal layout
        """
        checkbox_frame.pack(pady=5)
    
        work_checkbox = Checkbutton(checkbox_frame, text="Work", variable=work_var, font=("Arial", 9))
        """
        Checkbox for Work category.
    
        :type: Checkbutton
        :attributes:
        - text: "Work"
        - variable: work_var (IntVar)
        - font: Arial, size 9
        :position: Grid row 0, column 0
        """
        work_checkbox.grid(row=0, column=0, padx=10, sticky=W)
    
        housework_checkbox = Checkbutton(checkbox_frame, text="Housework", variable=housework_var, font=("Arial", 9))
        """
        Checkbox for Housework category.
    
        :type: Checkbutton
        :attributes:
        - text: "Housework"
        - variable: housework_var (IntVar)
        - font: Arial, size 9
        :position: Grid row 0, column 1
        """
        housework_checkbox.grid(row=0, column=1, padx=10, sticky=W)
    
        else_checkbox = Checkbutton(checkbox_frame, text="Else", variable=else_var, font=("Arial", 9))
        """
        Checkbox for Else category.
    
        :type: Checkbutton
        :attributes:
        - text: "Else"
        - variable: else_var (IntVar)
        - font: Arial, size 9
        :position: Grid row 0, column 2
        """
        else_checkbox.grid(row=0, column=2, padx=10, sticky=W)
    
        button_frame = Frame(root1)
        """
        Frame containing the Add and Cancel buttons.
    
        :type: Frame
        :purpose: Organize buttons in a horizontal layout
        """
        button_frame.pack(pady=10)
    
        Button(button_frame, 
               text="Add task", 
               command=add, 
               bg="#4CAF50", 
               fg="white", 
               width=15).pack(side=LEFT, padx=5)
    
        Button(button_frame, 
               text="Cancel", 
               command=root1.destroy, 
               bg="#f44336", 
               fg="white", 
               width=15).pack(side=LEFT, padx=5)
        
    except Exception as e:
        tkinter.messagebox.showerror(title="Window Error", 
                                     message="Failed to create task entry window")

def deletetask():
    """
    Delete the currently selected task from the listbox.
    
    Retrieves the currently selected task using curselection()
    and removes it from the listbox.
    
    :raises IndexError: If no task is selected
    :returns: None
    """
    try:
        selected = listbox_task.curselection()
        if not selected:
            raise IndexError("No task selected") 
        listbox_task.delete(selected[0])
    except IndexError:
        tkinter.messagebox.showwarning(title="Selection Error", 
                                       message="Please select a task to delete!")
    except Exception:
        tkinter.messagebox.showerror(title="Error", 
                                     message="Failed to delete the task")

def markcompleted():
    """
    Mark a task as completed by appending a checkmark (✔) to it.
    
    Retrieves the currently selected task, checks if it's already marked,
    and if not, appends " ✔" to the task text. The task is then updated
    in the listbox.
    
    :raises IndexError: If no task is selected
    :returns: None
    """
    try:
        selected = listbox_task.curselection()
        if not selected:
            raise IndexError("No task selected")
        
        temp = selected[0]
        temp_marked = listbox_task.get(selected)
        
        if " ✔" not in temp_marked:
            temp_marked = temp_marked + " ✔"
            listbox_task.delete(temp)
            listbox_task.insert(temp, temp_marked)
        else:
            tkinter.messagebox.showinfo(title="Info", 
                                        message="Task is already marked as completed")
    except IndexError:
        tkinter.messagebox.showwarning(title="Selection Error", 
                                       message="Please select a task to mark!")
    except Exception:
        tkinter.messagebox.showerror(title="Error", 
                                     message="Failed to mark the task as completed")

try: 
    label = Label(window, 
                text='To-do List', 
                font=('Helvetica', 22, 'bold'), 
                fg='#38db7d')
    """
    Main application title label.

    :type: Label
    :attributes:
        - text: 'To-do List'
        - font: Helvetica, 22, bold
        - fg: Text color (#38db7d - green)
    """
    label.pack(pady=10)

    frame_task = Frame(window)
    """
    Frame containing the task listbox and scrollbar.

    :type: Frame
    :purpose: Container for listbox and scrollbar widgets
    """
    frame_task.pack(pady=10)

    listbox_task = Listbox(frame_task, 
                        bg="black", 
                        fg="white", 
                        height=12, 
                        width=50, 
                        font="Helvetica",
                        selectbackground="#4CAF50") 
    """
    The main listbox that displays all tasks.

    :type: Listbox
    :attributes:
        - bg: Background color (black)
        - fg: Text color (white)
        - height: Number of visible rows (12)
        - width: Width in characters (50)
        - font: Text font (Helvetica)
        - selectbackground: Background color for selected items (#4CAF50)
    """ 
    listbox_task.pack(side=LEFT)

    scrollbar_task = Scrollbar(frame_task)
    """
    Vertical scrollbar for the task listbox.

    :type: Scrollbar
    :purpose: Enables scrolling through tasks when list exceeds visible area
    """
    scrollbar_task.pack(side=RIGHT, fill=Y)
    listbox_task.config(yscrollcommand=scrollbar_task.set)
    scrollbar_task.config(command=listbox_task.yview)

    add_button = Button(window, 
        text="Add task", 
        width=50, 
        command=entertask, 
        bg="#4CAF50", 
        fg="white", 
        font=("Arial", 10, "bold"))
    """
    Button to open the task entry window.

    :type: Button
    :attributes:
        - text: "Add task"
        - width: 50 characters
        - bg: Background color (#4CAF50 - green)
        - fg: Text color (white)
        - font: Arial, 10, bold
    :command: Calls entertask() function when clicked
    """
    add_button.pack(pady=3)

    delete_button = Button(window, 
        text="Delete selected task", 
        width=50, 
        command=deletetask,
        bg="#f44336", 
        fg="white", 
        font=("Arial", 10, "bold"))
    """
    Button to delete the selected task.

    :type: Button
    :attributes:
        - text: "Delete selected task"
        - width: 50 characters
        - bg: Background color (#f44336 - red)
        - fg: Text color (white)
        - font: Arial, 10, bold
    :command: Calls deletetask() function when clicked
    """
    delete_button.pack(pady=3)

    complete_button = Button(window, 
        text="Mark as completed", 
        width=50, 
        command=markcompleted,
        bg="#FFC400", 
        fg="white", 
        font=("Arial", 10, "bold"))
    """
    Button to mark the selected task as completed.

    :type: Button
    :attributes:
        - text: "Mark as completed"
        - width: 50 characters
        - bg: Background color (#FFC400 - yellow/orange)
        - fg: Text color (white)
        - font: Arial, 10, bold
    :command: Calls markcompleted() function when clicked
    :note: Appends " ✔" to the task text to indicate completion
    """
    complete_button.pack(pady=3)
except Exception:
    tkinter.messagebox.showerror(title="Startup Error", 
                                 message="Failed to start the application")



try:
    window.mainloop()
except Exception:
    pass