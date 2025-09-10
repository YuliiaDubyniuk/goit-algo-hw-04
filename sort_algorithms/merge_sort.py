def merge_sort(lst):
    """
    Split list to 2 parts 
    Merge elements from both parts in sorted order
    """
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    """Return new sorted list after merging in right order 2 halves of the original"""
    merged = []
    left_index = 0
    right_index = 0

    # Join left side and right side elements in correct order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Add other elements if left
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged
