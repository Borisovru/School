f = open('17.txt','r')
lines = f.readlines()
f.close()
m=0
count=0
MAX=0
for line in lines:
    if int(line)%100==17 and int(line)>MAX:
        MAX=int(line)
for i in range(len(lines)-2):
    c=0
    if len(lines[i]) ==4:
        c+=1
    if len(lines[i+1]) ==4:
        c+=1
    if len(lines[i+2]) ==4:
        c+=1
    if c == 2 and (int(lines[i]) %5==0 or int(lines[i+1]) %5==0 or int(lines[i+2]) %5==0) and int(lines[i])+int(lines[i+1])+int(lines[i+2]) >= MAX:
        count+=1
        if m<int(lines[i])+int(lines[i+1])+int(lines[i+2]):
            m=int(lines[i])+int(lines[i+1])+int(lines[i+2])
print(count)
print(m)