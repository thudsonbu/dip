def compare_versions(v1, v2):
    v1_list = [num for num in v1.split(".")]
    v2_list = [num for num in v2.split(".")]
    iterations = min(len(v1_list, v2_list))
    for i in range(iterations):
        comp = compare_value(v1_list[i],v2_list[i])
        if comp == 0:
            continue
        else:
            return comp
    if len(v1_list) > len(v2_list):
        sum = 0
        for num in v1_list[iterations + 1::]:
            sum += num
        if sum > 0:
            return 1
    elif len(v1_list) < len(v2_list):
        sum = 0
        for num in v2_list[iterations + 1::]:
            sum += num
        if sum > 0:
            return -1
    else: 
        return 0
        
def compare_value(v1, v2):
    count = 0
    sym = v1[count]
    while sym == "0":
        count += 1
        sym = v1[count]
    v1 = v1[count::]
    count = 0
    sym = v2[count]
    while sym == "0":
        sym = v2[count]
    v2 = v2[count::]
    if v1 > v2:
        return 1
    elif v1 < v2:
        return -1
    else:
        return 0