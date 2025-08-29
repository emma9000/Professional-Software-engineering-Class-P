
class User:

    def __init__(self,name,address,age,ID):
        self.name=name
        self.address=address
        self.age=age
        self.ID=ID

    def greet(self):
        print(f" Greeting from the User class name is {self.name}")

class Academics(User):
        
    def __init__(self,tax_code,salary,name,address,age,ID):
        super().__init__(name,address,age,ID)
        self.tax_code=tax_code
        self.salary=salary  
    
    def greet(self):
        return super().greet()

class Staff(User):
    
    def __init__(self,pay_rate,office,name,address,age,ID):
        super().__init__(name,address,age,ID)
        self.pay_rate=pay_rate
        self.office=office
    def greet(self):
        return super().greet()
    

class Student(Academics):

    def __init__(self,acadamic_record,student_code,tax_code,salary,name,address,age,ID):
        super().__init__(tax_code,salary,name,address,age,ID)
        self.acadamic_record=acadamic_record
        self.student_code=student_code

    def great(self):
        print(f"Hi, I'm new in YB College, my name is {self.name}")
    
class Teacher(Staff):

    def __init__(self,title,courseid,pay_rate,office,name,address,age,ID):
        super().__init__(pay_rate,office,name,address,age,ID)
        self.title=title
        self.courseid=courseid
    def greet(self):
        print(f"Hi, I'm your teacher {self.name}")

student= Student("A123","B234","",0,"Emma","New Lynn",18,1)
student.greet()
teacher= Teacher("Professor",1,10,"lecture office","Emily","YB college location",30,1)
teacher.greet()