import tkinter as tk
from tkinter import ttk, messagebox

marks_records = []
courses = [
    "Computer Science", "Mechanical", "Electrical", "Chemical", "Aerospace", 
    "Artificial Intelligence & Machine Learning", "Data Science",
    "Robotics", "Biomedical", "Cyber Security"
]

subjects = ["CSE", "Calculus", "Computational Physics", "AI ML", "English", "EVS"]

def is_valid_marks(marks_str):
    if marks_str == "":
        return False
    for ch in marks_str:
        if ch < '0' or ch > '9':
            return False
    marks = int(marks_str)
    if marks < 0 or marks > 100:
        return False
    return True

def calculate_grade(marks):
    if marks >= 90:
        return 'S'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B'
    elif marks >= 60:
        return 'C'
    elif marks >= 50:
        return 'D'
    else:
        return 'F'

def add_marks():
    name = entry_name.get().strip()
    roll = entry_roll.get().strip()
    course = combo_course.get()
    subject = combo_subject.get()
    marks_str = entry_marks.get().strip()

    if not name:
        messagebox.showerror("Missing Name", "Name is required.")
        return
    if not is_valid_marks(marks_str):
        messagebox.showerror("Invalid Marks", "Marks must be an integer between 0 and 100.")
        return

    marks = int(marks_str)
    grade = calculate_grade(marks)

    for record in marks_records:
        if record["Roll"] == roll and record["Subject"] == subject:
            messagebox.showerror("Duplicate Entry", f"Marks for roll {roll} and subject {subject} already recorded.")
            return

    record = {"Name": name, "Roll": roll, "Course": course, "Subject": subject, "Marks": marks, "Grade": grade}
    marks_records.append(record)

    update_table()

    entry_name.delete(0, tk.END)
    entry_roll.delete(0, tk.END)
    entry_marks.delete(0, tk.END)
    combo_course.current(0)
    combo_subject.current(0)

    messagebox.showinfo("Success", f"Marks added for {name} in {subject} with grade {grade}!")

def update_table():
    for row in marks_table.get_children():
        marks_table.delete(row)
    idx = 0
    for record in marks_records:
        marks_table.insert("", "end", iid=idx, values=(
            record["Name"],
            record["Roll"],
            record["Course"],
            record["Subject"],
            record["Marks"],
            record["Grade"]
        ))
        idx += 1

def remove_record():
    selected = marks_table.selection()
    if len(selected) == 0:
        messagebox.showwarning("Select Entry", "No record selected.")
        return
    idx = int(selected[0])
    record = marks_records.pop(idx)
    update_table()
    label_details.config(text="Select a record above to see details.")
    messagebox.showinfo("Removed", f"Marks record for {record['Name']} in {record['Subject']} removed.")

def show_details(event):
    selected = marks_table.selection()
    if len(selected) == 0:
        label_details.config(text="Select a record above to see details.")
        return
    idx = int(selected[0])
    record = marks_records[idx]
    text = (f"Record Details:\nName: {record['Name']}\nRoll Number: {record['Roll']}\n"
            f"Course: {record['Course']}\nSubject: {record['Subject']}\nMarks: {record['Marks']}\nGrade: {record['Grade']}")
    label_details.config(text=text)

root = tk.Tk()
root.title("Marks Management System")

reg_frame = tk.LabelFrame(root, text="Marks Entry", padx=10, pady=10)
reg_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

tk.Label(reg_frame, text="Name:").grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(reg_frame)
entry_name.grid(row=0, column=1)

tk.Label(reg_frame, text="Reg. No.:").grid(row=1, column=0, sticky="w")
entry_roll = tk.Entry(reg_frame)
entry_roll.grid(row=1, column=1)

tk.Label(reg_frame, text="Course:").grid(row=2, column=0, sticky="w")
combo_course = ttk.Combobox(reg_frame, values=courses, state="readonly")
combo_course.grid(row=2, column=1)
combo_course.current(0)

tk.Label(reg_frame, text="Subject:").grid(row=3, column=0, sticky="w")
combo_subject = ttk.Combobox(reg_frame, values=subjects, state="readonly")
combo_subject.grid(row=3, column=1)
combo_subject.current(0)

tk.Label(reg_frame, text="Marks:").grid(row=4, column=0, sticky="w")
entry_marks = tk.Entry(reg_frame)
entry_marks.grid(row=4, column=1)

btn_add = tk.Button(reg_frame, text="Add Marks", command=add_marks)
btn_add.grid(row=5, column=0, columnspan=2, pady=5)

list_frame = tk.LabelFrame(root, text="Marks Records", padx=10, pady=10)
list_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

marks_table = ttk.Treeview(list_frame, columns=("Name", "Roll", "Course", "Subject", "Marks", "Grade"), show="headings", height=8)
for col in marks_table["columns"]:
    marks_table.heading(col, text=col)
marks_table.grid(row=0, column=0, sticky="nsew")

btn_remove = tk.Button(list_frame, text="Remove Record", command=remove_record)
btn_remove.grid(row=1, column=0, pady=5)

details_frame = tk.LabelFrame(root, text="Record Details", padx=10, pady=10)
details_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

label_details = tk.Label(details_frame, text="Select a record above to see details.")
label_details.pack()

marks_table.bind("<<TreeviewSelect>>", show_details)

root.mainloop()
