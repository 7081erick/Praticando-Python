'''
    How to SETS() works...
    * add (Add), * update(Update/Add), * clear(Delete all), * discard(Remove)
    * Union (|) - Joins all elements of sets.
    * Intersection (&) - Show all elements present in both sets.
    * Difference (-) - Show only elements present in left set.
    * Symmetric_Difference (^) - Show elements present in one but not in other.

    OBS: Sets dont have keys, like dictionary, sets only have values. As a list, it works as a tuple (with immutable values and without indices). Besides that, sets don't respect orders, they show elements in random order. Sets don't show duplicate elements.
'''

# Using add()
create = set()
create.add(1)
create.add(2)
create.add(3)
create.add('Victor')
print(create)  # {1, 2, 3, 'Victor'}

print('=' * 30)
# Using update() -> Works like add(), but iterate the element
create_two = set()
create_two.update('Python')
create_two.update([8, 9, 10])
create_two.update((11, 12, 20))
print(create_two)  # {'t', 'h', 8, 'y', 'P', 'n', 9, 10, 11, 12, 'o', 20}

print('=' * 30)
# Using clear()
create_three = {1, 2, 3, 4, 5}
create_three.clear()
print(create_three)  # set()

print('=' * 30)
# Using discard()
create_four = {1, 2, 3, 4}
create_four.discard(2)
print(create_four)  # {1, 3, 4}

print('=' * 30)
# Using Intersction / &
create_five = {6, 7, 8, 9, 10, 11, 12, 13, 14}
create_inter = {6, 7, 8, 9, 10}
section = create_five & create_inter
print(section)  # {6, 7, 8, 9, 10}

print('=' * 30)
# Using Difference / -
create_six = {6, 7, 8, 9, 10, 11, 12, 13, 14}
create_rence = {6, 7, 8, 9, 10, 15}
dif = create_six - create_rence  # -> Only show left set, in this case create_six
print(dif)  # {11, 12, 13, 14}

print('=' * 30)
# Using Symmetric_Difference / ^
create_seven = {1, 2, 3, 4, 5, 6}
create_mer = {1, 2, 3, 4, 5, 7}
sy = create_seven ^ create_mer
print(sy)  # {6, 7}

print('=' * 30)
# Using Union / |
create_eigth = {1, 2, 3, 4, 5}
create_more = {6, 7, 8, 9, 10}
join = create_eigth | create_more
print(join)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}