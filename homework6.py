my_dict = {'Anastasia': 2003, 'Veronika': 2000, 'Ivan': 1999}
print(my_dict)
print(my_dict['Anastasia'])
print(my_dict.get('Sergey'))
my_dict.update({'Sasha': 2006, 'Egor': 1987})
a = my_dict.pop('Ivan')
print(a)
print(my_dict)

my_set = {1,2,3,6,1,3,6, 'String', 2.65, (1, 2, 6)}
print(my_set)
my_set.update({12, (2, 9)})
my_set.discard('String')
print(my_set)









