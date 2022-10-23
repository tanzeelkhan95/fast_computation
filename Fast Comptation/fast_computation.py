print()
h_string = "FAST COMPUTATION OF POWER"
new_string = h_string.center(55, ".")
print(new_string)
print()
n = int(input("ENTER THE VALUE OF n : "))
print()
k = int(input("ENTER THE VALUE OF k : "))
print()
m = int(input("ENTER THE VALUE OF m : "))
print()

def mod_power(n, k , m):
    r = 1
    while k>0:
        if k & 1 == 1:
            r = (r * n) % m
        n = (n * n) % m
        k >>= 1
    return r

print("THE RESULT IS : " + str(mod_power(n,k,m)))
print()
l_string = "PRESS ENTER TO CLOSE"
new1_string = l_string.center(55, ".")
print(new1_string)
print()
print("@2021 TANZEEL.TECH ALL RIGHT RESERVED")
input()