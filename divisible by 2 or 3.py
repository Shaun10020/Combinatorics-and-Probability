n=1000

def divisible(num,integer):
    if num%integer==0:
        return True
    else:
        return False
count=0
for i in range(1000):
    if divisible(i+1,2):
        count+=1
    elif divisible(i+1,3):
        count+=1
print(count)
