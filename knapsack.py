def knapSack(W, waight, val, num):
    if num == 0 or W == 0:
        return 0

    if (waight[num - 1] > W):
        return knapSack(W, waight, val, num - 1)


    else:
        return max(val[num - 1] + knapSack(W - waight[num - 1], waight, val, num - 1),
                   knapSack(W, waight, val, num - 1))
    val = [60, 100, 120]
    waight = [10, 20, 30]
    W = 50
    num = len(val)
    print(knapSack(W, waight, val, num))