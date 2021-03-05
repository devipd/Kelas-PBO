class Student:
   """A class representasing a student"""
   stdCount = 0

   def __init__(self,n,a,nim):
      self.name = n
      self.age = a
      self.nim = nim
      Student.stdCount += 1
   
   def getCount(self):
     print ("Total Student : %d" % Student.stdCount)

   def getStudent(self):
      print ("Nama : ", self.name,", Umur : ",self.age,", NIM : ",self.nim)

#This would create first object of Student class"
std1 = Student("Devi Puspita Dewi",20,1905877)
#This would create second object of Student class"
std2 = Student("Fauziyah Rhaudatul Jannah",19, 1904035)
#This would create thrid object of Student class"
std3 = Student("Sanni Deslia Pasaribu",20, 1903119)
#This would create four object of Student class"
std4 = Student("Esa Noer Fadhila", 21,1908527)
#This would create five object of Student class"
std5 = Student("Adisty Nurahmah Laily",21,1904347)
#This would create six object of Student class"
std6 = Student("Zamzam Kholidatuzzahra",20,1905872)
std1.getStudent()
std2.getStudent()
std3.getStudent()
std4.getStudent()
std5.getStudent()
std6.getStudent()
print ("Total Student %d" % Student.stdCount)