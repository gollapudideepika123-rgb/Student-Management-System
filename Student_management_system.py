import tkinter as tk
from tkinter import messagebox
def msg():
        if (name.get() == "" or age.get() == "" or course.get() == ""):
            messagebox.showerror("Error","Fill the all the fileds")
        else:
            op.insert(tk.END, f"Name: {name.get()} | Age: {age.get()} | Course: {course.get()}\n")
            messagebox.showinfo("Success","Successfully added")
        name.delete(0, tk.END)
        course.delete(0, tk.END)
def msg1():
    select = op.curselection()
    if select:
        op.delete(select[0])
        messagebox.showinfo("Deleted", "Deleted Successfully")
    else:
        messagebox.showerror("Error", "Select a student to delete")
obj = tk.Tk()
obj.geometry("600x600")
obj.title("Student Management System")
tk.Label(obj,text = "Student Management System",
        font = ("Arial",30,"bold")).pack(pady = 10)
f= tk.Frame(obj)
f.pack()
tk.Label(f,text = "Name").grid(row = 0,column = 0,padx=5, pady=5)
name = tk.Entry(f)    
name.grid(row = 0,column = 1)
tk.Label(f,text = "Age").grid(row = 1,column = 0,padx=5, pady=5)
age = tk.Scale(f,from_ =1,to = 40,orient = tk.HORIZONTAL,resolution = 1)
age.grid(row = 1,column = 1,padx=5, pady=5)
tk.Label(f,text = "Course").grid(row = 2,column = 0,padx=5, pady=5)
course= tk.Entry(f)
course.grid(row = 2,column = 1,padx=5, pady=5)
tk.Button(obj,text = "Add Student",command = msg).pack(pady = 10)
op = tk.Listbox(obj,height =15,width = 300,bd = 5)
op.pack(pady = 10)
tk.Button(obj,text = "delete Student",command = msg1).pack(pady = 10)

