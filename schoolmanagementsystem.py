import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root", 
            password="Sairam@3824",  
            database="schoolmanagement"  
        )
        self.cursor = self.conn.cursor()

    def add_student(self, student_id, student_name, student_grade):
        query = "INSERT INTO students (id, name, grade) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (student_id, student_name, student_grade))
        self.conn.commit()

    def delete_student(self, student_id):
        query = "DELETE FROM students WHERE id = %s"
        self.cursor.execute(query, (student_id,))
        self.conn.commit()

    def update_student(self, student_id, student_name, student_grade):
        query = "UPDATE students SET name = %s, grade = %s WHERE id = %s"
        self.cursor.execute(query, (student_name, student_grade, student_id))
        self.conn.commit()

    def add_teacher(self, teacher_id, teacher_name, teacher_department):
        query = "INSERT INTO teachers (id, name, department) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (teacher_id, teacher_name, teacher_department))
        self.conn.commit()

    def delete_teacher(self, teacher_id):
        query = "DELETE FROM teachers WHERE id = %s"
        self.cursor.execute(query, (teacher_id,))
        self.conn.commit()

    def update_teacher(self, teacher_id, teacher_name, teacher_department):
        query = "UPDATE teachers SET name = %s, department = %s WHERE id = %s"
        self.cursor.execute(query, (teacher_name, teacher_department, teacher_id))
        self.conn.commit()

    def add_course(self, course_id, course_name, course_credits):
        query = "INSERT INTO courses (id, name, credits) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (course_id, course_name, course_credits))
        self.conn.commit()

    def delete_course(self, course_id):
        query = "DELETE FROM courses WHERE id = %s"
        self.cursor.execute(query, (course_id,))
        self.conn.commit()

    def update_course(self, course_id, course_name, course_credits):
        query = "UPDATE courses SET name = %s, credits = %s WHERE id = %s"
        self.cursor.execute(query, (course_name, course_credits, course_id))
        self.conn.commit()

    def add_grade(self, student_id, course_id, grade):
        query = "INSERT INTO grades (student_id, course_id, grade) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (student_id, course_id, grade))
        self.conn.commit()

    def delete_grade(self, student_id, course_id):
        query = "DELETE FROM grades WHERE student_id = %s AND course_id = %s"
        self.cursor.execute(query, (student_id, course_id))
        self.conn.commit()

    def update_grade(self, student_id, course_id, grade):
        query = "UPDATE grades SET grade = %s WHERE student_id = %s AND course_id = %s"
        self.cursor.execute(query, (grade, student_id, course_id))
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

class Login:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("School Management System - Login")
        self.root.geometry("600x300")  

        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack(pady=10)
        self.username_entry = tk.Entry(self.root, width=40)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack(pady=10)
        self.password_entry = tk.Entry(self.root, width=40, show="*")
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(self.root, text="Login", command=self.check_credentials, width=20)
        self.login_button.pack(pady=20)

        self.root.mainloop()

    def check_credentials(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":  
            self.root.destroy()
            MainMenu()
        else:
            messagebox.showerror("Invalid credentials", "Invalid username or password")

class MainMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("School Management System - Main Menu")
        self.root.geometry("600x400")  

        self.student_button = tk.Button(self.root, text="Student Management", command=self.student_management, width=30)
        self.student_button.pack(pady=20)

        self.teacher_button = tk.Button(self.root, text="Teacher Management", command=self.teacher_management, width=30)
        self.teacher_button.pack(pady=10)

        self.course_button = tk.Button(self.root, text="Course Management", command=self.course_management, width=30)
        self.course_button.pack(pady=10)

        self.grade_button = tk.Button(self.root, text="Grade Management", command=self.grade_management, width=30)
        self.grade_button.pack(pady=10)

        self.root.mainloop()

    def student_management(self):
        StudentManagement()

    def teacher_management(self):
        TeacherManagement()

    def course_management(self):
        CourseManagement()

    def grade_management(self):
        GradeManagement()

class StudentManagement:
    def __init__(self):
        self.db = Database()
        self.root = tk.Tk()
        self.root.title("Student Management")
        self.root.geometry("600x500")  

        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Manage Students", font=("Arial", 20))
        title_label.pack(pady=20)

        self.student_id_label = tk.Label(self.root, text="Student ID:")
        self.student_id_label.pack(pady=5)
        self.student_id_entry = tk.Entry(self.root, width=40)
        self.student_id_entry.pack(pady=5)

        self.student_name_label = tk.Label(self.root, text="Student Name:")
        self.student_name_label.pack(pady=5)
        self.student_name_entry = tk.Entry(self.root, width=40)
        self.student_name_entry.pack(pady=5)

        self.student_grade_label = tk.Label(self.root, text="Student Grade:")
        self.student_grade_label.pack(pady=5)
        self.student_grade_entry = tk.Entry(self.root, width=40)
        self.student_grade_entry.pack(pady=5)

        self.add_button = tk.Button(self.root, text="Add Student", command=self.add_student, width=20)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Student", command=self.delete_student, width=20)
        self.delete_button.pack(pady=5)

        self.update_button = tk.Button(self.root, text="Update Student", command=self.update_student, width=20)
        self.update_button.pack(pady=5)

        self.view_button = tk.Button(self.root, text="View Students", command=self.view_students, width=20)
        self.view_button.pack(pady=5)

    def add_student(self):
        student_id = self.student_id_entry.get()
        student_name = self.student_name_entry.get()
        student_grade = self.student_grade_entry.get()
        
        try:
            self.db.add_student(student_id, student_name, student_grade)
            messagebox.showinfo("Success", "Student added successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", str(err))

    def delete_student(self):
        student_id = self.student_id_entry.get()
        
        try:
            self.db.delete_student(student_id)
            messagebox.showinfo("Success", "Student deleted successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", str(err))

    def update_student(self):
        student_id = self.student_id_entry.get()
        student_name = self.student_name_entry.get()
        student_grade = self.student_grade_entry.get()
        
        try:
            self.db.update_student(student_id, student_name, student_grade)
            messagebox.showinfo("Success", "Student updated successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", str(err))

    def view_students(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("View Students")
        view_window.geometry("500x300")

        tree = ttk.Treeview(view_window, columns=("ID", "Name", "Grade"), show='headings')
        tree.heading("ID", text="Student ID")
        tree.heading("Name", text="Student Name")
        tree.heading("Grade", text="Student Grade")
        tree.pack(fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(view_window, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.db.cursor.execute("SELECT id, name, grade FROM students")
        records = self.db.cursor.fetchall()

        for student_id, student_name, student_grade in records:
            tree.insert("", tk.END, values=(student_id, student_name, student_grade))

        if not records:
            messagebox.showinfo("Info", "No students found.")

class TeacherManagement:
    def __init__(self):
        self.db = Database()
        self.root = tk.Tk()
        self.root.title("Teacher Management")
        self.root.geometry("600x500")  

        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Manage Teachers", font=("Arial", 20))
        title_label.pack(pady=20)

        self.teacher_id_label = tk.Label(self.root, text="Teacher ID:")
        self.teacher_id_label.pack(pady=5)
        self.teacher_id_entry = tk.Entry(self.root, width=40)
        self.teacher_id_entry.pack(pady=5)

        self.teacher_name_label = tk.Label(self.root, text="Teacher Name:")
        self.teacher_name_label.pack(pady=5)
        self.teacher_name_entry = tk.Entry(self.root, width=40)
        self.teacher_name_entry.pack(pady=5)

        self.teacher_department_label = tk.Label(self.root, text="Department:")
        self.teacher_department_label.pack(pady=5)
        self.teacher_department_entry = tk.Entry(self.root, width=40)
        self.teacher_department_entry.pack(pady=5)

        self.add_button = tk.Button(self.root, text="Add Teacher", command=self.add_teacher, width=20)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Teacher", command=self.delete_teacher, width=20)
        self.delete_button.pack(pady=5)

        self.update_button = tk.Button(self.root, text="Update Teacher", command=self.update_teacher, width=20)
        self.update_button.pack(pady=5)

        self.view_button = tk.Button(self.root, text="View Teachers", command=self.view_teachers, width=20)
        self.view_button.pack(pady=5)

    def add_teacher(self):
        teacher_id = self.teacher_id_entry.get()
        teacher_name = self.teacher_name_entry.get()
        teacher_department = self.teacher_department_entry.get()
        
        try:
            self.db.add_teacher(teacher_id, teacher_name, teacher_department)
            messagebox.showinfo("Success", "Teacher added successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", str(err))

    def delete_teacher(self):
        teacher_id = self.teacher_id_entry.get()
        
        try:
            self.db.delete_teacher(teacher_id)
            messagebox.showinfo("Success", "Teacher deleted successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", str(err))

    def update_teacher(self):
        teacher_id = self.teacher_id_entry.get()
        teacher_name = self.teacher_name_entry.get()
        teacher_department = self.teacher_department_entry.get()
        
        try:
            self.db.update_teacher(teacher_id, teacher_name, teacher_department)
            messagebox.showinfo("Success", "Teacher updated successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", str(err))

    def view_teachers(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("View Teachers")
        view_window.geometry("500x300")

        tree = ttk.Treeview(view_window, columns=("ID", "Name", "Department"), show='headings')
        tree.heading("ID", text="Teacher ID")
        tree.heading("Name", text="Teacher Name")
        tree.heading("Department", text="Department")
        tree.pack(fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(view_window, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.db.cursor.execute("SELECT id, name, department FROM teachers")
        records = self.db.cursor.fetchall()

        for teacher_id, teacher_name, teacher_department in records:
            tree.insert("", tk.END, values=(teacher_id, teacher_name, teacher_department))

        if not records:
            messagebox.showinfo("Info", "No teachers found.")

class CourseManagement:
    def __init__(self):
        self.db = Database()
        self.root = tk.Tk()
        self.root.title("Course Management")
        self.root.geometry("600x500")  

        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Manage Courses", font=("Arial", 20))
        title_label.pack(pady=20)

        self.course_id_label = tk.Label(self.root, text="Course ID:")
        self.course_id_label.pack(pady=5)
        self.course_id_entry = tk.Entry(self.root, width=40)
        self.course_id_entry.pack(pady=5)

        self.course_name_label = tk.Label(self.root, text="Course Name:")
        self.course_name_label.pack(pady=5)
        self.course_name_entry = tk.Entry(self.root, width=40)
        self.course_name_entry.pack(pady=5)

        self.course_credits_label = tk.Label(self.root, text="Credits:")
        self.course_credits_label.pack(pady=5)
        self.course_credits_entry = tk.Entry(self.root, width=40)
        self.course_credits_entry.pack(pady=5)

        self.add_button = tk.Button(self.root, text="Add Course", command=self.add_course, width=20)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Course", command=self.delete_course, width=20)
        self.delete_button.pack(pady=5)

        self.update_button = tk.Button(self.root, text="Update Course", command=self.update_course, width=20)
        self.update_button.pack(pady=5)

        self.view_button = tk.Button(self.root, text="View Courses", command=self.view_courses, width=20)
        self.view_button.pack(pady=5)

    def add_course(self):
        course_id = self.course_id_entry.get()
        course_name = self.course_name_entry.get()
        course_credits = self.course_credits_entry.get()
        
        try:
            self.db.add_course(course_id, course_name, course_credits)
            messagebox.showinfo("Success", "Course added successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", str(err))

    def delete_course(self):
        course_id = self.course_id_entry.get()
        
        try:
            self.db.delete_course(course_id)
            messagebox.showinfo("Success", "Course deleted successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", str(err))

    def update_course(self):
        course_id = self.course_id_entry.get()
        course_name = self.course_name_entry.get()
        course_credits = self.course_credits_entry.get()
        
        try:
            self.db.update_course(course_id, course_name, course_credits)
            messagebox.showinfo("Success", "Course updated successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", str(err))

    def view_courses(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("View Courses")
        view_window.geometry("500x300")

        tree = ttk.Treeview(view_window, columns=("ID", "Name", "Credits"), show='headings')
        tree.heading("ID", text="Course ID")
        tree.heading("Name", text="Course Name")
        tree.heading("Credits", text="Credits")
        tree.pack(fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(view_window, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.db.cursor.execute("SELECT id, name, credits FROM courses")
        records = self.db.cursor.fetchall()

        for course_id, course_name, course_credits in records:
            tree.insert("", tk.END, values=(course_id, course_name, course_credits))

        if not records:
            messagebox.showinfo("Info", "No courses found.")

class GradeManagement:
    def __init__(self):
        self.db = Database()
        self.root = tk.Tk()
        self.root.title("Grade Management")
        self.root.geometry("600x500")  

        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Manage Grades", font=("Arial", 20))
        title_label.pack(pady=20)

        self.student_id_label = tk.Label(self.root, text="Student ID:")
        self.student_id_label.pack(pady=5)
        self.student_id_entry = tk.Entry(self.root, width=40)
        self.student_id_entry.pack(pady=5)

        self.course_id_label = tk.Label(self.root, text="Course ID:")
        self.course_id_label.pack(pady=5)
        self.course_id_entry = tk.Entry(self.root, width=40)
        self.course_id_entry.pack(pady=5)

        self.grade_label = tk.Label(self.root, text="Grade:")
        self.grade_label.pack(pady=5)
        self.grade_entry = tk.Entry(self.root, width=40)
        self.grade_entry.pack(pady=5)

        self.add_button = tk.Button(self.root, text="Add Grade", command=self.add_grade, width=20)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Grade", command=self.delete_grade, width=20)
        self.delete_button.pack(pady=5)

        self.update_button = tk.Button(self.root, text="Update Grade", command=self.update_grade, width=20)
        self.update_button.pack(pady=5)

        self.view_button = tk.Button(self.root, text="View Grades", command=self.view_grades, width=20)
        self.view_button.pack(pady=5)

    def add_grade(self):
        student_id = self.student_id_entry.get()
        course_id = self.course_id_entry.get()
        grade = self.grade_entry.get()
        
        try:
            self.db.add_grade(student_id, course_id, grade)
            messagebox.showinfo("Success", "Grade added successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", str(err))

    def delete_grade(self):
        student_id = self.student_id_entry.get()
        course_id = self.course_id_entry.get()
        
        try:
            self.db.delete_grade(student_id, course_id)
            messagebox.showinfo("Success", "Grade deleted successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", str(err))

    def update_grade(self):
        student_id = self.student_id_entry.get()
        course_id = self.course_id_entry.get()
        grade = self.grade_entry.get()
        
        try:
            self.db.update_grade(student_id, course_id, grade)
            messagebox.showinfo("Success", "Grade updated successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", str(err))

    def view_grades(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("View Grades")
        view_window.geometry("500x300")

        tree = ttk.Treeview(view_window, columns=("Student ID", "Course ID", "Grade"), show='headings')
        tree.heading("Student ID", text="Student ID")
        tree.heading("Course ID", text="Course ID")
        tree.heading("Grade", text="Grade")
        tree.pack(fill=tk.BOTH, expand=True)

        
        scrollbar = ttk.Scrollbar(view_window, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.db.cursor.execute("SELECT student_id, course_id, grade FROM grades")
        records = self.db.cursor.fetchall()

        for student_id, course_id, grade in records:
            tree.insert("", tk.END, values=(student_id, course_id, grade))

        if not records:
            messagebox.showinfo("Info", "No grades found.")

if __name__ == "__main__":
    Login()
