#initialize list
high=100
values=list(range(high))

#sieve
for i in range (2,high):
    if values[i]==0:
        continue
    else:
        counter=2
        while counter*i<high:
            values[counter*i]=0
            counter+=1
values2=[]
total=0
sums=[]
sums.append(0)
values2.append(0)
for each in values:
    if each!=0 and each!=1:
        total+=each
        values2.append(each)
        sums.append(total)
#print(values2)
#print(sums)
maxrun=0
number=0
current_max=0
high_index=len(values2)-1



for index,start in enumerate(values2):
    current_max=high_index
    while current_max>index:
        current_sum=sums[current_max]-sums[index]
        if current_sum>high:
            high_index-=1
            current_max-=1
            continue
        if current_sum in values2:
            if current_max-index>maxrun:
                maxrun=current_max-index
                number=current_sum
                current_max-=1
        current_max-=1

print('--------------------------')
print('Max Run: '+str(maxrun))
print('Sum: '+str(number))
