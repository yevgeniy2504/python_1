
init_list = [1, 1, 2, 3, 4, 4, 5, 5, 5, 6, 6, 7, 8, 9, ]

repeated_list = [elem for elem in init_list if init_list.count(elem) > 1]

print(list(set(repeated_list)))




