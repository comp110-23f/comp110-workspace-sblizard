def sum_evens(input_list: list[int]) -> int:
    return_val: int = 0
    for i in input_list:
        if i%2 == 0:
            return_val += i
    return return_val