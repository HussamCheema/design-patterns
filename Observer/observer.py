from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self, observable, *args):
        pass


class Observable:

    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def delete_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observers(self, *args):
        for observer in self.__observers:
            observer.update(self, *args)
            
            
class Employee(Observable): 

    def __init__(self, name, salary):
        super().__init__() 
        self._name = name
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary
        self.notify_observers(new_salary) 


class Payroll(Observer): 

    def update(self, changed_employee, new_salary):
        print(f'Cut a new check for {changed_employee.name}! '
            f'Her/his salary is now {new_salary}!')


class TaxMan(Observer): 

    def update(self, changed_employee, new_salary):
        print(f'Send {changed_employee.name} a new tax bill!')
        
        
        
e = Employee('Amy Fowler Fawcett', 50000)
p = Payroll()
t = TaxMan()

e.add_observer(p)
e.add_observer(t)

print('Update 1')
e.salary = 60000

e.delete_observer(t)

print('\nUpdate 2')
e.salary = 65000
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        