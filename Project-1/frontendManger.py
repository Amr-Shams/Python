from Manger import Manger
from Employee import Employee
class FrontEndManger:
    def __init__(self):
        self._Mangers=Manger()
        self._choice=0
    def take_choice(self,m):
        self._choice=m
    def print_screen(self):
        print("Programe Options")
        print("1) Add A new Employee ")
        print("2) List All Employess ")
        print("3) Delete by age Range ")
        print("4) Update Salary By Name")
        print("5) End the progrme ")
    def processing(self):
           if self._choice==1:
                new_employee=Employee()
                new_employee.name=input('Enter Name: ')
                new_employee.age=int(input('Enter Age: '))
                new_employee.salary=int(input('Enter salary: '))
                self._Mangers.add_employee(new_employee)
           elif self._choice==2:
                self._Mangers.list_all_employees()
           elif self._choice==3:
                agefrom=int(input('Enter Age from: '))
                ageto=int(input('Enter Age to '))
                self._Mangers.delete_employee(agefrom,ageto)
           elif self._choice==4:
                n=input("Enter the Name: ")
                s=int(input('Enter the New Salary: '))
                self._Mangers.update_salary(n,s)
    @property
    def choice(self):
        return self._choice
    @choice.setter
    def choice(self,m):
        if 5>=m>=1 and isinstance(m,int):
            self._choice=m
    @choice.getter
    def choice(self):
        return self._choice
