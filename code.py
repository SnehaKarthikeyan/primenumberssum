Coding:
  
def fac(x):
   count=0
   for j in range(1,x+1):
      if x%j==0:
        count=count+1
   if count==2:
      return 1
   else:
      return 0
x=int(input())
i=0;
j=x;
while(1):
 if(fac(i) and fac(j) and i+j==x):
   print(i,end=" ")
   print(j)
   break
 else:
   i=i+1;
   j=j-1;
