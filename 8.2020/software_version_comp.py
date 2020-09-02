# Hi, here's your problem today. This problem was recently asked by Amazon:

# Version numbers are strings that are used to identify unique states of software products. A version number is in the format a.b.c.d. and so on where a, b, etc. are numeric strings separated by dots. These generally represent a hierarchy from major to minor changes. Given two version numbers version1 and version2, conclude which is the latest version number. Your code should do the following:
# If version1 > version2 return 1.
# If version1 < version2 return -1.
# Otherwise return 0.

# Note that the numeric strings such as a, b, c, d, etc. may have leading zeroes, and that the version strings do not start or end with dots. Unspecified level revision numbers default to 0.

# Example:
# Input: 
# version1 = "1.0.33"
# version2 = "1.0.27"
# Output: 1 
# #version1 > version2

# Input:
# version1 = "0.1"
# version2 = "1.1"
# Output: -1
# #version1 < version2

# Input: 
# version1 = "1.01"
# version2 = "1.001"
# Output: 0
# #ignore leading zeroes, 01 and 001 represent the same number. 

# Input:
# version1 = "1.0"
# version2 = "1.0.0"
# Output: 0
# #version1 does not have a 3rd level revision number, which
# defaults to "0"

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
        v2_val = int(remove_leading_zeros(v2[count]))
        if v1_val == v2_val and same_length and count == len(v2) - 1:
            return 0
        elif v1_val == v2_val:
            count += 1
            continue
        elif v1_val > v2_val:
            return 1
        else:
            return -1
    for section in longer[count::]:
        if remove_leading_zeros(section) == "0":
            continue
        else:
            return out
    return 0

def remove_leading_zeros(str):
    while len(str) > 1:
        if str[0] == "0":
            str = str[1::]
        else:
            break
    return str

def compare_versions_improved(v1,v2):
    v1 = [int(section) for section in v1.split(".")]
    v2 = [int(section) for section in v2.split(".")]
    count = 0
    while count < len(v1) and count < len(v2):
        if v1[count] == v2[count]:
            count += 1
            continue
        elif v1[count] > v2[count]:
            return 1
        else:
            return -1
    while count < len(v1):
        if v1[count] == 0:
            count += 1
            continue
        else:
            return 1
    while count < len(v2):
        if v2[count] == 0:
            count += 1
            continue
        else:
            return -1
    return 0



print(remove_leading_zeros("001"))
print(remove_leading_zeros("1"))

print(compare_versions("1.0.12","1.0.02.0.0.0"))
print(compare_versions_improved("1.1","1"))