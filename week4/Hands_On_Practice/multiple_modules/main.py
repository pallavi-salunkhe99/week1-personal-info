# Controls program flow

import student_input
import student_calculate
import student_display

name, marks = student_input.get_student()
grade = student_calculate.calculate_grade(marks)
student_display.show_result(name, marks, grade)
