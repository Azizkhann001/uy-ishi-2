set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}

set4=set1.intersection(set2)
set3=set1.difference(set2)
print(sum(set4)-sum(set3))