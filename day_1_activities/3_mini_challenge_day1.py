# Project Prompt:

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
    # 1. Ask the user for the following information: (Vanessa)
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

cpsid = input("What is your CPSID?: ")
while cpsid == " " or len(cpsid)<8:
    print("Please type in your CPSID")
    cpsid = input("What is your CPSID?: ")


first_name = input("What is your first name?: ")
while first_name == " ":
    print("Please enter your first name")
    first_name = input("What is your first name?: ")
    
        
last_name = input("What is your last name?: ")
while last_name == " ":
    print("Please enter your last name")
    last_name = input("What is your last name?: ")


middle_name = input("What is your middle name?: ")
while middle_name == " ":
    print("Please enter your middle name")
    middle_name = input("What is your middle name?: ")


homeroom = input("What is your homeroom?: ")
while homeroom == " ":
    print("Please enter your homeroom")
    homeroom = input("What is your homeroom?: ")


grade_level = input("What is your grade level?: ")
while grade_level == " ":
    print("Please enter your grade level")
    grade_level = input("What is your grade level?: ")

        
primary_email = input("What is your first email?: ")
while primary_email == " ":
    print("Please enter your first email")
    primary_email = input("What is your first email?: ")


secondary_email = input("What is your second email?: ")
while secondary_email == " ":
    print("Please enter your second email")
    secondary_email = input("What is your second email?: ")


# 2. Combine the First and Last name into this format:
    #    "Last, First"  
combo_name = last_name, first_name
# 3. Store all of the new information into ONE dictionary 
    #    that matches the structure of the existing student data.
# 4. Add (append) that new dictionary into the main students list.
new_student = ({"CPSID": {cpsid},
                "Combo,Name": {combo_name},
                "LName": {last_name},
                "FName": {first_name},
                "MName": {middle_name},
                "HR": {homeroom},
                "GL": {grade_level},
                "Email": {primary_email, secondary_email}})
students.append(new_student)


# 5. After adding the student, the program must:
    #    - Print a confirmation message
    #    - Print the total number of students in the system
    #    - Print the newly added student record



# 6. The program must NOT delete or overwrite any existing students.

# 7. If the CPS ID already exists in the system:
        #    - Do NOT add the student
        #    - Display an error message saying the CPS ID is already taken

id_list = [ ]
for student in students.values():
    id_list.append('CPSID')
for i in range(len(students)):
    if cpsid in id_list:
        print("Error: CPS ID is already taken.")
        print("Unregistering new student.")
    else:
        continue

