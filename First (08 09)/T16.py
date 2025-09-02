list=[0]
def F(n):
    global list
    if len(list) <= n:
        list.append(list[n//10]+ n%10)
    return list[n]
count=0
f2=0
for i in range(1134567010):
    f1=f2
    f2=F(i+1)
    if f1>f2 and i<=1134567009 and i>=237567892:
        count+=1
print(count)