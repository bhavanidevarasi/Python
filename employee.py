from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self,name,employee_id,salary):
        if salary < 0:
            raise ValueError("salary can not be negative")
        self.name=name
        self.employee_id=employee_id
        self.__salary= salary
    @property
    def salary(self):
        return self.__salary
    @abstractmethod
    def calculate_salary(self):
        pass
class FullTimeEmp(Employee):
    def __init__(self,name,employee_id,salary):
        super().__init__(name,employee_id,salary)
    def calculate_salary(self):
        return self.salary * 30
class PartTimeEmp(Employee):
    def __init__(self,hrs,name,employee_id,salary):
        self.hrs = hrs
        super().__init__(name,employee_id,salary)
    def calculate_salary(self):
        return self.salary * self.hrs
class Freelancer(Employee):
    def __init__(self,days,name,employee_id,salary):
        self.days=days
        super().__init__(name,employee_id,salary)
    def calculate_salary(self):
        return self.salary * self.days
if __name__ == '__main__':
    try:
        ft = FullTimeEmp('harry',1,30)
        pt = PartTimeEmp(2,'tom',2,40)
        fl = Freelancer(3,'hermoine',3,20)
        print("The saalry of Full time Employee : ",ft.calculate_salary())
        print("The salary of Part time Employee : ",pt.calculate_salary())
        print("The salary of Free lancer Employee : ",fl.calculate_salary())
        employees = [ft,pt,fl]
        for employee in employees:
            print(employee.name, employee.calculate_salary())
    except ValueError as e :
        print(e)
# Notification Problem
class Notification(ABC):
    @abstractmethod
    def notification(self):
        pass
class EmailNotification(Notification):
    def __init__(self,email_id):
        self.__email_id=email_id
    def notification(self):
        print(f"This is an email notification from : {self.__email_id}")
class SMSNotification(Notification):
    def __init__(self,SMS_ID):
        self.__SMS_ID=SMS_ID
    def notification(self):
        print(f"This is an sms notification from : {self.__SMS_ID}")
class PushNotification(Notification):
    def __init__(self,random):
        self.__random = random
    def notification(self):
        print(f"This is a random notification from : {self.__random}")
en = EmailNotification('adc@gmail.com')
sn = SMSNotification('123343')
pn = PushNotification('myntra')
en.notification()
sn.notification()
pn.notification()
noti = [en,sn,pn]
for n in noti:
    print(n.notification())
#Vehicle Problem
class Vehicle(ABC):
    def __init__(self,price):
        self.__price = price
        self.__availability= True
    @property
    def price(self):
        return self.__price
    @property
    def availability(self):
        return self.__availability
    @abstractmethod
    def calculate_rent(self,days):
        pass
class Car(Vehicle):
    def __init__(self,days,price):
        self.days=days
        super().__init__(price)
    def rent(self):
        return self.price 
    def return_vehicle(self):
        return True
    def calculate_rent(self):
        return self.price * self.days

