i = 2
print("Enter number: ")
n = int(input())
sum = 0
while i < n :
    if i % 3 == 0 and i % 5 == 0 or i % 3 == 0 or i % 5 == 0 :
        sum += i
    i += 1
print("Otvet", sum)
