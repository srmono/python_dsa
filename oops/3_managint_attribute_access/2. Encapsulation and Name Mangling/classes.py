class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.set_salary(salary)

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    def __str__(self):
        return f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}"

    def __repr__(self):
        return (
            f"Employee("
            f"{repr(self.name)}, {repr(self.age)}, "
            f"{repr(self.position)}, {repr(self.salary)})"
        )

    def get_salary(self):
        # return self.__salary
        return self._salary

    def set_salary(self, salary):
        if salary < 1000:
            raise ValueError('Minimum wage is $1000')
        # self.__salary = salary
        self._salary = salary


employee1 = Employee("Ji-Soo", 38, "developer", 1200)
employee2 = Employee("Mohan", 44, "tester", 1000)

employee1.set_salary(2000)
print(employee1.get_salary())
# print(employee1._Employee__salary)
