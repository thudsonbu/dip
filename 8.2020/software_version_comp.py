def compare_versions(v1,v2):
    v1 = [section for section in v1.split(".")]
    v2 = [section for section in v2.split(".")]
    same_length = len(v1) == len(v2)
    if not same_length:
        if len(v1) > len(v2):
            longer = v1
            out = 1
        else:
            longer = v2
            out = -1
    count = 0
    while count < len(v1) and count < len(v2):
        v1_val = int(remove_leading_zeros(v1[count]))
        print("val1: " + str(v1_val))
        v2_val = int(remove_leading_zeros(v2[count]))
        print("val2: " + str(v2_val))
        if v1_val == v2_val and same_length and count == len(v2) - 1:
            print("yup")
            return 0
        elif v1_val == v2_val:
            count += 1
            continue
        elif v1_val > v2_val:
            return 1
        else:
            return -1
    for section in longer[count::]:
        if remove_leading_zeros(section) == "":
            continue
        else:
            return out
    return 0
    



def remove_leading_zeros(str):
    while len(str) > 0:
        if str[0] == "0":
            str = str[1::]
        else:
            break
    return str

print(remove_leading_zeros("001"))
print(remove_leading_zeros("1"))

print(compare_versions("1","1.01"))