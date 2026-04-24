# 1*1+ 2*2 + ....+ n*n
n = int(input("Enter last number of the series  1*1+ 2*2 + ....+ n*n: "))
total = 0
for i in range(1,n+1,1):
    total += i*i
print(f"Total = {total}")