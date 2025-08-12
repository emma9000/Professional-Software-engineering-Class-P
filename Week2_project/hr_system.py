
class Employee:

    def __init__(self,name,salary,job_title):
        self.name = name
        self.salary = salary
        self.job_title = job_title

    # displaying an emplyee's details
    def display_info(self):
        print(f"name: {self.name} salary: {self.salary} job_title: {self.job_title}")

    # Increasing an employee’s salary and displaying the updated amount.
    def give_raise(self,raise_amount):
        original_salary = self.salary
        self.salary += raise_amount 
        print(f"[SYSTEM] Salary adjustment confirmed: {self.name}'s monthly salary has been successfully updated")
        print(f"from {original_salary} to {self.salary}. Effective immediately.")

class VerifyInput:

    def get_int_input(prompt):
        try:
            return float(prompt)
        except ValueError:
            print("The number you input is invalid. Please input an float!")

        
if __name__=="__main__":

    employee_1 = Employee ("Emma", 15000, "Software Engineer")
    employee_2 = Employee ("Niko", 20000, "Manager")
    #store basic employee information
    employees = [employee_1,employee_2]

    #display basic employee information
    for emp in employees:
        emp.display_info()

    # raise salary for someone
    is_raised=False
    while not is_raised:
        input_data=input(f"Enter employee's full name and salary raise amount (separated by space):")

        raise_info=input_data.split(' ')
        if(len(raise_info)<2):
            continue
        
        amout= VerifyInput.get_int_input(raise_info[1])    
        if(amout!=None):       
            name = raise_info[0].lower()

            for emp in employees:
                if emp.name.lower() != name:
                    continue
                else:
                    emp.give_raise(amout)
                    is_raised=True
                    break
                

    