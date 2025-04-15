"""
def count_suits_iterative(suits):
    count = 0

    for i in suits:
        count += 1

    return count

def count_suits_recursive(suits):
    if not suits:
        return 0
    
    return count_suits_iterative(suits[1:]) + 1

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))


def sum_stones(stones):
    if not stones:
        return 0

    return sum_stones(stones[1:]) + stones[0]

print(sum_stones([5, 10, 15, 20, 25, 30]))
print(sum_stones([12, 8, 22, 16, 10]))"



def count_suits_iterative(suits):
    unique_suits = set()

    for i in suits:
        unique_suits.add(i)

    return len(unique_suits)

def count_suits_recursive(suits):

    if not suits:
        return 0
    
    first_suit = suits[0]
    rest_suits = suits[1:]

    unique_in_rest = count_suits_recursive(rest_suits)

    if first_suit in rest_suits:
        return unique_in_rest

    else:
        return 1 + unique_in_rest


print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))"
"""