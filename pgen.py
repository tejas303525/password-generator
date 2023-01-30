import random
import string
import json
#to create a random password generator
n=int(input("Enter the length of password: "))
d={}
name=input("Account name: ")

res="".join(random.choice(string.ascii_letters) for i in range(n))


for i in range(len(res)):
    if res not in d:
        d[name]=res
with open("passwordgen.txt","a") as f:
    f.write(json.dumps(d))
