def tr(x):
    y=''
    while x>0:
        y= str(x%9)+y
        x= x//9
    return y
print(tr(3**24-45))