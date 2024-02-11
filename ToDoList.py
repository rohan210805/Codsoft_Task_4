from tkinter import *

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do List')
        self.root.geometry('650x410+300+150')
        
        self.label = Label(self.root, text='To-Do List App', font='Arial 25 bold', width=20, bd=5, bg='lightblue', fg='black')
        self.label.pack(side='top', fill=BOTH)
        
        self.label2 = Label(self.root, text='Add Task', font='Arial 18 bold', width=10, bd=5, bg='lightgreen', fg='black')
        self.label2.place(x=40, y=54)
        
        self.label3 = Label(self.root, text='Tasks', font='Arial 18 bold', width=10, bd=5, bg='lightgreen', fg='black')
        self.label3.place(x=320, y=54)
        
        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font='Arial 15 italic')
        self.main_text.place(x=280, y=100)
        
        self.scrollbar = Scrollbar(self.root, orient=VERTICAL, command=self.main_text.yview)
        self.scrollbar.place(x=530, y=100, height=190)
        self.main_text.config(yscrollcommand=self.scrollbar.set)
        
        self.text = Text(self.root, bd=5, height=2, width=30, font='Arial 10 bold')
        self.text.place(x=20, y=120)
        
        # Add Task
        def add():
            content = self.text.get(1.0, END)
            if content.strip():  # Check if content is not empty
                self.main_text.insert(END, content)
                with open('data.txt', 'a') as file:
                    file.write(content.strip() + '\n')
                self.text.delete(1.0, END)
            
        # Delete Task
        def delete():
            selection = self.main_text.curselection()
            if selection:
                index = selection[0]
                self.main_text.delete(index)
                with open('data.txt', 'r') as file:
                    lines = file.readlines()
                with open('data.txt', 'w') as file:
                    for i, line in enumerate(lines):
                        if i != index:
                            file.write(line)
        
        # Read Tasks from file
        with open('data.txt', 'r') as file:
            tasks = file.readlines()
            for task in tasks:
                self.main_text.insert(END, task.strip())
        
        # Add Task Button
        self.button = Button(self.root, text='Add', font='Arial 15 bold italic', 
                             width=10, bd=5, bg='lightgreen', fg='black', command=add)
        self.button.place(x=30, y=180)
        
        # Delete Task Button
        self.button2 = Button(self.root, text='Delete', font='Arial 15 bold italic', 
                              width=10, bd=5, bg='lightgreen', fg='black', command=delete)
        self.button2.place(x=30, y=280)

def main():
    root = Tk()
    ui = Todo(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()
