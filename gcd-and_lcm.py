n1= int(input("enter a no 1:"))
n2= int(input("enter a no 2:"))
maxx=max(n1,n2)
minn=min(n1,n2)

#GCD (HCF)
gcd=0
for i in range(2,minn+1):
    if(n1%i==0 and n2%i==0):
        gcd=i

print(f" GCD of {n1} and {n2} is {gcd}")


#LCM 
lcm=0
for i in range(maxx,maxx*minn+1,maxx):
    if(i%minn==0):
        lcm=i
        break
print(f"LCM of {n1} and {n2} is {lcm}")
