import math

def distancecomp(in1, in2):
    count = int(0)
    for j in range(0, len(in1)-1, 1):
        #print(j)
        count = count + math.hypot(in1[j+1]-in1[j], in2[j+1]-in2[j])
        #print(count)
    print('*')
    print(math.hypot((in1[len(in1)-1]-in1[0]), (in2[len(in2)-1]-in2[0])))

x = [1,2,3, 4, 5, 6, 7, 0]
y = [1,4,9, 16,25,36,49, 0]
distancecomp(x, y)
print(x[0], x[1], x[2])
