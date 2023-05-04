from person import Person
from Employee import Employee
from office import Office

employees = []
employees.append(Employee("Eatedal",10000,10,200))
employees.append(Employee("makram",10000,10,200))


of1=Office("iti",employees)
print(of1.get_All_employees())



