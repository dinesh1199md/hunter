np=list(str(input()))
h=[]
for i in np:
  if i not in h:
    h.append(i)
print(*h,sep="")
