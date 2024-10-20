import numpy as np
pt = "defendtheeastwall"
print("Roll No:2453021")
print(len(pt))
x = (pt[0])
y = ""
for i in range(1,len(pt)):
    if (i%2==0):
        x += pt[i]
    else:
        y += pt[i]
final = x+y
print(final)


"""final = "dfnteataleedheswl"
half=len(final)/2
print(np.ceil(half))
nh = int(half)+1
print(nh)
x = ""
y=""
nx=""
z=""
for i in range(0,int(np.ceil(len(final)/2))):
   x +=final[i]
#print(final[i])

for i in range(nh,len(final)):
   y += final[i]
   #print(final[i])

print(x)
print(y)
subs = final[1:5]
print(subs)"""
def merge(x,y):
   result=""
   y1 = y.replace(" ","")
   i=0
   while(i<len(x) or i<len(y1)):
      if(i<len(x)):
         result +=x[i]
      if(i<len(y1)):
         result += y1[i]
      i+=1
   return result
print(merge(x,y))


