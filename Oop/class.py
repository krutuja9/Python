class Employee:
  
  def __init__(self, name , salary):
    self.name = name
    self.salary = salary
  def getSalary(self):
    print (self.salary)
  

rutuja = Employee("rutuja", 30000)
print(rutuja.salary)
print(rutuja.name)

rk = Employee("rk", 60000)
print(rk.salary)
print(rk.name)

rk.getSalary()
 
