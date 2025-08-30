class Student:

    def __init__(self, name, age):
        self.name = name # public​
        self._age = age # protected​
        self.__grade = 'A' # private​
        self.__password='666666' # private​


    def get_grade(self):

        return self.__grade
    
    # A new public method that allows users to change their password (a private attribute)
    def change_password(self,new_password):
        self.__password=new_password
        print(f"Password changed successfully! new password is :{self.__password}")
        

class GroupStudent(Student):

    def __init__(self, name, age, group_num):
        super().__init__(name,age)

        self.group_num=group_num
        
    # public attribute
    def show_group(self):
        print(f"My group is {self.group_num}")

    # protect attribute
    def show_age(self):
        print(f"My age is {self._age}")


s = Student('Ali', 20)

print(s.name) # accessible​
print(s._age) # discouraged​
print(s.get_grade()) # correct way​

s.change_password("abc123")

gb = GroupStudent("Emma",18,"B")
gb.show_age()
gb.show_group()

# The purpose of encapsulation is to improve code security and maintainability.  
# Only the necessary information is exposed to the outside through public attributes.  
