def wrapper(f):
    def fun(l):
        lis = []
        for item in l:
            lis.append('+91 '+item[-10:-5]+' '+ item[-5:])
        return f(lis)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
