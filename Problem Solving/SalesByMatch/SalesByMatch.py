def sockMerchant(n, ar):
    color_count = {}
    

    for color in ar:
        color_count[color] = color_count.get(color, 0) + 1
    
    total_pairs = sum(count // 2 for count in color_count.values())
    
    return total_pairs

     