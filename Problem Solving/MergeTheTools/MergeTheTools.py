def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        print("".join(sorted(set(string[i:i+3]), key=string[i:i+3].index)))
        