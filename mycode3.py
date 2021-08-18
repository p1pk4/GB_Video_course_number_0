my_list1 = [1, 2, 3, 5, 6, 4]
my_list2 = ['d', 'a', 'c', 'b']

my_list1.sort()
my_list2.sort()
print(my_list1, my_list2)

if len(my_list1) <= len(my_list2):
    for list1 in my_list1:
        print(list1)
else:
    for list2 in my_list2:
        print(list2)