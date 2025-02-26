from collections import Counter

def is_balanced(code):
    cache = Counter(code)
    print(cache)
    print(len(cache))
    frequency_set = set(cache.values())

    if len(frequency_set) > 2:
        return False
    
    new_list = list(frequency_set)

    if new_list[0] - new_list[1] == 1 or new_list[0] - new_list[1] == -1:
        return True
    else:
        return False

code = 'aabb'
print(is_balanced(code))

