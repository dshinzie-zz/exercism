def flatten(input_list):
    if input_list == []:
        return input_list
    if isinstance(input_list[0], list):
        return flatten(input_list[0]) + flatten(input_list[1:])
    return input_list[:1] + flatten(input_list[1:])
