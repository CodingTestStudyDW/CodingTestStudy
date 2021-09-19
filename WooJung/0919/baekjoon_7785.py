N = int(input())
log = {}
for i in range(N):
    name, enter = input().split()
    if enter == 'enter':
        log[name] = 1
    else:
        log[name] = 0
names = []
for name in log:
    if log[name] == 1:
        names.append(name)
for a in sorted(names, reverse = True):
    print(a)
    
    
###############################################
##   TIME OUT
###############################################

N = int(input())
name_ = []

for i in range(N):
    name, enter = input().split()
    if enter == 'enter':
        name_.append(name)
    else:
        name_.remove(name)  
for a in sorted(name_, reverse = True):
    print(a)
