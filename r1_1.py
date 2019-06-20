st=[199,196,104]
len1=len(st)
sti=""
for i in range(0,len1):
  if(st[i]%4==0 and st[i]>=100 and st[i]<=200):
    sti=st[i]
    print(sti)
