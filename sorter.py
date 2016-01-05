import time

def MinIndex(R) :
    result = -1
    i = -1
    for A in R :
        i += 1
        JeNajmensie = True
        for U in R :
            if A > U :
                JeNajmensie = False
        if JeNajmensie :
            return i

def MinIndex2(R) :
    Min = R[0]
    MinIndex = -1
    index = -1
    for A in R :
        index += 1
        if Min >= A :
            Min = A
            MinIndex = index
    return MinIndex        
            
P = [1, 0, 2, 1, 0, 4]
print MinIndex2(P)

c = -1
for X in P :
    print P
    c += 1
    i = MinIndex2(P[c:len(P)]) + c
    print i
    H = P[c]
    P[c] = P[i]
    P[i] = H
            
print P


time.sleep(10)
