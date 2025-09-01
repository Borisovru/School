def tr(x):
    y=''
    while x>0:
        y=str(x%3)+y
        x=x//3
    return y
def retr(y):
    x = 0
    count = 1
    while y:
        x+=count*int(y[-1])
        y = y[:-1]
        count*=3
    return x
m=0
for i in range(20):
    if i%3==0:
        mm=retr(tr(i)+tr(i)[-2:])
    else:
        mm=retr(tr(i) + tr(i%3*5))
    if mm<=173 and mm>m:
        m=mm
print(m)