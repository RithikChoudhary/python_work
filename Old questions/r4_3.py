st="who"
len1=len(st)
m=len1-1
sti=""
for i in range(0,len1):
  sti=sti +st[i]
sti=sti+'#'
for i in range(0,len1):
  sti=sti+st[m]
  m=m-1
print(sti)
