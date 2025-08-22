from database import create_connection
import sqlite3

class StudentRepo:   
        
    def add(self,name, email, phone, classid, account, password)->int:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO student (name, email, phone, classid, account, password ) VALUES (?, ?, ?, ?, ?, ?)", (name, email, phone, classid,account, password ))
        conn.commit()
        print(" student added successfully.")
        conn.close()
        return cursor.lastrowid
    
    def delete(self, id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM student WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        print("student deleted.")        
        
    def check_exist(self,account)->int:
        is_exist= 0
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student WHERE account = ? ORDER BY id LIMIT ?", (account,1))
        row = cursor.fetchone()
        conn.close()
        if row is not None:
            is_exist=row[0]
        
        return is_exist

    def view_all(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student")
        rows = cursor.fetchall()
        conn.close()
        return rows
    
    def search_by_name(self,name):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student WHERE name LIKE ?", ('%' + name + '%',))
        rows = cursor.fetchall()
        conn.close()
        return rows
    
class ClassRepo:   
        
    def add(self,name)->int:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO class (name) VALUES (?)", (name, ))
        conn.commit()
        print(" class added successfully.")
        conn.close()
        return cursor.lastrowid
    
    def delete(self, id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM class WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        print("class deleted.")        
        
    def check_exist(self,name)->int:
        is_exist= 0
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM class WHERE name = ? ORDER BY id LIMIT ?", (name,1))
        row = cursor.fetchone()
        conn.close()
        if row is not None:
            is_exist=row[0]
        
        return is_exist

    def view_all(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM class")
        rows = cursor.fetchall()
        conn.close()
        return rows
    
    def search_by_name(self,name):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM class WHERE name LIKE ?", ('%' + name + '%',))
        rows = cursor.fetchall()
        conn.close()
        return rows

class CourseRepo:   
        
    def add(self,name, detials)->int:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO course (name, details) VALUES (?, ?)", (name, detials ))
        conn.commit()
        print(" course added successfully.")
        conn.close()
        return cursor.lastrowid
    
    def delete(self, id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM course WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        print("course deleted.")        
        
    def check_exist(self,name)->int:
        is_exist= 0
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM course WHERE name = ? ORDER BY id LIMIT ?", (name,1))
        row = cursor.fetchone()
        conn.close()
        if row is not None:
            is_exist=row[0]
        
        return is_exist

    def view_all(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM course")
        rows = cursor.fetchall()
        conn.close()
        return rows
    
    def search_by_name(self,name):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM course WHERE name LIKE ?", ('%' + name + '%',))
        rows = cursor.fetchall()
        conn.close()
        return rows
    
class TeacherRepo:   
        
    def add(self,name, title, courseid)->int:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO teacher (name, title, courseid ) VALUES (?, ?, ?)", (name, title, courseid))
        conn.commit()
        print(" teacher added successfully.")
        conn.close()
        return cursor.lastrowid
    
    def delete(self, id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM teacher WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        print("teacher deleted.")        
        
    def check_exist(self,name)->int:
        is_exist= 0
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM teacher WHERE name = ? ORDER BY id LIMIT ?", (name,1))
        row = cursor.fetchone()
        conn.close()
        if row is not None:
            is_exist=row[0]
        
        return is_exist

    def view_all(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM teacher")
        rows = cursor.fetchall()
        conn.close()
        return rows
    
    def search_by_name(self,name):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM teacher WHERE name LIKE ?", ('%' + name + '%',))
        rows = cursor.fetchall()
        conn.close()
        return rows
    
class AssignmentRepo:   
        
    def add(self, title, description, deadline, course_id)->int:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO assignment (title, description, deadline, course_id) VALUES (?, ?, ?, ?)", ( title, description, deadline, course_id))
        conn.commit()
        print(" assignment added successfully.")
        conn.close()
        return cursor.lastrowid
    
    def delete(self, id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM assignment WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        print("assignment deleted.")        
        
    def check_exist(self,account)->int:
        is_exist= 0
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM assignment WHERE title = ? ORDER BY id LIMIT ?", (account,1))
        row = cursor.fetchone()
        conn.close()
        if row is not None:
            is_exist=row[0]
        
        return is_exist

    def view_all(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM assignment")
        rows = cursor.fetchall()
        conn.close()
        return rows
    
    def search_by_title(self,title):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM assignment WHERE title LIKE ?", ('%' + title + '%',))
        rows = cursor.fetchall()
        conn.close()
        return rows
    
class GradeRepo:   
        
    def add(self,value, comment, student_id, assignment_id)->int:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO grade (value, comment, student_id, assignment_id) VALUES (?, ?, ?, ?)", (value, comment, student_id, assignment_id ))
        conn.commit()
        print(" grade added successfully.")
        conn.close()
        return cursor.lastrowid
    
    def delete(self, id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM grade WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        print("grade deleted.")        
    
    def search_by_studentid(self,id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM grade WHERE student_id = ?", (id,))
        rows = cursor.fetchone()
        conn.close()
        return rows
    
    def search_by_assignment_id(self,id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM grade WHERE assignment_id = ?", (id,))
        rows = cursor.fetchone()
        conn.close()
        return rows