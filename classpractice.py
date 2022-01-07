l = [True for i in range(100000001)]
val = 2
while(val*val<=100000000):
    if l[val]:
        x = val*val
        while x<=100000000:
            l[x] = False
            x += val
    val += 1

f = open("primes.txt","a")

for i in range(1,100000001):
    if l[i]:
        f.writelines(str(i)+"\n")
f.close()

print("Completed!")