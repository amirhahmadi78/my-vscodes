
a = {
    "name" :[],
    "age" : [] ,
    "number" :[],
    "illness" :[]
}

v= True
while v == True:
    x= input("type '1' for add a patient , type '2' for find a patient , type '3' for delet a patient ,type '4' for see all patient , type '5' for stop")
    if x == "1" :
      a["name"].append(input("your name"))
      a["age"].append(int(input("your age")))
      a["number"].append(len(a["name"])+1000)
      a["illness"].append(input("your illness"))
      print("Its your number" , len(a["name"])+1000)
    elif x == "2" :
      z= input("what is your number?")
      z=int(z)
      b = a["number"].index(z)
      print("name: " , a["name"][b])
      print("age: " , a["age"][b])
      print("number: " , a["number"][b])
      print("illness: " ,a["illness"][b])
    elif x == '3':
      z= input("what is your number?")
      z=int(z)
      b = a["number"].index(z)
      del a['name'][b]
      del a["age"][b]
      del a["number"][b]
      del a["illness"][b]
      print(f'okay {a['name'][b]} deleted')
    elif x == '4':
       for h in a["name"] :
          b = a["name"].index(h)
          print (f' name: {h}  , age: {a["age"][b]} , number: {a["number"][b]},illness: {a["illness"][b]}')

    elif x == '5':
      break 
    
    else : print("its wrong , please try again ,type '1' for add a patient , type '2' for find a patient , type '3' for delet a patient ,type '4' for see all patient , type '5' for stop ")
    

    



        
    



