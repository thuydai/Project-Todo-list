from tkinter import *
import tkinter.messagebox
from tkinter import ttk

window = Tk()
window.title("To-Do List App")
window.geometry("500x550")

work_var = IntVar(value=1) 
housework_var = IntVar()
else_var = IntVar()

def entertask():
    def add():
        input_text = entry_task.get(1.0, "end-1c")
        
        selected_categories = []
        if work_var.get() == 1:
            selected_categories.append("Work")
        if housework_var.get() == 1:
            selected_categories.append("Housework")
        if else_var.get() == 1:
            selected_categories.append("Else")
        
        if input_text == "":
            tkinter.messagebox.showwarning(title="Error!", message="Please enter some text")
        elif not selected_categories:
            tkinter.messagebox.showwarning(title="Error!", message="Please select at least one category")
        elif len(selected_categories) > 1:
            tkinter.messagebox.showwarning(title="Error!", message="Please select only one category")
            
        else:
            task_with_category = f"[{selected_categories[0]}] {input_text}"
            listbox_task.insert(END, task_with_category)
            root1.destroy()
    
    root1 = Toplevel()
    root1.title("Add your task")
    root1.geometry("300x250")
    
    Label(root1, text="Enter your task:", font=("Arial", 10, "bold")).pack(pady=10)
    entry_task = Text(root1, width=40, height=3)
    entry_task.pack(pady=5)
    
    Label(root1, text="Select task categories:", font=("Arial", 10, "bold")).pack(pady=10)
    
    checkbox_frame = Frame(root1)
    checkbox_frame.pack(pady=5)
    
    work_checkbox = Checkbutton(checkbox_frame, text="Work", variable=work_var, font=("Arial", 9))
    work_checkbox.grid(row=0, column=0, padx=10, sticky=W)
    
    housework_checkbox = Checkbutton(checkbox_frame, text="Housework", variable=housework_var, font=("Arial", 9))
    housework_checkbox.grid(row=0, column=1, padx=10, sticky=W)
    
    else_checkbox = Checkbutton(checkbox_frame, text="Else", variable=else_var, font=("Arial", 9))
    else_checkbox.grid(row=0, column=2, padx=10, sticky=W)
    
    button_frame = Frame(root1)
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

def deletetask():
    try:
        selected = listbox_task.curselection()
        listbox_task.delete(selected[0])
    except:
        tkinter.messagebox.showwarning(title="Error!", message="Please select a task to delete!")

def markcompleted():
    try:
        selected = listbox_task.curselection()
        temp = selected[0]
        temp_marked = listbox_task.get(selected)
        if " ✔" not in temp_marked:
            temp_marked = temp_marked + " ✔"
            listbox_task.delete(temp)
            listbox_task.insert(temp, temp_marked)
    except:
        tkinter.messagebox.showwarning(title="Error!", message="Please select a task to mark!")

label = Label(window, 
              text='To-do List', 
              font=('Helvetica', 22, 'bold'), 
              fg='#38db7d')
label.pack(pady=10)

frame_task = Frame(window)
frame_task.pack(pady=10)

listbox_task = Listbox(frame_task, 
                       bg="black", 
                       fg="white", 
                       height=12, 
                       width=50, 
                       font="Helvetica",
                       selectbackground="#4CAF50")  
listbox_task.pack(side=LEFT)

scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=RIGHT, fill=Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

Button(window, 
       text="Add task", 
       width=50, 
       command=entertask, 
       bg="#4CAF50", 
       fg="white", 
       font=("Arial", 10, "bold")).pack(pady=3)

Button(window, 
       text="Delete selected task", 
       width=50, 
       command=deletetask,
       bg="#f44336", 
       fg="white", 
       font=("Arial", 10, "bold")).pack(pady=3)

Button(window, 
       text="Mark as completed", 
       width=50, 
       command=markcompleted,
       bg="#FFC400", 
       fg="white", 
       font=("Arial", 10, "bold")).pack(pady=3)

window.mainloop()