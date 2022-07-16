from Patients import Patient
class Speicality:
    def __init__(self):
        self._Patientlst=[]
        self._numofurgents=0
        self._numofsurgent=0
        self._numnormal=0
    def Add_Patient(self,Pp):
        if len(self._Patientlst)<10:
            if Pp.status=='Super Urgent':
                self._Patientlst.insert(self._numofsurgent,Pp)
                self._numofurgents+=1
                self._numofsurgent+=1
                self._numnormal+=1
            elif Pp.status=='Urgent':
                self._Patientlst.insert(self._numofurgent,Pp)
                self._numofurgents+=1
                self._numnormal+=1
            else:
                self._Patientlst.insert(self._numnormal,Pp)
                self._numnormal+=1
        else:
            print("We are sorry it's full ")
    def print_patients(self):
        for i in self._Patientlst:
            print(f'Patient: {i.name} is {i.status}')
    def GetNextPatient(self):
        if len(self._Patientlst)!=0:
            return True,self._Patientlst.pop(0)
        else:
            return False,Patient('dumby',0)
    def Remove_patient(self,name):
        for i in range(len(self._Patientlst)):
            if self._Patientlst[i].name==name:
                print(f'patient {self._Patientlst[i].name} is leaving')
                self._Patientlst.pop(i)
    @property
    def lst(self):
        return self._Patientlst


