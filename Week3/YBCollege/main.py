from repositories import StudentRepo,ClassRepo,CourseRepo,TeacherRepo,AssignmentRepo,GradeRepo
from database import create_table

def class_opertation():
    classRepo=ClassRepo()
    lastrowid=classRepo.add("Master of Software Engineering")
    class_list= classRepo.view_all()
    print(class_list)
    # classRepo.delete(1)

def course_opertation():
    courseRepo=CourseRepo()
    lastrowid=courseRepo.add("Research Method","Research Method aim to teach student about how to write an essay.")
    print(lastrowid)
    rows=courseRepo.search_by_name("Research Method")
    print(rows)
    course_list= courseRepo.view_all()
    print(course_list)
    # courseRepo.delete(1)

def teacher_opertation():
    courseRepo=CourseRepo()
    course_id=courseRepo.check_exist("Research Method")
    if course_id == 0:
        print("Can't find course Research Method!")
        return  
    teacherRepo=TeacherRepo()
    lastrowid=teacherRepo.add("Rina","lecture",course_id)

    rows=teacherRepo.search_by_name("Rina")
    print(rows)

    teacher_list= teacherRepo.view_all()
    print(teacher_list)
    # teacherRepo.delete(1)

def student_opertation():
    classRepo=ClassRepo()
    classid=classRepo.check_exist("Master of Software Engineering")
    if classid == 0:
        print("Can't find class Master of Software Engineering!")
        return  
    studentRepo=StudentRepo()
    lastrowid=studentRepo.add("Emma","888.gmail.com","8080709",classid,"emma_account","888abc")
    rows=studentRepo.search_by_name("Emma")
    print(rows)
    index=studentRepo.check_exist("emma_account")    
    print(index)
    student_list= studentRepo.view_all()
    print(student_list)
    studentRepo.delete(1)

def assignment_opertation():
    courseRepo=CourseRepo()
    course_id=courseRepo.check_exist("Research Method")
    if course_id == 0:
        print("Can't find course Research Method!")
        return       
    assignmentRepo=AssignmentRepo()
    lastrowid=assignmentRepo.add("SWE_Assignment_1","important","15/9/2025",course_id)
    rows=assignmentRepo.search_by_title("SWE_Assignment_1")
    print(rows)

    # assignmentRepo.delete(1)

def grade_opertation():
    assignmentRepo=AssignmentRepo()
    assignment_id=assignmentRepo.check_exist("SWE_Assignment_1")
    if assignment_id == 0:
        print("Can't find assignment SWE_Assignment_1!")
        return
    studentRepo=StudentRepo()
    student_id=studentRepo.check_exist("Emma")
    if student_id == 0:
        print("Can't find student Emma!")
        return    
    gradeRepo=GradeRepo()
    lastrowid=gradeRepo.add(30,"A+",student_id,assignment_id)
    print(lastrowid)
   # gradeRepo.delete(1)

def main():
    create_table()
    class_opertation()
    course_opertation()
    teacher_opertation()
    student_opertation()
    assignment_opertation()
    grade_opertation()


    

if __name__ == "__main__":
    main()

