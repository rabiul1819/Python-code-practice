# 1 + 2 + 3 + .....+ n
total = 0
n = int(input("Enter last number of the series 1+2+...+n: "))
for i in range(1,n+1,1):
    total += i
print(total)