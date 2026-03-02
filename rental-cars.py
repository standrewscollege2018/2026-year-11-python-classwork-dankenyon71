'''This program functions as a rental system for university cars'''

from dataclasses import dataclass

cars = []

class Car:
    def __init__(self, name, seats):
        self._name = name
        self._seats = seats
        cars.append(self)

Car('Suzuki Van', 2)
Car('Toyota Corolla', 4)
Car('Honda CRV', 4)
Car('Suzuki Swift', 4)
Car('Mitsubishi Airtrek', 4)
Car('Nissan DC Ute', 4)
Car('Toyota Previa', 7) 
Car('Toyota Hi Ace', 12)
Car('Toyota Hi Ace', 12)

print('University vehicle rental system')
print('=================================')

for i in range(len(cars)):
    print(f"{i+1}. {cars[i]._name:20} {cars[i]._seats} seats")