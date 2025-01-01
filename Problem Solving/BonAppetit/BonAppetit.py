def bonAppetit(bill, k, b):
    total_cost = sum(bill) - bill[k]
    
    anna_share = total_cost // 2
    
    if b == anna_share:
        print("Bon Appetit")
    else:
        print(b - anna_share)

arr = [3, 12, 2, 9]
k = 1
b = 12
bonAppetit(arr, k, b) 