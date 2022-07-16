class Employee:
    def __init__(self,name='',salary=0,age=0):
        self._salary=salary
        self._name=name
        self._age=age
    def __str__(self):
        return f'Employee: {self._name} has age {self._age} and a salary {self._salary}'
    @property
    def salary(self):
        return self._salary
    @salary.getter
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,new_salary):
        if new_salary>0 and isinstance(new_salary,float):
            self._salary=new_salary
        else:
            print("Pleas enter a valid salary")
    @salary.deleter
    def salary(self):
        del self._salary
    @property
    def age(self):
        return self._age
    @age.getter
    def age(self):
        return self._age
    @age.setter
    def age(self,new_age):
        if new_age>=21 and isinstance(new_age,int):
            self._age=new_age
        else:
            print("Pleas enter a valid Age")
    @age.deleter
    def age(self):
        del self._age
    @property
    def name(self):
        return self._name
    @name.getter
    def name(self):
        return self._name
    @name.setter
    def name(self,new_name):
        if new_name!='' and isinstance(new_name,str):
            self._name=new_name
        else:
            print("Pleas enter a valid name")
    @name.deleter
    def name(self):
        del self._name

