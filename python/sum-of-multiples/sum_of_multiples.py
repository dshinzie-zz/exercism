def sum_of_multiples(number_to, number_list):
    multples_sum = 0
    multples_sum += sum([i for i in range(number_to) if any(i % number == 0 for number in number_list)])
    return multples_sum
