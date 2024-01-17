import tkinter
from tkinter import ttk
import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="student_1_stop_center"
 )

cursor = mydb.cursor() 

def enter_data():
    Stu_ID = student_id_entry.get()
    Stu_DOB = student_dob_entry.get()
    Stu_Title = student_title_combobox.get()
    Stu_FName = student_first_name_entry.get()
    Stu_LName = student_last_name_entry.get()
    Stu_Age = student_age_spinbox.get()
    Stu_Gender = student_gender_combobox.get()
    Stu_Level_of_Study = student_study_level_combobox.get()
    Stu_Sem = student_semester_combobox.get()
    Stu_Group = student_group_combobox.get()
    Stu_Program = stu_program_combobox.get()
    Stu_Faculty = student_faculty_combobox.get()
    Stu_Institution = student_institution_combobox.get()
    Stu_Address = student_address_combobox.get()
    Stu_Phone = student_phone_entry.get()
    

    sql = 'INSERT INTO `student` ( Stu_Program, Stu_ID, Stu_DOB, Stu_Title, Stu_FName, Stu_LName, Stu_Age, Stu_Gender, Stu_Level_of_Study, Stu_Sem, Stu_Group, Stu_Faculty, Stu_Institution, Stu_Address, Stu_Phone ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )'

    val = (Stu_Program, Stu_ID, Stu_DOB, Stu_Title, Stu_FName, Stu_LName, Stu_Age, Stu_Gender, Stu_Level_of_Study, Stu_Sem, Stu_Group, Stu_Faculty, Stu_Institution, Stu_Address, Stu_Phone)
    
    try:
        cursor.execute(sql, val)
        mydb.commit()
        print('Data saved successfully.')

    except Exception as e:
       print(f'Error saving data: {e}')

def update_data():
    Stu_ID = student_id_entry.get()
    Stu_Title = student_title_combobox.get()
    Stu_Age = student_age_spinbox.get()
    Stu_Sem = student_semester_combobox.get()
    Stu_Group = student_group_combobox.get()
    Stu_Address = student_address_combobox.get()
    Stu_Phone = student_phone_entry.get()
     # SQL query to update data
    sql = f'''
    UPDATE student
    SET
        Stu_Title = %s,
        Stu_Age = %s,
        Stu_Sem = %s,
        Stu_Group = %s,
        Stu_Address = %s,
        Stu_Phone = %s
    WHERE Stu_ID = %s;
    '''

    val = (Stu_Title, Stu_Age, Stu_Sem, Stu_Group , Stu_Address, Stu_Phone, Stu_ID)

    try:
        cursor.execute(sql, val)
        mydb.commit()
        print('Data updated successfully.')

    except Exception as e:
       print(f'Error updating data: {e}')

def delete_data():
    Stu_ID = student_id_entry.get()
    
     # SQL query to delete data
    sql = f'''
    DELETE FROM student
    WHERE Stu_ID = %s;
    '''

    val = (Stu_ID)

  
    try:
        cursor.execute(sql, val)
        mydb.commit()
        print('Data has been deleted.')

    except Exception as e:
        print(f'Error deleting data: {e}')    

def update_groups(event):
    selected_semester = student_semester_combobox.get()

    if selected_semester == '1':
        student_groups = ['KCDIM1441A', 'KCDIM1441B', 'KCDIM1441C', 'KCDIM1441D', 'KCDIM1441E', 'KCDIM1441F']
    elif selected_semester == '2':
        student_groups = ['KCDIM1442A', 'KCDIM1442B', 'KCDIM1442C', 'KCDIM1442D', 'KCDIM1442E', 'KCDIM1441F']
    elif selected_semester == '3':
        student_groups = ['KCDIM1443A', 'KCDIM1443B', 'KCDIM1443C', 'KCDIM1443D', 'KCDIM1443E', 'KCDIM1443F']
    elif selected_semester == '4':
        student_groups = ['KCDIM1444A', 'KCDIM1444B', 'KCDIM1444C', 'KCDIM1444D', 'KCDIM1444E', 'KCDIM1444F']
    elif selected_semester == '5':
        student_groups = ['KCDIM1445A', 'KCDIM1445B', 'KCDIM1445C', 'KCDIM1445D', 'KCDIM1445E', 'KCDIM1445F']

    student_group_combobox['values'] = student_groups
    student_group_combobox.current(0)


#gui
root = tkinter.Tk()
root.title('Student Information Entry Form')

frame = tkinter.Frame(root, bg='lavender')
frame.pack()


#saving student info
student_info_frame = tkinter.LabelFrame(frame,text = 'Student Information', bg= 'lightyellow' )
student_info_frame.grid(row = 0 , column = 0, padx = 50, pady = 50)

#program
stu_program = tkinter.Label(student_info_frame , text = 'Program:', bg='lavender')
stu_program.grid(row = 0, column = 0, pady = 20, padx = 20 )
stu_program_combobox = ttk.Combobox(student_info_frame, values ='CDIM144')
stu_program_combobox.grid(row = 0, column = 1, pady = 20, padx = 20)

#student id
student_id_label = tkinter.Label(student_info_frame, text = 'Student ID:', bg='lavender')
student_id_label.grid(row = 0, column = 2, pady = 20, padx = 20)
student_id_entry = tkinter.Entry(student_info_frame)
student_id_entry.grid(row = 0, column = 3, pady = 20, padx = 20)

#student date of birth
student_dob_label = tkinter.Label(student_info_frame, text = 'Date of Birth (YYYY/MM/DD):', bg='lavender')
student_dob_label.grid(row = 0, column = 4, pady = 20, padx = 20)
student_dob_entry = tkinter.Entry(student_info_frame)
student_dob_entry.grid(row = 0, column = 5, pady = 20, padx = 20)

#student title
student_title_label = tkinter.Label(student_info_frame, text = 'Title:', bg='lavender')
student_title_label.grid(row = 1, column = 0, pady = 20, padx = 20)
student_title_entry = tkinter.Entry(student_info_frame)
student_title_combobox = ttk.Combobox(student_info_frame, values =['','Mr.', 'Ms.', 'Mrs.', 'Dr.'])
student_title_combobox.grid(row = 1, column = 1, pady = 20, padx = 20)

#student first name
first_name_label = tkinter.Label(student_info_frame, text = 'First Name:', bg='lavender')
first_name_label.grid(row = 1, column = 2, pady = 20, padx = 20)
student_first_name_entry = tkinter.Entry(student_info_frame)
student_first_name_entry.grid(row = 1, column = 3, pady = 20, padx = 20)

#student last name
last_name_label = tkinter.Label(student_info_frame, text = 'Last Name:', bg='lavender')
last_name_label.grid(row = 1, column = 4, pady = 20, padx = 20)
student_last_name_entry = tkinter.Entry(student_info_frame)
student_last_name_entry.grid(row = 1, column = 5, pady = 20, padx = 20)

#student age
student_age_label = tkinter.Label(student_info_frame, text = 'Age (Year):', bg='lavender')
student_age_label.grid(row = 2, column = 0, pady = 20, padx = 20)
student_age_spinbox = tkinter.Spinbox(student_info_frame, from_= 18, to = 45)
student_age_spinbox.grid(row = 2, column = 1, pady = 20, padx = 20)

#student gender
student_gender_label = tkinter.Label(student_info_frame, text = 'Gender:', bg='lavender')
student_gender_label.grid(row = 2, column = 2, pady = 20, padx = 20)
student_gender_combobox = ttk.Combobox(student_info_frame, values =['Male', 'Female'])
student_gender_combobox.grid(row = 2, column = 3, pady = 20, padx = 20)

#student level of study
student_study_level_label = tkinter.Label(student_info_frame, text = 'Level of Study:', bg='lavender')
student_study_level_label.grid(row = 2 , column = 4, pady = 20, padx = 20)
student_study_level_combobox = ttk.Combobox(student_info_frame, values =['Diploma'])
student_study_level_combobox.grid(row = 2, column =5, pady = 20, padx = 20)

#student semester
student_semester_label = tkinter.Label(student_info_frame, text='Semester:', bg='lavender')
student_semester_label.grid(row= 3, column= 0, pady= 20, padx = 20)
student_semester_combobox = ttk.Combobox(student_info_frame, values=['1', '2', '3', '4', '5'])
student_semester_combobox.grid(row= 3, column= 1, pady= 20, padx = 20)
student_semester_combobox.bind("<<ComboboxSelected>>", update_groups)

#student group
student_group_label = tkinter.Label(student_info_frame, text='Group:', bg='lavender')
student_group_label.grid(row= 3, column= 2, pady= 20, padx= 20)
student_groups = ['KCDIM1441A', 'KCDIM1441B', 'KCDIM1441C', 'KCDIM1441D', 'KCDIM1441E']
student_group_combobox = ttk.Combobox(student_info_frame, values=student_groups)
student_group_combobox.grid(row= 3, column= 3, pady= 20, padx= 20)

        
#update groups
def update_groups(event):
        selected_semester = student_semester_combobox.get()

        # Update groups based on the selected semester
        if selected_semester == '1':
            student_groups = ['KCDIM1441A', 'KCDIM1441B', 'KCDIM1441C', 'KCDIM1441D', 'KCDIM1441E','KCDIM1441F']
        # Add more conditions for other semesters
        if selected_semester == '2':
            student_groups = ['KCDIM1442A', 'KCDIM1442B', 'KCDIM1442C', 'KCDIM1442D', 'KCDIM1442E','KCDIM1441F']

        if selected_semester == '3':
            student_groups = ['KCDIM1443A', 'KCDIM1443B', 'KCDIM1443C', 'KCDIM1443D', 'KCDIM1443E','KCDIM1443F']

        if selected_semester == '4':
            student_groups = ['KCDIM1444A', 'KCDIM1444B', 'KCDIM1444C', 'KCDIM1444D', 'KCDIM1444E','KCDIM1444F']

        else: #selected_semester == '5':
            student_groups = ['KCDIM1445A', 'KCDIM1445B', 'KCDIM1445C', 'KCDIM1445D', 'KCDIM1445E','KCDIM1445F']

        # Update the values in the group combobox
        student_group_combobox['values'] = student_groups
        student_group_combobox.current(0)  # Set the default selected group
        
        
#student faculty
student_faculty_label = tkinter.Label(student_info_frame, text = 'Faculty:', bg='lavender')
student_faculty_label.grid(row = 3, column = 4, pady = 20, padx = 20)
student_faculty_combobox = ttk.Combobox(student_info_frame, values =['College of Computing, Information and Mathematics'])
student_faculty_combobox.grid(row = 3, column = 5, pady = 20, padx = 20)

#student institution
student_institution_label = tkinter.Label(student_info_frame, text = 'Institution:', bg='lavender')
student_institution_label.grid(row = 4, column = 0, pady = 20, padx = 20)
student_institution_combobox = ttk.Combobox(student_info_frame, values = ['UiTM Kedah']) 
student_institution_combobox.grid(row = 4, column = 1, pady = 20, padx = 20)

#student address
student_address_label = tkinter.Label(student_info_frame, text = 'Address:', bg='lavender')
student_address_label.grid(row = 4, column = 2, pady = 20, padx = 20)
student_address_combobox = ttk.Combobox(student_info_frame, values = ['Kedah', 'Pahang', 'Melaka', 'Sabah', 'Sarawak', 'Kelantan', 'Perak', 'Perlis', 'Selangor', 'Melaka', 'Pulau Pinang', 'Kuala Lumpur', 'Negeri Sembilan', 'Johor', 'Terengganu', 'Putrajaya'])
student_address_combobox.grid(row = 4, column = 3, pady = 20, padx = 20)

#student phone number
student_phone_label = tkinter.Label(student_info_frame, text = 'Phone Number (Without space):', bg='lavender')
student_phone_label.grid(row = 4, column = 4, pady = 20, padx = 20)
student_phone_entry = tkinter.Entry(student_info_frame)
student_phone_entry.grid(row = 4, column = 5, pady = 20, padx = 20)

#accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions", bg='lightyellow')
terms_frame.grid(row=5, column=0, sticky="news", padx= 10, pady= 10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text= "I accept the terms and conditions.",
variable=accept_var, onvalue="Accepted", offvalue="Not Accepted", bg='lavender')
terms_check.grid(row=0, column=0, pady = 10, padx = 10)

button_frame = tkinter.LabelFrame(frame, bg='lightyellow')
button_frame.grid(row=6, column=0, sticky="news", padx= 10, pady= 10)
#save button
save_button = tkinter.Button(button_frame, text = 'Save data', command=enter_data, bg='lightgrey')
save_button.grid(row = 0, column = 0, pady = 10, padx = 10)

#update button
update_button = tkinter.Button(button_frame, text='Update Data', command=update_data, bg='lightgrey')
update_button.grid(row = 0, column = 1, pady = 10, padx = 10)

#delete button
delete_button = tkinter.Button(button_frame, text="Delete Data", command=delete_data, bg='lightgrey')
delete_button.grid(row = 0, column = 2, pady = 10, padx = 10)


root.mainloop()

