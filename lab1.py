
a = int(input ("Введіть а: "))

while (a < 1 or a > 100):

  a = int(input ("Введіть а в діапазоні від 1 до 100: "))
    
b = int(input ("Введіть b: "))

while (a < 1 or b > 100):

   b = int(input ("Введіть b в діапазоні від 1 до 100: "))
    
if a > b:

    x = (a / b + 1)

if a == b:

    x = a + 25
if a < b:

    x = (a * b - 2) / a


print("Результат обчислення виразу: " , x)
''' 
n=20
result = 1

for i in range(1, 2*n, 2):
    result *= i
    
print ("Добуток непарних чисел:", result)

n = 5
for i in range(n, 0, -1):
    p = ' ' * (n + 3 )
    print (p, end=" ")
    for j in range(i, n + 1,):
        print(j, end=" ")
    print()
    
for i in range(1, n + 1):
    print("  " * (n - i), end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
'''

