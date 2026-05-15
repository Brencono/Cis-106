#define object
class Employee:
    def __init__(self, first, last, pay):
        # use pass to leave empty for now
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + '@company.com'
        #self.rate = 0.00
    
    
    def bonus(self,rate):
        b = float(rate) * float(self.pay)
        return b
   
    
   # main progrma
    # instantiate the object
empl1 = Employee('Frank', 'Alvino', 600000)

#use the object
print(empl1.email)
print(empl1.first)
print(empl1.last)
print(empl1.pay)
print(empl1.bonus(.1))
print(empl1.bonus(.2))