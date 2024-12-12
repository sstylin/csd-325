
# Todo Application
# Original code : Python Tkinter By Example : https://github.com/Dvlv/Tkinter-By-Example/blob/master/Tkinter-By-Example.pdf
# Modified by Steve Stylin@BEllevue University. Module 10.2-  GUI ToDo

# Change the Color of Menu Items: We will define two complementary colors for the task labels.
# Change Mouse Button for Deletion: The deletion of tasks will now be triggered by the right mouse button (Button-3).
# Add Instructional Label: An instruction label will be added to inform users how to delete a task.
# Implement Exit Menu Item: A menu item under "File" will be added to allow users to exit the application gracefully.

import tkinter as tk
import tkinter.messagebox as msg

class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()
        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        self.tasks_canvas = tk.Canvas(self)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)
        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.title("Stylin-ToDo")
        self.geometry("300x400")

        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")

        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_frame = self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="n")

        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        # Instructional label added
        instruction_label = tk.Label(self.tasks_frame, text="Instruction Added ---**Right-click to delete a task**---",bg="darkviolet", fg="white", pady=10)
        instruction_label.pack(side=tk.TOP, fill=tk.X)

        # Task labels with complementary colors
        todo1 = tk.Label(self.tasks_frame, text="Grade 325 Discussion Board", bg="gold", fg="black", pady=10)
        todo2 = tk.Label(self.tasks_frame, text="Grade 325 Tkinter program", bg="darkviolet", fg="white", pady=10)
        todo3 = tk.Label(self.tasks_frame, text="Advance Python", bg="gold", fg="black", pady=10)
        todo4 = tk.Label(self.tasks_frame, text="Module 10.2-", bg="darkviolet", fg="white", pady=10)

        # Bind right mouse button for deletion
        todo1.bind("<Button-3>", self.remove_task)
        todo2.bind("<Button-3>", self.remove_task)
        todo3.bind("<Button-3>", self.remove_task)
        todo4.bind("<Button-3>", self.remove_task)

        self.tasks.append(todo1)
        self.tasks.append(todo2)
        self.tasks.append(todo3)
        self.tasks.append(todo4)

        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        # Adding the exit menu item
        menubar = tk.Menu(self)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        self.config(menu=menubar)

        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, tk.END).strip()
        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)
            self.set_task_colour(len(self.tasks), new_task)
            new_task.bind("<Button-3>", self.remove_task)  # Bind right-click for new tasks
            new_task.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(new_task)
        self.task_create.delete(1.0, tk.END)

    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):
            self.tasks.remove(event.widget)
            event.widget.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        colours = [("darkviolet", "white"), ("gold", "black")]
        my_scheme_choice = colours[position % len(colours)]
        task.configure(bg=my_scheme_choice[0])
        task.configure(fg=my_scheme_choice[1])

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width=canvas_width)

    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        else:
            move = 1 if event.num == 5 else -1
            self.tasks_canvas.yview_scroll(move, "units")


if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()