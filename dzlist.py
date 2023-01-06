from random import randint
#3

my_list_1 = [1, 2, 3, 4, 5, 6]
my_list_2 = ['a', 'b', 'c', 'd', 'e', 'f']
my_result = []
my_result2 = []

for i in range(0, len(my_list_1)):
    if i % 2 != 0:
        my_result.append(my_list_1[i])
    else:
        my_result2.append(my_list_2[i])
my_result.extend(my_result2)
print(my_result)

#11
print('\n*** Задача 11 ***\n')
my_str = str('hello world')
my_set = set(my_str)
my_list = (list(my_set))
my_results = []
for i in my_list:
    my_results.append(i)
print(my_results)
