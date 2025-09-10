def insertion_sort(lst):
    """Sort a list of comparable items in ascending order using insertion sort."""
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst
