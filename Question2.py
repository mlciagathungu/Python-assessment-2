class person:
    def __init__(self, name, age, salary, ):
        self.name = name
        self._age = age
        self.__salary = salary

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self._age)
        print("Salary:", self.__salary)

person1 = person("John", 25, 50000)
person1.display_info()  
print(person1.name) 
print(person1._age) 
print(person1.__salary) 


