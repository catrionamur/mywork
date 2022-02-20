#Take list of names and modules to you enter blank module
#Catriona Murray

names= []
modules = []
grades = []
done = False
while(done == False):
   studentName = input("Enter Name: ")
   gradesInput = int(input("Enter Grade: "))
   modulesInput = input("Enter Module: ")
   if (modulesInput != ""):
        modules.append(modulesInput)
        names.append(studentName)
        grades.append(gradesInput)
   else: 
      done = True 
      print (names)
      print (modules)
      print (str(grades))
      break
