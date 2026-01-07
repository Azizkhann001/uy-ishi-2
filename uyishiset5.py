
soz1=input("1-sozni kiriting:")
soz2=input("2-sozni kiriting:")

natija=True
for i in set(soz1):
    if soz1.count(i)!= soz2.count(i):
        natija=False
        break

print(natija)