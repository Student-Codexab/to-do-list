from tkinter import *
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(END, task)
        task_entry.delete(0, END)
        save_tasks_to_file()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)
        save_tasks_to_file()
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def save_tasks_to_file():
    with open("tasks.txt", "w") as file:
        tasks = tasks_listbox.get(0, END)
        for task in tasks:
            file.write(task + "\n")

def load_tasks_from_file():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                tasks_listbox.insert(END, task.strip())
    except FileNotFoundError:
        pass  # If the file doesn't exist yet

# Create the main window
root = Tk()
root.title("To-Do List Application")
icon_image = PhotoImage(file="task.png")
root.iconphoto(False,icon_image)
root.geometry("430x420+100+100")
root.resizable(False,False)
# Create widgets
task_entry = Entry(root, width=20,font=('arial black',12,'normal'),borderwidth=10)
task_entry.grid(row=0, column=2, padx=10, pady=10)

add_button = Button(root, text="Add Task", command=add_task,width=10,font=" arial 15 bold",bg="#5a95ff",fg="#fff",bd=0)
add_button.grid(row=1, column=2, padx=10, pady=10)

delete_icon = PhotoImage(file="delete.png")
delete_button = Button(root,image=delete_icon,bd=0,command=remove_task)
delete_button.grid(row=1, column=3, padx=10, pady=10)

tasks_listbox = Listbox(root,width=35,borderwidth=10,font=('calibre',14,'bold'))
tasks_listbox.grid(row=2, column=2, columnspan=5, padx=10, pady=10)

load_tasks_from_file()

# Run the main event loop
root.mainloop()
print("Hello world")
