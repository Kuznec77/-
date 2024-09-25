my_dict = {'Vasya': 1988, 'serz': 1978, 'Petya':2001}
print(my_dict)
print(my_dict['Petya'])
print(my_dict.get('Sasha'))
my_dict.update({'Roma':1985, 'Sveta':1988})
a = my_dict.pop('Vasya')
print(a)
print(my_dict)
my_set = {1,2,3,4,5,1,2,3,}
print(my_set)
my_set.add(6)
my_set.add('orange')
my_set.discard(2)
print(my_set)