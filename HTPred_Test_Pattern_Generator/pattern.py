def pattern(lst):
    if len(lst)==1:
        return [lst]
    if len(lst)==0:
        return []
    x=[]
    for y in range(len(lst)):
       a=lst[y]
       rlst=lst[:y]+lst[y+1:]
       for z in pattern(rlst):
           x.append([a] + z)
    return x
l=[{'1'},{'0'},{'1','0'},{'1'},{'1'}]
for x in pattern(l):
    print(x)