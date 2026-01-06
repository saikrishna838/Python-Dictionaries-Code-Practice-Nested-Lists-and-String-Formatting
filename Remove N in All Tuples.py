num_list = [(1, 2, 3, 4, 5, 6), (2, 4, 6, 8), (1, 3, 5, 7)]

n = int(input())
for tuple_b in num_list:
    is_contain = n in tuple_b
    if is_contain:
        tuple_index = int(num_list.index(tuple_b))
        n_index = int(tuple_b.index(n))
        temp_list = list(num_list[tuple_index])
        temp_list.pop(n_index)
        num_list[tuple_index] = tuple(temp_list)
        
print(num_list)
    
        