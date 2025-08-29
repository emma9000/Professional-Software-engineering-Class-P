
class User:

    def __init__(self,name,address,age,ID):
        self.name=name
        self.address=address
        self.age=age
        self.ID=ID

class Academics(User):
        
    def __init__(self,tax_code,salary,name,address,age,ID):
        super().__init__(name,address,age,ID)
        self.tax_code=tax_code
        self.salary=salary  

class Staff(User):
    
    def __init__(self,pay_rate,office,name,address,age,ID):
        super().__init__(name,address,age,ID)
        self.pay_rate=pay_rate
        self.office=office

class Student(Academics):

    def __init__(self,acadamic_record,student_code,tax_code,salary,name,address,age,ID):
        super().__init__(tax_code,salary,name,address,age,ID)
        self.acadamic_record=acadamic_record
        self.student_code=student_code
    
class Teacher(Staff):

    def __init__(self,title,courseid,pay_rate,office,name,address,age,ID):
        super().__init__(pay_rate,office,name,address,age,ID)
        self.title=title
        self.courseid=courseid
