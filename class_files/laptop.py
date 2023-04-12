class Laptop:
    def __init__(self, cpu, ram):
        self.cpu = cpu 
        self.ram = ram
    
    def config(self):
        print("configuration of the laptop is: ", self.cpu, self.ram)
        
laptop1 = Laptop("I7", 16)
laptop2 = Laptop("i9", 32)

#print(laptop1)

laptop1.config()
laptop2.config()

# Laptop.config(laptop1)
# Laptop.config(laptop2)