s = int(input("Masofani kiriting: "))
v = int(input("Tezlikni kiriting: "))
t = int(input("Vqatni kiriting: "))
if s == 0:
    print(v*t)
elif v == 0:
    print(s/t)
elif t == 0:
    print(s/v)
else:
    print("I dont know")
    
