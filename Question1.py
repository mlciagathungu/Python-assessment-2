class car:
    def __init__(self, brand, model, year):
        self.model = model
        self._brand = brand
        self.__year = year
    def display_info(self):
        print("Brand:", self._brand)
        print("Model:", self.model)
        print("Year:", self.__year)
car1 =car("Audi", "rsq8", 2020) 
car1.display_info() 
print(car1.model) 
print(car1._brand) 
print(car1.__year) 