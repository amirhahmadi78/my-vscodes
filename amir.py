cs = [
{
   'title': 'python'
},
{
   'title' : 'html'
} ]

class Ensan:
   def __init__(self , lname , fname):
      self.lname = lname
      self.fname = fname

class student(Ensan):
   def __init__(self, lname, fname, level):
      super().__init__(lname, fname)
      self.level= level
      self.corsess= []

   def fullname(self):
         print(f"NAME: {self.fname}  LASTNAME: {self.lname} MY LEVEL:  {self.level}")

   def corse (self):
      if self.corsess == False:
         print('vaghteshe zabaneto vared koni')
      else:
         print(self.corsess)

p1=student("ahmadi","amir", "5")
p1.corsess.append(cs[1])
p1.fullname()
p1.corse()


























