# 1 + 3 + + ....+ n
n = int(input("Enter last number of the series 1 + 3 +...+ n: "))
total = 0
for i in range(1,n+1,2):
    total += i
print(f"Total = {total}")