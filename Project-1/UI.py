from Special import Speicality
from Patients import Patient
class Ui:
    def __init__(self):
        self._speicallist=[Speicality() for i in range(22)]
    def AddPatient(self):
        while True:
            s=int(input("Enter your speciality:1-20::  "))
            if 20>=s>=1:
                break
        n=input('Enter Pateint Name: ')
        while True:
            m=int(input('Enter Status: '))
            if 2>=m>=0:
                break
        self._speicallist[s].Add_Patient(Patient(n,m))

    def printt(self):
        for j,i in enumerate(self._speicallist):
            if len(i.lst)!=0:
                print(f'Specilization {j}: There are {len(i.lst)}')
                i.print_patients()
    def Get_Next(self):
        while True:
            s=int(input("Enter your speciality: "))
            if 20>=s>=1:
                break
        state,p=self._speicallist[s].GetNextPatient()
        if state==True:
            self._speicallist[s].GetNextPatient()
            print(f'The Patient is leaving {p.name}')
        else:
            print("Have Rest ")
    def remove_patient(self):
        while True:
            s=int(input("Enter your speciality: "))
            if 20>=s>=1:
                break
        n=input('Enter Patient Name: ')
        self._speicallist[s].Remove_patient(n)




