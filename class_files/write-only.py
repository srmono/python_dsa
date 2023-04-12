
@property
def password():
    raise AttributeError("Password is write-only")
    
@password.setter
def password(self, password):
    self._password = password
    

@property
def annual_salary(self):
    return self.salary * 12