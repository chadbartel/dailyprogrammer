def mean(num_list):
    result = 0
    count = 0
    for num in num_list:
        result += num
        count += 1
    return result/count


def mean_diff_sq(num_list):
    avg = mean(num_list)
    diff_list = []
    for num in num_list:
        diff_list.append((num - avg)**2)
    return diff_list


def add_list(num_list):
    diff_list = mean_diff_sq(num_list)
    result = 0
    for d in diff_list:
        result += d
    return result


def div_sum(num_list):
    list_sum = add_list(num_list)
    count = len(num_list)
    return list_sum/count


def std_dev(num_list):
    sum_div = div_sum(num_list)
    return sum_div**(1/2)


print(std_dev([5, 6, 11, 13, 19, 20, 25, 26, 28, 37]))
