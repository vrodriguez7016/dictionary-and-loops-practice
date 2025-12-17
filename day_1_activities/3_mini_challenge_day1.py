# Project Prompt:  Vanessa Rodriguez, Ayelen Cardenas

# You are hired to build a Student Lookup Tool for a school front office. The secretary must be able to:

    # Enter a student’s full name

    # Instantly see:

            # CPS ID

            # Homeroom

            # Grade Level

            # Primary Email

            # Students must:

            # Describe the search process





## be able to add new data
# Your program must allow the secretary to ADD a brand new student
# into the system while the program is running.

# Your job is to let the secretary type in a new student just like filling out a registration form.
# Once the form is complete, your program must turn that information into a dictionary and add it to the main list of students.
# If the student already exists (same CPS ID), your program must block the entry to prevent duplicates.

# The program should:
    # 1. Ask the user for the following information: 
    #    - CPS ID
    #    - First Name
    #    - Last Name
    #    - Middle Name
    #    - Homeroom
    #    - Grade Level
    #    - Primary Email
    #    - Secondary Email

import student_data 
students = student_data.students

key_to_extract = 'Combo,Name'
student_list = [d[key_to_extract] for d in students if key_to_extract in d]

search_student = input("Type full name of student you are searching for in 'last name', 'first name' format. If you don't wish to search for a student, type 'quit': ")
if not search_student == "quit":
    for i in range(len(student_list)):
        if search_student==student_list[i]:
            print(students[i])
        else: 
            continue


print("Student Registration Form")
print("-"*30)
cpsid = input("What is your CPSID?: ")

while not cpsid or len(cpsid)<8:
    if not cpsid:
        print("Please type in your CPSID")
    elif len(cpsid)<8:
        print("CPSID is not at least 8 digits.")
    cpsid = input("What is your CPSID?: ")


first_name = input("What is your first name?: ")
while not first_name:
    print("Please enter your first name")
    first_name = input("What is your first name?: ")
    
        
last_name = input("What is your last name?: ")
while not last_name:
    print("Please enter your last name")
    last_name = input("What is your last name?: ")


middle_name = input("What is your middle name?: ")
while not middle_name:
    print("Please enter your middle name")
    middle_name = input("What is your middle name?: ")


homeroom = input("What is your homeroom?: ")
while not homeroom:
    print("Please enter your homeroom")
    homeroom = input("What is your homeroom?: ")


grade_level = input("What is your grade level?: ")
while not grade_level:
    print("Please enter your grade level")
    grade_level = input("What is your grade level?: ")

        
primary_email = input("What is your first email?: ")
while not primary_email:
    print("Please enter your first email")
    primary_email = input("What is your first email?: ")


secondary_email = input("What is your second email?: ")
while not secondary_email:
    print("Please enter your second email")
    secondary_email = input("What is your second email?: ")


# 2. Combine the First and Last name into this format:
    #    "Last, First"  
combo_name = last_name, first_name
# 3. Store all of the new information into ONE dictionary 
    #    that matches the structure of the existing student data.
# 4. Add (append) that new dictionary into the main students list.
new_student = {"CPSID": {cpsid},
                  "Combo,Name": {combo_name},
                   "LName": {last_name},
                   "FName": {first_name},
                   "MName": {middle_name},
                   "HR": {homeroom},
                   "GL": {grade_level},
                   "Email": {primary_email, secondary_email}}
students.append(new_student)

key_to_extract1 = 'CPSID'
id_list = [d[key_to_extract1] for d in students if key_to_extract1 in d]
res = False
for i in range(len(id_list)):
        if cpsid == id_list[i]:
            print("Error: CPS ID is already taken.")
            print("Unregistering new student.")
            students.pop(-1)
            res = True
        else: 
            continue


if res == False:
    print(f"Registration confirmed: Student {combo_name}, CPSID: {cpsid}, HR: {homeroom}, GL: {grade_level}, Email: {primary_email, secondary_email} ")


# 5. After adding the student, the program must:
    #    - Print a confirmation message
    #    - Print the total number of students in the system
    #    - Print the newly added student record

total_students = len(student_list)
print(f"Total number of students: {total_students}")

students_dict = {
    1: {"name": "Vicky Xavier", "grade": "B"},
    2: {"name": "Liam Thomas", "grade": "A"}
}
new_student_id = 3
new_student_data = {"name": "Quinn Clark", "grade": "C"}

students_dict[new_student_id] = student_data
print(f"Newly added student (via variable): {new_student_data}")

# 6. The program must NOT delete or overwrite any existing students.

# 7. If the CPS ID already exists in the system:
        #    - Do NOT add the student
        #    - Display an error message saying the CPS ID is already taken

