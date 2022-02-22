# Hi, here's your problem today. This problem was recently asked by Facebook:

# Given a file path with folder names, '..' (Parent directory), and '.' (Current directory), return the shortest 
# possible file path (Eliminate all the '..' and '.').

# Example
# Input: '/Users/Joma/Documents/../Desktop/./../'
# Output: '/Users/Joma/'
# def shortest_path(file_path):
#   # Fill this in.

# print shortest_path('/Users/Joma/Documents/../Desktop/./../')
# # /Users/Joma/

def shortest_file_path(path):
    directories = [direct for direct in path.split('/')]
    print(directories)
        
    pos = 0
    for i in range(0,len(directories)):
        if directories[pos] == "":
            directories.pop(pos)
        elif directories[pos] == "..":
            pos -= 1
            directories.pop(pos)
            directories.pop(pos)
        elif directories[pos] == ".":
            directories.pop(pos)
        else:
            pos += 1

    print("/".join(directories))

shortest_file_path('/Users/Joma/Documents/../Desktop/./../')