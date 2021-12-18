# Program GRADES
def create_grades(student_name: str):
    """Creates a dictionary of a classe."""
    student_name = {}
    student_name['n1'] = float(input("Enter the grade 1: "))
    student_name['n2'] = float(input("Enter the grade 1: "))
    student_name['n3'] = float(input("Enter the grade 1: "))
    student_name['n4'] = float(input("Enter the grade 1: "))
    average = 0
    for v in student_name.values():
        average = v + average
    final_average = average/4
    student_name['final_a'] = final_average
    return student_name

def add_student(class_list: list):
    """Add student to a list."""
    answer = ''
    while answer.lower() != 'n':
        enter_name = input("Enter a name: ")
        new_student = create_grades(enter_name)
        class_list.append(new_student)
        answer = input("Do you want to add a student? [Y]es or [N]o?: ")
    print("Ok, then let's finished the procedure!")

def grade_analysis(class_list: list):
    """Analysis if a student succeed or don't."""
    for student in class_list:
        if student['final_a'] > 5:
            print(f"The student {student} pass!")
        else:
            print(f"The student {student} fails!")

# MAIN PROGRAM
high_school_class = []
add_student(high_school_class)
grade_analysis(high_school_class)
