from UI import Ui
if __name__=='__main__':
    Ui=Ui()
    while True:
        print("Programe Options")
        print("1) Add A new Patient ")
        print("2) List All Patients ")
        print("3) Get Next Patient ")
        print("4) Remove a leaving patient")
        print("5) End the progrme ")
        while True:
            n=int(input('Enter Your Choice: '))
            if 5>=n>=1:
                break
        if n==1:
            Ui.AddPatient()
        elif n==2:
            Ui.printt()
        elif n==3:
            Ui.Get_Next()
        elif n==4:
            Ui.remove_patient()
        else:
            print("Thanks for Your Time :) ")





