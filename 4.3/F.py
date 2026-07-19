def merge(left, right):
    result = []
    pos_left = pos_right = 0
    while pos_left < len(left) and pos_right < len(right):
        if left[pos_left] > right[pos_right]:
            result.append(right[pos_right])
            pos_right += 1
        else:
            result.append(left[pos_left])
            pos_left += 1

    result += left[pos_left:]
    result += right[pos_right:]
    return result


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        left = merge_sort(left)
        right = merge_sort(right)
    return merge(left, right)