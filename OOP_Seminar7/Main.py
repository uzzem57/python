from Coffe import Coffe
from Tea import Tea



coffe1 = Coffe("cappuchino", 200, 150 )
print(coffe1.getPrice())

tea1 = Tea("Green", 150, 98)
print(tea1.getTemperature())
tea1.setName("Black")
print(tea1.getName())

my_dict = {}
my_dict[tea1] = (tea1.getName(),tea1.getVolume(), tea1.getTemperature())
print(my_dict)











