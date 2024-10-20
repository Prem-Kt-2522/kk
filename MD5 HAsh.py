import hashlib
print("Roll No: 2453021")
str2hash = "Implementation of MD5 HashAlgorithm"
#encoding given string using encode(),then sendig to MD5()
result = hashlib.md5(str2hash.encode())
print("The hexadecimal equivalent of hash is : ",end="")
print(result.hexdigest())
print(hashlib.algorithms_guaranteed)
print("MENU:\n1.MD5\n2.sha256\n3.sha512\n4.sha224\n5.sha1")
n = int(input("Enter your choice: "))
if n==1:
    result = hashlib.md5(str2hash.encode())
    print("The hexadecimal equivalent of hash is : ",end="")
    print(result.hexdigest())
elif n==2:
    result = hashlib.sha256(str2hash.encode())
    print("The hexadecimal equivalent of hash is : ",end="")
    print(result.hexdigest())
elif n==3:
    result = hashlib.sha512(str2hash.encode())
    print("The hexadecimal equivalent of hash is : ",end="")
    print(result.hexdigest())
elif n==4:
    result = hashlib.sha224(str2hash.encode())
    print("The hexadecimal equivalent of hash is : ",end="")
    print(result.hexdigest())
elif n==5:
    result = hashlib.sha1(str2hash.encode())
    print("The hexadecimal equivalent of hash is : ",end="")
    print(result.hexdigest())
else:
    print("Please enter valid option : ")
