import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Dictionary to map grades to grade points
grade_point_dict = {
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'F': 0.0
}

credit_hour_dict = {
    0.0: 0.0,
    1.0: 1.0, 
    2.0: 2.0, 
    3.0: 3.0, 
    4.0: 4.0
}

course1_dict = {
    'CTU152': 'CTU152',
    'ELC151': 'ELC151',
    'HBU121': 'HBU121',
    'IMC151': 'IMC151',
    'IML152': 'IML152',
    'IML153': 'IML153',
    'IML155': 'IML155'
     
}

def calculate_gpa():
    try:
        total_grade_points = 0
        total_credit_hours = 0

        for i in range(7):  # Assuming there are 7 courses
            credit_hour = credit_hour_vars[i].get()
            grade = grade_vars[i].get()

            if credit_hour and grade:
                grade_points = grade_point_dict.get(grade.upper(), 0)
                total_grade_points += grade_points * float(credit_hour)
                total_credit_hours += float(credit_hour)

        if total_credit_hours > 0:
            gpa = total_grade_points / total_credit_hours
            result_label.config(text=f"Your GPA is: {gpa:.2f}")
            
            message_label.config(text="GPA calculation successful.", fg="green")
        else:
            messagebox.showwarning("Input Error", "Please enter valid credit hours and grades.")
            message_label.config(text="Invalid input. Please check your entries.", fg="red")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for credit hours.")
        message_label.config(text="Invalid input. Please enter numeric values for credit hours.", fg="red")



# Function to insert data into MySQL database
def save_data():
    try:
        student_id = int(student_id_entry.get())
        total_grade_points = 0
        total_credit_hours = 0

        for i, (course_code, course_name) in enumerate(course1_dict.items()):
            credit_hour = float(credit_hour_vars[i].get())
            grade = grade_vars[i].get()

            if credit_hour and grade:
                grade_points = grade_point_dict.get(grade.upper(), 0)
                total_grade_points += grade_points * credit_hour
                total_credit_hours += credit_hour

                # Insert credit hours and grades into the database
                mycursor.execute("INSERT INTO `grade_semester2` (student_id, course_code, credit_hours, grade) VALUES (%s, %s, %s, %s)",
                                 (student_id, course_code, credit_hour, grade))
                mydb.commit()
                #messagebox.showinfo("Data Saved Successfully .")
        if total_credit_hours > 0:
            gpa = total_grade_points / total_credit_hours
            result_label.config(text=f"Your GPA is: {gpa:.2f}")
            message_label.config(text="GPA calculation successful.", fg="green")

            # Update the GPA in the database
            mycursor.execute("UPDATE grade_semester2 SET gpa = %s WHERE student_id = %s", (gpa, student_id))
            mydb.commit()
            #messagebox.showinfo("Data Saved Successfully .")
        else:
            messagebox.showwarning("Input Error", "Please enter valid credit hours and grades.")
            message_label.config(text="Invalid input. Please check your entries.", fg="red")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for credit hours.")
        message_label.config(text="Invalid input. Please enter numeric values for credit hours.", fg="red")


 # ... (existing code)

# Function to update data in MySQL database
def update_data():
    try:
        student_id = int(student_id_entry.get())
        total_grade_points = 0
        total_credit_hours = 0

        for i, (course_code, course_name) in enumerate(course1_dict.items()):
            credit_hour = float(credit_hour_vars[i].get())
            grade = grade_vars[i].get()

            if credit_hour and grade:
                grade_points = grade_point_dict.get(grade.upper(), 0)
                total_grade_points += grade_points * credit_hour
                total_credit_hours += credit_hour

                # Update credit hours and grades in the database
                mycursor.execute("UPDATE grade_semester2 SET credit_hours = %s, grade = %s WHERE student_id = %s AND course_code = %s",
                                 (credit_hour, grade, student_id, course_code))
                mydb.commit()

        if total_credit_hours > 0:
            gpa = total_grade_points / total_credit_hours
            result_label.config(text=f"Your GPA is: {gpa:.2f}")
            message_label.config(text="GPA calculation successful.", fg="green")

            # Update the GPA in the database
            mycursor.execute("UPDATE grade_semester2 SET gpa = %s WHERE student_id = %s", (gpa, student_id))
            mydb.commit()

        else:
            messagebox.showwarning("Input Error", "Please enter valid credit hours and grades.")
            message_label.config(text="Invalid input. Please check your entries.", fg="red")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for credit hours.")
        message_label.config(text="Invalid input. Please enter numeric values for credit hours.", fg="red")


# Function to delete data from MySQL database
def delete_data():
    try:
        student_id = int(student_id_entry.get())

        # Delete all records for the given student_id
        mycursor.execute("DELETE FROM grade_semester2 WHERE student_id = %s", (student_id,))
        mydb.commit()

        result_label.config(text="")
        message_label.config(text="Data deleted successfully.", fg="green")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid numeric value for student ID.")
        message_label.config(text="Invalid input. Please enter a numeric value for student ID.", fg="red")




# GUI interface
root = tk.Tk()
root.title('Student Grade Information Entry Form')

frame = tk.Frame(root)
frame.grid()

# MySQL connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student_1_stop_center"
)

mycursor = mydb.cursor()

# saving student info
grade_info_frame = tk.LabelFrame(frame, text='Student Grade Information (Semester 2)', bg='lightyellow')
grade_info_frame.grid(row=0, column=0, sticky="news", pady=20, padx=20)


# student id
student_id_label = tk.Label(grade_info_frame, text='Student ID', bg='lavender')
student_id_label.grid(row=0, column=0, pady=10, padx=10)
student_id_entry = tk.Entry(grade_info_frame)
student_id_entry.grid(row=0, column=1, pady=10, padx=10)

# Label to display GPA result
result_label = tk.Label(frame, bg='yellow')
result_label.grid(row=1, columnspan=4, pady=10)

# Message Label
message_label = tk.Label(frame, text="")
message_label.grid(row=2, columnspan=4, pady=5)

# Frame to enter credit hours and grades for each course
course_frame = tk.LabelFrame(frame, text="Enter Credit Hours and Grades for Each Course", bg='lightyellow')
course_frame.grid(row=2, column=0, sticky="news", pady=20, padx=20)

# Lists to store credit hour and grade variables
credit_hour_vars = []
grade_vars = []

# Populate the course frame with labels, entry widgets, and dropdowns
for i, (course_code, course_name) in enumerate(course1_dict.items()):
    credit_hour_label = tk.Label(course_frame, text=f"Credit Hours for {course_name}:", bg='lavender')
    credit_hour_label.grid(row=i, column=0, padx=5, pady=5)

    credit_hour_var = tk.StringVar(course_frame)
    credit_hour_dropdown = tk.OptionMenu(course_frame, credit_hour_var, *credit_hour_dict.keys())
    credit_hour_dropdown.grid(row=i, column=1, padx=5, pady=5)

    grade_label = tk.Label(course_frame, text=f"Grade for {course_name}:", bg='lavender')
    grade_label.grid(row=i, column=2, padx=5, pady=5)

    grade_var = tk.StringVar(course_frame)
    grade_dropdown = tk.OptionMenu(course_frame, grade_var, *grade_point_dict.keys())
    grade_dropdown.grid(row=i, column=3, padx=5, pady=5)

    credit_hour_vars.append(credit_hour_var)
    grade_vars.append(grade_var)

# button frame
button_frame = tk.LabelFrame(frame, bg='lightyellow')
button_frame.grid(row=3, column=0, sticky="news", pady=20, padx=20)


# Button to calculate GPA and save data
calculate_button = tk.Button(button_frame, text="Calculate GPA", command=calculate_gpa, bg='lightgrey')
calculate_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

# Save button
save_button = tk.Button(button_frame, text='Save', command=save_data, bg='lightgrey')
save_button.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# Update button
update_button = tk.Button(button_frame, text='Update', command=update_data, bg='lightgrey')
update_button.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

# Delete button
delete_button = tk.Button(button_frame, text='Delete', command=delete_data, bg='lightgrey')
delete_button.grid(row=1, column=3, padx=5, pady=5, sticky="ew")


# Run the Tkinter event loop
root.mainloop()
