"""
def welcome():
    print("welcome to the hundred acre wood")

welcome()

def greeting(name):
    print(f"welcome to the hundred acre wood {name}! My name is Christopher Robin")
    pass

greeting("Michael")
greeting("Winnie the pooh")

def print_catchphrase(character):

    if character == "pooh":
        print("Oh bother!")
    elif character == "tigger":
        print("TTFN: Tata for now")
    elif character == "Eeyore":
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")

print_catchphrase("pooh")
print_catchphrase("piglet")


def get_items(items, x):

    if x >= 0 and x < len(items):
        print(items[x])
        return items[x]
    else:
        print("invalid index")
        return None
    
items = ["piglet", "pooh", "rabbit", "roo"]
x = 4

get_items(items, x)

def sum_honey(hunny_jars):
    total = 0

    for jar in hunny_jars:
        total += jar

    print(total)
    return total

sum_honey(hunny_jars)

hunny_jars  = [2, 3, 4, 5]

def doubled(hunny_jars):
    
    for i in range(len(hunny_jars)):
        hunny_jars[i] *= 2

    print(hunny_jars)
    return hunny_jars

doubled(hunny_jars)

def count_less_than(race_times, threshold):
    count = 0

    for i in race_times:
        if i < threshold:
            count += 1

    print(count)
    return count

race_times = [1, 2, 3, 4, 5,]
threshold = 4

count_less_than(race_times, threshold)


def print_todo_list(tasks):

    print("Poohs todos")
    for task in range(len(tasks)):
        print(f"{task + 1}: {tasks[task]}")

    return None

tasks = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(tasks)

def can_pair(item_quantities):
    return all(qty % 2 == 0 for qty in item_quantities)

item_quantities = [3, 2, 4, 6, 8]

print(can_pair(item_quantities))
"""

def split_haycorns(quantity):
    result = []

    for i in range(1, quantity + 1):
        if quantity % i == 0:
            result.append(i)

    print(result)
    return result

split_haycorns(6)
split_haycorns(1)


