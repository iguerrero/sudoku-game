import random
from itertools import permutations
import string

a = list(string.digits)
b = []
for i in range(len(a)):
    b.append(int(a[i]))
print(b)

a = [1,2,3,4,5,6,7,8,9]
for i in range(0,8,3):
    a.insert(i+3,a[i])
    a.pop(i)
print(a)
####################################3
# def permut():
#     a = permutations('roma')
#
#     for i in a:
#         print(i)

# permut()

####################################
# def choices():
#     choices = []
#     permuts = permutations([1,2,3])
#     for i in permuts:
#         choices.append(i)
#     ord = random.choice(choices)
#     a, b, c = ord
#     print(ord)
#     print(a, b, c)
#
# choices()

########################################
# def latSqr(x):
#     choices =[]
#     permuts = permutations([x, x + 1, x + 2])
#     for i in permuts:
#         choices.append(i)
#     ord = random.choice(choices)
#     a, b, c = ord
#
#     lats = [[[a, b, c], [b, c, a], [c, a, b]],[[a, b, c], [c, a, b], [b, c, a]]]
#     lat = random.choice(lats)
#
#
#     return lat
#
# print(latSqr(7))


