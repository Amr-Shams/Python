from Employee import Employee
class Manger:
    def __init__(self,new_list=[]):
        self._employeelist=new_list
    def add_employee(self,emp):
        if isinstance(emp,Employee):
            self._employeelist.append(emp)
        else:
            print("We add only employees")
    def list_all_employees(self):
        for i in self._employeelist:
            print(i)
    def update_salary(self,name,salary):
        found=False
        for i in range(len(self._employeelist)):
            if self._employeelist[i].name==name:
                found=True
                temp=self._employeelist[i].age
                del self._employeelist[i]
                self.add_employee(Employee(name,salary,temp))
        if not found:
            print("No Name with this")

    def delete_employee(self,age_from,age_to):
        ff=True
        n=len(self._employeelist)
        idx=0
        while idx<n:
            if age_to>=self._employeelist[idx].age>=age_from:
                print(f'Deleteing {self._employeelist[idx].name}')
                del self._employeelist[idx]
                n=len(self._employeelist)
                ff=False
            else:
                idx+=1
        if ff:
            print("Enter a valid Range")

    @property
    def employee_list(self):
        self._employeelist=[]
    @employee_list.setter
    def employee_list(self,new_list):
        if len(new_list)>0 and isinstance(new_list,list):
            self._employeelist=new_list
        else:
            print("Enter a valid List")
    @employee_list.deleter
    def employee_list(self):
        del self._employeelist


