
"""
def linear_search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            print(i)
            return i
        else:
            print(-1)
            return -1
        
items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
linear_search(items, target)


def final_value_after_operations(operations):
    tigger = 1

    for i in operations:
        if i == "bouncy" or i == "flouncy":
            tigger += 1
        elif i == "trouncy" or i == "pouncy":
            tigger -= 1
    
    print(tigger)
    return tigger

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)


def mystery_function(s):
    count = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
    return count

result = mystery_function("AABBAB")
print(result)


def mystery_function(lst, threshold):
    total = 0
    i = 0
    while i < len(lst) and total + lst[i] <= threshold:
        total += lst[i]
        i += 1
    return total

result = mystery_function([1, 2, 3, 4, 5], 7)
print(result)


def tiggerfy(word):

    word = word.lower()
    word = word.replace("t", "")
    word = word.replace("i", "")
    word = word.replace("gg", "")
    word = word.replace("er", "")

    print(word)
    return word

tiggerfy("Trigger")
tiggerfy("eggplant")
tiggerfy("Choir")


def non_decreasing(nums):
    count = 0

    for i in range(0, len(nums) - 1):
        if nums[i + 1] == nums[i] + 1:
            continue
        else:
            count += 1

    if count <= 1:
        print("True")
        return True
    else:
        print("False")
        return False
    
nums = [4, 2, 1]
non_decreasing(nums)
"""

print("Hello world!")

def find_missing_clues(clues, lower, upper):
    # clues -> unique integer array
    # All clues are within inclusive range [lower, upper]
    p1 = 0
    ranges = []
    for i in range(len(clues)):
        if i == clues[p1]:
            p1 += 1
        else:
            ranges.append([i, clues[p1] - 1])

    print(ranges)
    return ranges

clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
find_missing_clues(clues, lower, upper)

print("hello world!")