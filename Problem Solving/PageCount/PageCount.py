def pageCount(n, p):
    # Write your code here
    ft = p // 2
    tt = n // 2
    bt = tt - ft
    return min(ft , bt)

pageCount(6, 2) 