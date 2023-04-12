# Luke Psyhogios, April 25th 2022, Section 001, Assignment 7, Problem #0: CS Rosters
# Create path
import os
wd = os.getcwd()
path = wd + '/'

# Create and read course data
courses = open(path + 'class_data.txt','r')
course_data = courses.read()
courses.close()



# Create and read enrollment data
enr = open(path + 'enrollment_data.txt','r')
enr_data = enr.read()
enr.close()

# Create list of course and enrollment data
course_list = course_data.split('\n')
enr_list = enr_data.split('\n')

# Empty lists for IDs and titles
ids = []
titles = []
# Populate the lists
for i in course_list:
    course = i.split(',')
    ids.append(course[0])
    titles.append(course[1])

# Display top of program
print('NYU Computer Science Regestration System')
# Ask user for input
course_id = input('Enter a course ID (i.e. CS0002, CS0004): ')
if course_id in ids:
    # Find index
    id_index = ids.index(course_id)
    course_name = titles[id_index]
    # Display class title
    print('The title of this class is:', course_name)
    students_in_course = []
    # Populate the empty list with student names
    for student in enr_list:
        if course_id in student:
            full_name = student.split(',',1)
            name = full_name[1]
            students_in_course.append(name)
    # Get the number of students in the course
    num_students = len(students_in_course)
    # Display students and number of students
    print('These are', num_students, 'students in the course')
    students_in_course.sort()
    # Sort by 
    for s in students_in_course:
        split_name = s.split(',')
        first_name = split_name[1]
        last_name = split_name[0]
        print('*',first_name,last_name)
# If the course_id is not in the id list then end program
else:
    print('Cannot find this course')
