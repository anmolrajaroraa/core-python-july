'''
*
**
***
****
*****
'''

#k = 1
for i in range(5):
    for j in range(i+1):
        print('*', end='')

    #k += 1
    print()

'''
    *
   **
  ***
 ****
*****
'''

for i in range(5):
    for j in range(4 - i):
        print(" ", end='')
    for k in range(i + 1):
        print('*', end='')

    print()


'''
    *
   ***
  *****
 *******
*********

A
B C 
D E F
G H I J
K L M N O

a
a b
a b c
a b c d
a b c d e
'''

asciiCode = 65
for i in range(5):
    for j in range(i + 1):
        print(chr(asciiCode), end=" ")
        asciiCode += 1
    print()

print("********************")

for i in range(5):
    for j in range(4 - i):
        print(" ", end='')
    for k in range(2 * i + 1):
        print('*', end='')
    print()
