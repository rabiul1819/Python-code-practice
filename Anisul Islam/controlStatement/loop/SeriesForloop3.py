# 2 + 4 + 6+ ....+ n
n = int(input("Enter last number of the series 2 + 4 +...+ n: "))
total = 0
for i in range(2,n+1,2):
    total += i
print(f"Total = {total}")