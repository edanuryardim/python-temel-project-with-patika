input = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
newlist = []
def flatten(n):
    for i in n:
        if isinstance(i, list):
            flatten(i)
        else:
            newlist.append(i)


flatten(input)
print("flatten: " ,newlist)




