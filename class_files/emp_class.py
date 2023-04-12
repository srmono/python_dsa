class Employee:
    def __init__(self, name, age, role, salary):
        self.name = name 
        self.age = age 
        self.role = role 
        self.salary = salary
        #self.annual_salary
        #self.set_salary(salary)
    
    # def getEmpInfo(self):
    #     print(self.name)
    
    def increaseSalary(emp, percent):
        emp.salary += emp.salary * (percent/100)
    
    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"{self.name}"
    
    def __add__(self, other_emp):
        return Employee("New", self.age + other_emp.age, "dev", 2000)
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, salary):
        #raise AttributeError("salary is read-only")
        if salary < 1000:
            raise ValueError("Minimum wage is $1000")
        self._salary = salary
        
    @property
    def password(self):
        raise AttributeError("password is write only")
    
    @password.setter
    def password(self,password):
        self.password = password
        
        
emp1 = Employee("venkat", 36, "developer", 1200)
emp2 = Employee("karthik", 26, "tester", 1000)


emp1.password

#emp1.set_salary(2000)
# emp1.salary = 2500
# print(emp1.salary)
# print(emp1.get_salary())
# print(emp1._Employee__salary)

#emp3 = emp1.__add__(emp2)
#emp3 = emp1 + emp2 

#print(emp3)
# print(repr(emp1))


#emp1.getEmpInfo()

#Employee.increaseSalary(emp1, 20)
#Employee.employee_info(emp1)

#print(emp1.__class__)



# n = "venkat"
# print(n.__class__)
       