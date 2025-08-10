
class Person:

    # intial information in a list
    def __init__(self,name,age,address):
        self.details=[name,age,address]
    
    # add year to user's current age
    def age_add(self,add_year):
        self.details[1]+=add_year

class VerifyInput:

    def get_int_input(self,prompt):
        while True:
            try:
               return int(input(prompt))
            except ValueError:
                print("The number you input is invalid. Please input an integer!")


if __name__=="__main__":

    verify_obj=VerifyInput()
    # 1. collect user information
    
    name = input("please input your name: ")
    age = verify_obj.get_int_input("please input your age: ")
    address = input("please input your address: ")

    person = Person(name,age,address)

    # 2. print each detail with labels
    print("Name:", person.details[0])
    print("Age:", person.details[1])
    print("Address:", person.details[2])

    # 3. update age
    years = verify_obj.get_int_input("How many years you want to add to your current age? ")
    person.age_add(years)

    print(f"user name: {person.details[0]}. age: {person.details[1]} address: {person.details[2]}.")


    