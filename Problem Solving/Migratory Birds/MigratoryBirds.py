from collections import Counter

def migratoryBirds(arr):
    bird_counts = Counter(arr)
    max_count = max(bird_counts.values())
    most_frequent_birds = [bird for bird, count in bird_counts.items() if count == max_count]
    return min(most_frequent_birds)

array = [1, 4, 4, 4, 5, 3]
print(migratoryBirds(array)) 
