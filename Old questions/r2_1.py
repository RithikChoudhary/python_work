st=[1,5,9,7]
len1=len(st)

sts=st[0]
stm=st[0]
for i in range(0,len1-1):
  if(st[i]<st[i+1]):
    sts=st[i+1]
for i in range(0,len1-1):
  if(st[i]<stm):
    stm=st[i]
sum=sts+stm
print(sum)
