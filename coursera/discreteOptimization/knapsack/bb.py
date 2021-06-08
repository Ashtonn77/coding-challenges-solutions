def knapsack(c, k, est, val, currentBest):

    if val > currentBest:
        currentBest = val
    if k < 0 or est < currentBest:
        return 0

    valWithK = 0

    if w[k] <= c:
        valWithK = v[k] + knapsack(c - w[k], k - 1, est, val + v[k], currentBest)
    else:
        valWithK = 0

    valWithoutK = knapsack(c, k - 1, max(val, getBound(capacity, s, k)), val, currentBest)

    if valWithK > valWithoutK:
        x[k] = 1
    else:
        x[k] = 0

    return max(valWithoutK, valWithK)        



def getBound(c, n, skip):

    t = 0.0
    k = n

    while c > 0:
       
        if k == skip:
            k -= 1
            continue

        if w[k] <= c:
            t += v[k]
            c -= w[k]

        else:
            t = t + (c * (v[k] / w[k]))
            c = 0    

        k -= 1

    return t        


w = [3, 8, 5, 4]
v = [4, 15, 10, 8]
x = [0, 0, 0, 0]
s = 3
capacity = 11

est = getBound(capacity, s, -1)


print(knapsack(capacity, s, est, 0, 0))   
print(x)