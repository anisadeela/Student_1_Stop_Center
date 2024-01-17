import tkinter as tk
from tkinter import ttk
import mysql.connector

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student_1_stop_center"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

class CourseGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Course Information")

        # Set pastel color scheme
        bg_color = "#F4E8D9"  # Pastel yellow background
        text_color = "#333333"  # Dark gray text color
        button_color = "#D08E9B"  # Pastel pink button color
        label_font = ('Helvetica', 10)
        button_font = ('Helvetica', 12)

        # Set background color
        self.master.configure(bg=bg_color)

        # Initialize variables
        self.level_of_study_var = tk.StringVar()
        self.program_var = tk.StringVar()
        self.semester_var = tk.StringVar()

        self.create_widgets(bg_color, text_color, label_font, button_color, button_font)

    def create_widgets(self, bg_color, text_color, label_font, button_color, button_font):
        # Level of Study dropdown
        tk.Label(self.master, text="Level of Study:", bg=bg_color, fg=text_color, font=label_font).grid(row=0, column=0, pady=5, sticky='w')
        level_options = ["Diploma"]
        level_dropdown = ttk.Combobox(self.master, textvariable=self.level_of_study_var, values=level_options, state="readonly")
        level_dropdown.grid(row=0, column=1, pady=5, sticky='w')
        level_dropdown.set(level_options[0])  # Set default value

        # Program dropdown
        tk.Label(self.master, text="Program:", bg=bg_color, fg=text_color, font=label_font).grid(row=1, column=0, pady=5, sticky='w')
        program_options = ["CDIM144"]
        program_dropdown = ttk.Combobox(self.master, textvariable=self.program_var, values=program_options, state="readonly")
        program_dropdown.grid(row=1, column=1, pady=5, sticky='w')
        program_dropdown.set(program_options[0])  # Set default value

        # Semester dropdown
        tk.Label(self.master, text="Semester:", bg=bg_color, fg=text_color, font=label_font).grid(row=2, column=0, pady=5, sticky='w')
        semester_options = ["1", "2", "3", "4", "5"]
        semester_dropdown = ttk.Combobox(self.master, textvariable=self.semester_var, values=semester_options, state="readonly")
        semester_dropdown.grid(row=2, column=1, pady=5, sticky='w')
        semester_dropdown.set(semester_options[0])  # Set default value

        # Button to display course information
        tk.Button(self.master, text="Show Course Info", command=self.show_course_info, bg=button_color, fg='white', font=button_font).grid(row=3, column=0, columnspan=2, pady=10)

        # Create a Treeview widget for displaying the course information in a table
        self.tree = ttk.Treeview(self.master, columns=("Code", "Name", "Lecturer", "Credit Hour"), show="headings")
        self.tree.grid(row=4, column=0, columnspan=2, pady=10, sticky='nsew')

        # Configure column headings
        self.tree.heading("Code", text="Code")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Lecturer", text="Lecturer")
        self.tree.heading("Credit Hour", text="Credit Hour")

        # Configure column widths
        self.tree.column("Code", width=80)
        self.tree.column("Name", width=200)
        self.tree.column("Lecturer", width=150)
        self.tree.column("Credit Hour", width=100)

        # Configure vertical scrollbar
        vsb = ttk.Scrollbar(self.master, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        vsb.grid(row=3, column=2, sticky='ns')

        # Label for displaying total credit hours
        self.total_credit_label = tk.Label(self.master, text="", font=('Helvetica', 12, 'bold'), bg=bg_color, fg=text_color)
        self.total_credit_label.grid(row=5, column=0, columnspan=2, pady=10, sticky='w')

    def show_course_info(self):
        # Retrieve selected values
        level_of_study = self.level_of_study_var.get()
        program = self.program_var.get()
        semester = self.semester_var.get()

        # Get course information based on the selected semester
        courses = self.get_courses_for_semester(semester)

        # Insert data into the database and display course information in the table
        self.insert_and_display_course_info(level_of_study, program, semester, courses)

    def insert_and_display_course_info(self, level_of_study, program, semester, courses):
        # Set your desired colors and font
        bg_color = "lightblue"  # Example color, you can replace it with your preferred color
        text_color = "black"    # Example color, you can replace it with your preferred color
        label_font = ('Helvetica', 10, 'bold')  # Example font, you can adjust it as needed

        # Clear previous results
        self.tree.delete(*self.tree.get_children())

        # Insert data into the database
        if courses:
            for course in courses:
                self.insert_into_database(level_of_study, program, semester, course["code"], course["name"], course["lecturer"], course["credit_hour"])

            # Display course information in the table
            total_credit_hours = 0
            for course in courses:
                self.tree.insert("", "end", values=(course["code"], course["name"], course["lecturer"], course["credit_hour"]))
                total_credit_hours += course["credit_hour"]

            # Display total credit hours
            self.total_credit_label.config(text=f"Total Credit Hours: {total_credit_hours}")

    def insert_into_database(self, level_of_study, program, semester, subject_code, subject_name, lecturer_name, credit_hour):
        # Insert subject details into the 'course' table
        sql_course = "INSERT INTO `course` (Level_of_Study, Program, Semester, Subject_Code, Subject_Name, Lecturer_Name, Credit_Hour) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val_course = (level_of_study, program, semester, subject_code, subject_name, lecturer_name, credit_hour)
        mycursor.execute(sql_course, val_course)
        mydb.commit()

    def get_courses_for_semester(self, semester):
        # You can customize this function to return course information based on the selected semester
        course_info = {
            "1": [
                {"code": "CTU101", "name": "FUNDAMENTALS OF ISLAM", "lecturer": "USTAZ AFIQ BIN MUHAMMAD", "credit_hour": 2.0},
                {"code": "ELC121", "name": "INTEGRATED LANGUAGE SKILLS I", "lecturer": "MADAM HANI BINTI ZULKIFLI", "credit_hour": 3.0},
                {"code": "HBU111", "name": "NATIONAL KESATRIA I", "lecturer": "TUAN SABREE BIN MAHMOOD", "credit_hour": 1.0},
                {"code": "IMC111", "name": "INTRODUCTION TO INFORMATION SKILLS", "lecturer": "DR. SHAHIRA BINTI YUSOF", "credit_hour": 3.0},
                {"code": "IMC112", "name": "INTRODUCTION TO INFORMATION MANAGEMENT", "lecturer": "SIR AHMAD BIN NAUFAL", "credit_hour": 3.0},
                {"code": "IMC113", "name": "INFORMATION AND COMMUNICATION TECHNOLOGY APPLICATION", "lecturer": "MISS NADIA BINTI ISHAK", "credit_hour": 3.0},
                {"code": "MGT162", "name": "FUNDAMENTALS OF MANAGEMENT", "lecturer": "DR. KARMILA BINTI ZAKARIA", "credit_hour": 3.0},
                {"code": "UED102", "name": "STUDY SKILLS", "lecturer": "MADAM DAMIA BINTI NOH", "credit_hour": 0.0},
            ],
            "2": [
                {"code": "CTU152", "name": "VALUES AND CIVILIZATION", "lecturer": "USTAZAH SAFIYAH BINTI SYUKOR", "credit_hour": 2.0},
                {"code": "ELC151", "name": "INTEGRATED LANGUAGE SKILLS II", "lecturer": "MADAM WARDINA BINTI ISKANDAR", "credit_hour": 3.0},
                {"code": "HBU121", "name": "NATIONAL KESATRIA II", "lecturer": "TUAN AHMAD BIN TALIB", "credit_hour": 1.0},
                {"code": "IMC151", "name": "ORGANIZATION AND ACCESS TO INFORMATION", "lecturer": "DR. AZLINA BINTI YAHYA", "credit_hour": 3.0},
                {"code": "IML152", "name": "INTRODUCTION TO LIBRARY MANAGEMENT", "lecturer": "PROF. DR. KHADIJAH BINTI FATEH", "credit_hour": 4.0},
                {"code": "IML153", "name": "FUNDAMENTAL OF DATA MANAGEMENT", "lecturer": "DR. KHALID BIN JAAFAR", "credit_hour": 4.0},
                {"code": "IML155", "name": "COMMUNICATION SKILLS FOR INFORMATION PROFESSIONAL", "lecturer": "MADAM HANANI BINTI HAREES", "credit_hour": 3.0},
            ],
            "3": [
                {"code": "CTU264", "name": "ISLAMIC INFORMATION MANAGEMENT", "lecturer": "USTAZ DANIAL BIN ZUHAIR", "credit_hour": 2.0},
                {"code": "ELC231", "name": "INTEGRATED LANGUAGE SKILLS III", "lecturer": "SIR FARIS BIN FURQAN", "credit_hour": 3.0},
                {"code": "HBU131", "name": "NATIONAL KESATRIA III", "lecturer": "PUAN DHIA BINTI LOKMAN", "credit_hour": 1.0},
                {"code": "IML206", "name": "DIGITAL PRESERVATION IN LIBRARY ENVIRONMENT", "lecturer": "SIR HAFIZ BIN SHAMSUL", "credit_hour": 3.0},
                {"code": "IML207", "name": "INFORMATION SECURITY FOR LIBRARIES", "lecturer": "MISS FARHAH BINTI FARHAN", "credit_hour": 2.0},
                {"code": "IML208", "name": "PROGRAMMING FOR LIBRARIES", "lecturer": "SIR NOAH BIN MUHAMMAD NAUFAL", "credit_hour": 4.0},
                {"code": "IML209", "name": "DESCRIPTIVE CATALOGING", "lecturer": "MADAM ZALIKHA BINTI SAAD", "credit_hour": 3.0},
            ],
            "4": [
                {"code": "IMC258", "name": "METADATA DEVELOPMENT IN INFORMATION ENVIRONMENT", "lecturer": "DR. FAREHAH BINTI SULAIMAN", "credit_hour": 3.0},
                {"code": "IML254", "name": "INTRODUCTION TO WEB CONTENT DEVELOPMENT", "lecturer": "PROF. DR. RIZMAN BIN SHAHRIL", "credit_hour": 4.0},
                {"code": "IML255", "name": "SUBJECT CATALOGING AND CLASSIFICATION", "lecturer": "MADAM HUMAIRAH BINTI ZAHID", "credit_hour": 3.0},
                {"code": "IML256", "name": "MULTIMEDIA AND DIGITAL PUBLISHING IN LIBRARIES", "lecturer": "SIR HARRAZ BIN MALEEQ", "credit_hour": 4.0},
                {"code": "IML257", "name": "LIBRARIES AND CUSTOMERS", "lecturer": "MADAM AMANI BINTI ROSLAN", "credit_hour": 3.0},
            ],
            "5": [
                {"code": "ENT300", "name": "FUNDAMENTALS OF ENTREPRENEURSHIP", "lecturer": "MADAM RAHIMAH BINTI YUSOF", "credit_hour": 3.0},
                {"code": "IML301", "name": "LIBRARY OUTREACH", "lecturer": "MISS SYAHIDA BINTI GHAZALI", "credit_hour": 4.0},
                {"code": "IML302", "name": "DIGITAL REFERENCE AND INFORMATION ANALYTICS", "lecturer": "DR. SYAFIQ BIN AHMAD", "credit_hour": 3.0},
                {"code": "IML303", "name": "INNOVATION IN LIBRARIES", "lecturer": "DR. HAKIM BIN MUHAMMAD SAMAD", "credit_hour": 3.0},
                {"code": "IML310", "name": "LIBRARY FIELDWORKS", "lecturer": "PROF. DR. ANNISA BINTI ABDUL MANAF", "credit_hour": 4.0},
            ],
        }

        return course_info.get(semester, [])

if __name__ == "__main__":
    root = tk.Tk()
    app = CourseGUI(root)
    root.mainloop()
