def add(n):
    z=n-1
    x=1
    for i in range(0,n):
        for i in range(0,z):
            print(' ',end='')
        for i in range(0,x):
            print('*',end='')
        for i in range(0,z):
            print(' ',end='')
        x=x+2
        z=z-1
        print()
add(6)

print(' ---------   ')
print('  -------    ')
print('   -----     ')
print('    ---      ')
print('     -      ')


add(6)
 	

def add(n):
    z = n-1
    x = 1
    for i in range(0,n):
        for i in range(x,0,-1):
            print(' ',end='')
        for i in range(0,z):
            print('*',end='')
        for i in range(0,z):
            print('*',end='')
        z = z-1    
        x = x+1
        
        print()
add(6)

def add(n):
    z=n-1
    x=1
    for i in range(0,n):
        for i in range(0,x):
            print('1',end='')
        for i in range(0,z):
            print('*',end='')
        for i in range(0,z):
            print('0',end='')
        x=x+2
        z=z-1
        print()
add(6)

