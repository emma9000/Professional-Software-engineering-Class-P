The YB College database is designed to support student management, teacher management, and course management.
It should include entities such as students, teachers, courses, class, and a test/grade system.
Every student needs to join a class, attend the tests, and then receive grades for their performance.
A semester management system is also required, in which students are associated with a specific semester.
Each teacher has a job position as their title, and they are associated with a specific class.

## Student

id
name
email
phone
classid
account
password

## teacher

id
name
title
courseId

## course

Id
name
detials

## teacher_students

id
teacherId
studentId

## student_course

id
studentId
courseid

## class

id
name

## assignment

id
name
courseid
datetime

## grade

id
assignmentid
studentid
grade

![alt text](image-2.png)
