from collections import Counter

def is_balanced(code):
    cache = Counter(code)
    print(cache)
    return cache

code = 'aabb'
is_balanced(code)

