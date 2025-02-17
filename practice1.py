# class cases() :
#     def __init__(self , name , age , number , ill):
#         self.name= name
#         self.age= age
#         self.number=1000
#         self.ill=ill

#     def self(number) :
#         number +=1
from os import name


a = {
    "name" :[],
    "age" : [] ,
    "number" :[],
    "illness" :[]
}

v= True
while v == True:
    x= input("type add for add a person and tyype find for find a person")
    if x == "add" :
      a["name"].append(input("your name"))
      a["age"].append(int(input("your age")))
      a["number"].append(len(a["name"])+1000)
      a["illness"].append(input("your illness"))
      print("Its your number" , len(a["name"])+1000)
    elif x == "find" :
      z= input("what is your number?")
      z=int(z)
      b = a["number"].index(z)
      print("name: " , a["name"][b])
      print("age: " , a["age"][b])
      print("number: " , a["number"][b])
      print("illness: " ,a["illness"][b])
    else : print("its wrong please try again ,type 'add' for add a person and tyype 'find' for find a person ")
    

    



        
    



