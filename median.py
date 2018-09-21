print('working')


def median(arry1, arry2):

    arry1.extend(arry2)
    merged_list = sorted(arry1)

    return (len(merged_list) + 1) / 2
