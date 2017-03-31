SUBLIST, SUPERLIST, EQUAL, UNEQUAL = 1, 2, 3, 4

def check_lists(list1, list2):
    l1 = ' '.join(str(i) for i in list1)
    l2 = ' '.join(str(i) for i in list2)
    if l1 == l2:
        return EQUAL
    elif l1 in l2:
        return SUBLIST
    elif l2 in l1:
        return SUPERLIST
    else:
        return UNEQUAL
print(check_lists([10], [10]))
