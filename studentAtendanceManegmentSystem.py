import tkinter as tk
from tkinter import messagebox
import datetime

class Student:
    def __init__(self, name, lname, id):
        self.name = name
        self.lname = lname
        self.id = id
        self.present = 0
        self.absent = 0

class SystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Attendance Management System")
        
        self.students = []

        self.create_gui()

    def create_gui(self):
        # Create GUI elements
        label_menu = tk.Label(self.root, text="Menu", font=("Arial", 16))
        label_menu.pack(pady=10)

        button_add = tk.Button(self.root, text="Add Student", command=self.create_student)
        button_add.pack()

        button_display = tk.Button(self.root, text="Display Students", command=self.display_students)
        button_display.pack()

        button_delete = tk.Button(self.root, text="Delete Student Profile", command=self.delete_student)
        button_delete.pack()

        button_check = tk.Button(self.root, text="Check Students' Attendance", command=self.check_attendance)
        button_check.pack()

        button_profile = tk.Button(self.root, text="Developer Information", command=self.show_profile)
        button_profile.pack()

        button_update = tk.Button(self.root, text="Update Student Profile", command=self.update_student)
        button_update.pack()

        button_exit = tk.Button(self.root, text="Exit", command=self.root.quit)
        button_exit.pack()

    def create_student(self):
        # Functionality for adding a student
        top = tk.Toplevel(self.root)
        top.title("Add Student")

        label_name = tk.Label(top, text="Enter name of student:")
        label_name.pack()
        entry_name = tk.Entry(top)
        entry_name.pack()

        label_lname = tk.Label(top, text="Enter last name of student:")
        label_lname.pack()
        entry_lname = tk.Entry(top)
        entry_lname.pack()

        label_id = tk.Label(top, text="Enter ID of student:")
        label_id.pack()
        entry_id = tk.Entry(top)
        entry_id.pack()

        button_submit = tk.Button(top, text="Submit", command=lambda: self.submit_student(entry_name.get(), entry_lname.get(), entry_id.get(), top))
        button_submit.pack()

    def submit_student(self, name, lname, id, top):
        # Function to handle submission of new student
        try:
            id = int(id)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid ID (numeric).")
            return
        
        for student in self.students:
            if student.id == id:
                messagebox.showerror("Error", "Student with this ID already exists.")
                return
        
        student = Student(name, lname, id)
        self.students.append(student)
        messagebox.showinfo("Success", "Student added successfully.")
        top.destroy()

    def display_students(self):
        # Functionality for displaying students
        top = tk.Toplevel(self.root)
        top.title("Display Students")

        if not self.students:
            label_empty = tk.Label(top, text="No students to display.")
            label_empty.pack()
        else:
            for student in self.students:
                label_student = tk.Label(top, text=f"Name: {student.name} {student.lname}, ID: {student.id}, Present: {student.present}, Absent: {student.absent}")
                label_student.pack()

    def delete_student(self):
        # Functionality for deleting a student
        top = tk.Toplevel(self.root)
        top.title("Delete Student")

        label_id = tk.Label(top, text="Enter ID of student you want to delete:")
        label_id.pack()
        entry_id = tk.Entry(top)
        entry_id.pack()

        button_delete = tk.Button(top, text="Delete", command=lambda: self.delete_student_confirm(entry_id.get(), top))
        button_delete.pack()

    def delete_student_confirm(self, id, top):
        # Function to confirm and delete a student
        try:
            id = int(id)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid ID (numeric).")
            return
        
        for student in self.students:
            if student.id == id:
                self.students.remove(student)
                messagebox.showinfo("Success", "Student deleted successfully.")
                top.destroy()
                return
        
        messagebox.showerror("Error", "Student not found.")

    def check_attendance(self):
        # Functionality for checking attendance
        top = tk.Toplevel(self.root)
        top.title("Check Attendance")

        label_date = tk.Label(top, text="Enter date (DD/MM/YYYY):")
        label_date.pack()
        entry_date = tk.Entry(top)
        entry_date.pack()

        label_subject = tk.Label(top, text="Choose the subject:")
        label_subject.pack()

        options = ["Python", "Software Engineering", "Economics", "Inclusive", "Discrete"]
        var_subject = tk.StringVar(top)
        var_subject.set(options[0]) # Default value

        dropdown_subject = tk.OptionMenu(top, var_subject, *options)
        dropdown_subject.pack()

        button_check = tk.Button(top, text="Check Attendance", command=lambda: self.check_attendance_confirm(entry_date.get(), var_subject.get(), top))
        button_check.pack()

    def check_attendance_confirm(self, date, subject, top):
        # Function to confirm attendance check
        try:
            day, month, year = map(int, date.split('/'))
            datetime.datetime(year, month, day) # Check if the date is valid
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid date (DD/MM/YYYY).")
            return
        
        messagebox.showinfo("Attendance", f"{subject} class attendance for {date}:")

        for student in self.students:
            present = messagebox.askyesno(f"Attendance for {student.name}", f"Is {student.name} present?")
            if present:
                student.present += 1
            else:
                student.absent += 1

        top.destroy()

    def show_profile(self):
        # Functionality for showing developer information
        top = tk.Toplevel(self.root)
        top.title("Developer Information")

        label_info = tk.Label(top, text="Developer Information")
        label_info.pack()

        label_profile = tk.Label(top, text="-----------------------------------------------------------------------------------\n"
                                          "|   -> PYTHON PROJECT                                                             |\n"
                                          "|   -> Debre Birhan UNIVERSITY || DEPARTMENT OF SOFTWARE ENGINEERING ||              |\n"
                                          "|   -> PROJECT TITLE : STUDENT ATTENDANCE MANAGEMENT SYSTEM                         |\n"
                                          "|   -> COURSE INSTRUCTOR : Temesgen                                                 |\n"
                                          "|                 ------------------------------------------                        |\n"
                                          "|               |        PREPARED BY                         |                      |\n"
                                          "|               |   NAME                        ID           |                      |\n"
                                          "|               |   1.Rediet Sharew            1501430       |                      |\n"
                                          "|               |   2.Sosina Mulatu            1501481       |                      |\n"
                                          "|               |   3.Betelhem Worku           1501055       |                      |\n"
                                          "|                  ------------------------------------------                        |\n"
                                          "----------------------------------------------------------------------------------|")
        label_profile.pack()

    def update_student(self):
        # Functionality for updating student profile
        top = tk.Toplevel(self.root)
        top.title("Update Student Profile")

        label_id = tk.Label(top, text="Enter ID of student you want to update:")
        label_id.pack()
        entry_id = tk.Entry(top)
        entry_id.pack()

        button_update = tk.Button(top, text="Update", command=lambda: self.update_student_confirm(entry_id.get(), top))
        button_update.pack()

    def update_student_confirm(self, id, top):
        # Function to confirm and update student profile
        try:
            id = int(id)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid ID (numeric).")
            return
        
        for student in self.students:
            if student.id == id:
                student.name = input("Enter new name: ")
                student.lname = input("Enter new lname: ")
                student.id = int(input("Enter new id: "))
                messagebox.showinfo("Success", "Student information updated successfully.")
                top.destroy()
                return
        
        messagebox.showerror("Error", "Student not found.")

    def save_data(self):
        # Function to save data to file
        with open("students.txt", "w") as file:
            for student in self.students:
                file.write(f"{student.name},{student.lname},{student.id},{student.present},{student.absent}\n")
            messagebox.showinfo("Success", "Data saved successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SystemGUI(root)
    root.mainloop()
    