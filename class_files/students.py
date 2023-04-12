class Student:
    institution = "IT Gurukul"
    
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3
    
    @classmethod
    def info(cls):
        return cls.institution
    
    
s1 = Student(34, 47, 54)
s2 = Student(24, 72, 48)

print(s1.avg())

print(Student.info())