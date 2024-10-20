from math import gcd
def RSA(p:int,q:int,message:int):
    n = p*q
    t = (p-1)*(q-1)
    for i in range(2,t):
        if gcd(i,t)==1:
            e=i
            break
    j=0
    while True:
        if(j*e)%t==1:
            d=j
            break
        j+=1
    ct = (message**e)%n
    print(f"Encrypted message is {ct}")
    mes = (ct**d)%n
    print(f"Decrypted message is {mes}")

print("Roll No: 2453021")
p = int(input("Enter p: "))
q = int(input("Enter q: "))
mes = int(input("Enter Message: "))
RSA(p,q,mes)