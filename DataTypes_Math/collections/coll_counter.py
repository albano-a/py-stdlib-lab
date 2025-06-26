"""
Counter is a powerful and flexible tool for counting hashable objects.
It is a subclass of dict designed specifically for counting elements and provides many useful methods and
operations. Below is a comprehensive showcase of everything important about the Counter library.
"""

from collections import Counter


c1 = Counter()  # empty
c2 = Counter("abracadabra")  # from iterable (string)
c3 = Counter(["a", "b", "a", "c"])  # from list
c4 = Counter({"a": 2, "b": 3})  # from dict
c5 = Counter(a=4, b=2, c=0)  # from kwargs

print(c2["a"])  # count of 'a'
c2["z"] += 1  # increment 'z' (not present originally)
del c2["b"]  # delete key
print(c2["notfound"])  # returns 0, doesn't raise KeyError

c = Counter(a=2, b=1, c=0, d=-1)
print(list(c.elements()))  # ['a', 'a', 'b']
