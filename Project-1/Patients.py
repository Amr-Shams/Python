class Patient:
    def __init__(self,name,status):
        self._name=name
        if status==0:
            self._status='Normal'
        elif status==1:
            self._status='Urgant'
        else:
            self._status='Super Urgent'
    @property
    def name(self):
        return self._name
    @name.deleter
    def name(self):
        del self._name
    @property
    def status(self):
        return self._status
    @status.deleter
    def status(self):
        del self._status
