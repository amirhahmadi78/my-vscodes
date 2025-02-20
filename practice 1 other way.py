
a=[]


def add ():
    global patient
    patient= {
    'name':input("wats your name?"),
    'age':input("whats your years old"),
    'number':str(1001+len(a)),
    'illness':input("wahts your illness")
    }
    a.append(patient)
    print(f'your number: {patient["number"]}')
    print("you added to patients list")

def find():
    f=input('type your number')
    for patient in a:
        if patient['number']== f:
            print(patient)
        else : print("its wrong")

def delete():
    d=input('type your number')
    for patient in a:
        if d == patient["number"]:
           patient.clear()
           patient.update({'name':'deleted',
                           'age':'deleted',
                           'number':'deleted',
                           'illness':'deleted'})
        print('your patient deleted')
    else: print("its wrong")

def show():
     for patient in a:
       print(patient["name"], patient["number"])

def close():
    print(' okay goodbye')
    False


while True:
    x=input("type '1' for add, type '2' for find , type '3' for delete , type '4' for show list names , type '5' for close program")
    if x =="1":
        add()
    elif x == "2":
        find()
    elif x=="3":
        delete()
    elif x=="4":
        show()
    elif x=="5":
        close()
    else: print("please try again later") ,
    break



        




















